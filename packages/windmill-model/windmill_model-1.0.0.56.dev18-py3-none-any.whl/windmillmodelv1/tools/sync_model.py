# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Model synchronization utility.

This module provides functionality for synchronizing models across devices,
handling device validation, model deployment, and status tracking.
"""

import json
import os
import tarfile
import time
import traceback
from argparse import ArgumentParser
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime
from functools import wraps
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple, Union

import bcelogger as logger
from devicev1.client.device_api import (
    ListDeviceRequest,
    GetConfigurationRequest,
    parse_device_name,
    InvokeMethodRequest,
    HTTPContent,
    UpdateDeviceRequest,
    DeviceStatus,
    DEVICE_STATUS_MAP,
)
from jobv1.client.job_api_base import JobStatus
from jobv1.client.job_api_event import EventKind
from jobv1.client.job_api_job import parse_job_name, GetJobRequest
from jobv1.client.job_api_metric import (
    MetricLocalName,
    MetricKind,
    CounterKind,
    DataType,
)
from jobv1.client.job_api_task import UpdateTaskRequest
from jobv1.client.job_client import JobClient
from jobv1.tracker.tracker import Tracker
from windmillartifactv1.client.artifact_api_artifact import parse_artifact_name
from windmillclient.client.windmill_client import WindmillClient
from windmillcomputev1.filesystem import blobstore, upload_by_filesystem
from windmillmodelv1.client.model_api_model import parse_model_name

# Constants
SYNC_MODEL = "Sync/Model"
SYNC_SKILL = "Sync/Skill"
DEFAULT_SLEEP_TIME = 15  # seconds
DEFAULT_ENDPOINT_HUB_NAME = "default"
DEFAULT_ENDPOINT_NAME = "default"
DEFAULT_ENDPOINT_TIMEOUT = 300  # seconds

RESOURCE_PATHS = {
    "workspace": "/v1/workspaces/{workspace_id}",
    "modelstore": "/v1/workspaces/{workspace_id}/modelstores/{store_name}",
    "endpointhub": "/v1/workspaces/{workspace_id}/endpointhubs/{hub_name}",
    "endpoint": "/v1/workspaces/{workspace_id}/endpointhubs/{hub_name}/endpoints/{endpoint_name}",
}


def error_handler(func):
    """Decorator for handling errors in sync manager methods."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {str(e)}")
            logger.debug(f"Stack trace: {traceback.format_exc()}")
            raise

    return wrapper


@dataclass
class Config:
    """Configuration container for model synchronization.

    Attributes:
        org_id: Organization ID
        user_id: User ID
        job_name: Name of the job
        spec_uri: URI of the specification
        windmill_endpoint: Endpoint for windmill service
        output_artifact_path: Path for output artifacts
        output_dir: Output directory
        job_kind: Kind of job (default: SYNC_MODEL)
        task_name: Name of the task (default: sync-model)
    """

    org_id: str
    user_id: str
    job_name: str
    spec_uri: str
    windmill_endpoint: str
    output_artifact_path: str
    output_dir: str = "."
    job_kind: str = SYNC_MODEL
    workspace_id: str = ""
    job_local_name: str = ""
    task_name: str = "sync-model"

    @classmethod
    def from_env(cls) -> "Config":
        """Create configuration from environment variables."""
        return cls(
            org_id=os.getenv("ORG_ID", "ab87a18d6bdf4fc39f35ddc880ac1989"),
            user_id=os.getenv("USER_ID", "7e0c86dd01ae4402aa0f4e003f3480fd"),
            job_name=os.getenv("JOB_NAME", "workspaces/wsgdessn/jobs/job-4va1ub51"),
            spec_uri=os.getenv(
                "SPEC_URI", "file:///root/pipelines/model/arm/k3s/import_model.yaml"
            ),
            windmill_endpoint=os.getenv("WINDMILL_ENDPOINT", "10.224.41.36:8340"),
            output_artifact_path=os.getenv(
                "PF_OUTPUT_ARTIFACT_DEVICE_DATA", "./device_data"
            ),
        )

    def validate(self) -> None:
        """Validate configuration parameters."""
        if not self.org_id:
            raise ValueError("org_id cannot be empty")
        if not self.user_id:
            raise ValueError("user_id cannot be empty")
        if not self.job_name:
            raise ValueError("job_name cannot be empty")
        if not self.windmill_endpoint:
            raise ValueError("windmill_endpoint cannot be empty")


@dataclass
class ModelDeploymentContext:
    """Model deployment context containing all necessary information."""

    model_info: Any
    devices: List[Any]
    upload_uri: str


class ModelSyncManager:
    """Manages model synchronization operations."""

    def __init__(self, config: Config, client: Optional[Union[WindmillClient, JobClient]] = None):
        """
        Initialize the sync manager.

        Args:
            config: Configuration object
            client: Windmill client/JobClient instance
        """
        self.config = config
        self.client = client
        self.tracker = None

    @error_handler
    def sync_model(
        self, artifact_name: str, device_names: List[str], device_hub_name: str
    ) -> None:
        """
        Synchronize model to devices.

        Args:
            artifact_name: Name of the artifact to sync
            device_names: List of device names to sync to
            device_hub_name: Name of the device hub
        """
        total_devices = len(device_names)
        try:
            # 初始化基础设置
            self._initialize_tracker()
            self._log_total_devices(total_devices)

            self._update_task_display_name()

            # 准备部署环境
            deployment_context = self._prepare_deployment_context(
                artifact_name, device_names, device_hub_name, total_devices
            )
            if not deployment_context:
                return

            # 执行部署
            valid_devices, invalid_device_msg = self._deploy_to_devices(
                deployment_context.model_info,
                deployment_context.devices,
                deployment_context.upload_uri,
            )

            # 处理部署结果
            self._handle_deployment_results(
                valid_devices, deployment_context.devices, invalid_device_msg
            )

            # 更新设备状态
            self._update_devices_status(deployment_context.devices)

        except Exception as e:
            self._handle_deployment_error(e, total_devices)
            raise

    def _update_task_display_name(self) -> None:
        """Update task display name."""
        self.client.update_task(
            UpdateTaskRequest(
                workspace_id=self.config.workspace_id,
                job_name=self.config.job_local_name,
                local_name=self.config.task_name,
                display_name="模型下发",
            )
        )

    def _initialize_tracker(self) -> None:
        """Initialize the tracker with parsed job name."""
        parsed_job_name = parse_job_name(self.config.job_name)
        if not parsed_job_name or not (
            parsed_job_name.local_name and parsed_job_name.workspace_id
        ):
            raise ValueError(f"Invalid job name: {self.config.job_name}")

        self.config.workspace_id = parsed_job_name.workspace_id
        self.config.job_local_name = parsed_job_name.local_name
        self._set_job_kind(parsed_job_name)
        self.tracker = Tracker(
            client=self.client,
            workspace_id=parsed_job_name.workspace_id,
            job_name=self.config.job_name,
            task_name=self.config.task_name,
        )

    def _log_total_devices(self, total: int) -> None:
        """Log the total number of devices."""
        self.tracker.log_metric(
            local_name=MetricLocalName.Total,
            kind=MetricKind.Counter,
            counter_kind=CounterKind.Cumulative,
            data_type=DataType.Int,
            value=[str(total)],
        )

    def _prepare_deployment_context(
        self,
        artifact_name: str,
        device_names: List[str],
        device_hub_name: str,
        total_devices: int,
    ) -> Optional[ModelDeploymentContext]:
        """
        Prepare deployment context with error handling.

        Args:
            artifact_name: Name of the artifact
            device_names: List of device names
            device_hub_name: Name of the device hub
            total_devices: Total number of devices

        Returns:
            ModelDeploymentContext if successful, None if preparation fails
        """
        try:
            model_info = self._prepare_model_info(artifact_name)
            devices = self._prepare_devices(model_info, device_names, device_hub_name)

            if not devices:
                self._handle_no_valid_devices(total_devices)
                return None

            upload_uri = self._prepare_and_upload_model(model_info)
            return ModelDeploymentContext(model_info, devices, upload_uri)

        except Exception as e:
            self._handle_deployment_error(e, total_devices, "preparation")
            raise

    def _prepare_devices(
        self, model_info: Dict[str, Any], device_names: List[str], device_hub_name: str
    ) -> List[Dict[str, Any]]:
        """
        Prepare and validate devices.

        Args:
            model_info: Model information dictionary
            device_names: List of device names
            device_hub_name: Name of the device hub

        Returns:
            List of valid devices
        """
        device_local_names = [
            parse_device_name(name).local_name for name in device_names
        ]

        device_workspace_id = parse_device_name(device_names[0]).workspace_id

        device_list = self.client.list_device(
            ListDeviceRequest(
                workspace_id=device_workspace_id,
                device_hub_name=device_hub_name,
                selects=device_local_names,
            )
        )

        if device_list.totalCount < 1:
            return []

        configs = self.client.get_configuration(
            GetConfigurationRequest(
                workspace_id=device_workspace_id,
                device_hub_name=device_hub_name,
                local_name="default",
            )
        )

        valid_devices = []
        invalid_devices_msg = []
        for device in device_list.result:
            is_valid, invalid_msg = self._validate_device(device, configs, model_info)
            if is_valid:
                valid_devices.append(device)
                self._update_device_status(device, DeviceStatus.Processing)

            if len(invalid_msg) > 0:
                invalid_devices_msg.append(invalid_msg)

        if len(invalid_devices_msg) > 0:
            self._log_invalid_devices_metrics(invalid_devices_msg)

        return valid_devices

    def _log_invalid_devices_metrics(self, invalid_msgs: List[str]) -> None:
        """
        Log metric and event for invalid devices.
        """
        count = len(invalid_msgs)
        self.tracker.log_metric(
            local_name=MetricLocalName.Failed,
            kind=MetricKind.Counter,
            counter_kind=CounterKind.Cumulative,
            data_type=DataType.Int,
            value=[str(count)],
        )
        error_message = "\n".join(invalid_msgs)
        self.tracker.log_event(
            kind=EventKind.Failed, reason="Invalid devices", message=error_message
        )

    def _validate_device_status(
        self, device: Dict[str, Any]
    ) -> Tuple[bool, Optional[str]]:
        """
        Validate device status.

        Args:
            device: Device information dictionary

        Returns:
            Tuple of (is_valid, error_message)
        """
        device_status = device.get("status")
        device_name = device.get("localName")

        valid_statuses = {
            SYNC_MODEL: {DeviceStatus.Connected.value},
            SYNC_SKILL: {DeviceStatus.Connected.value, DeviceStatus.Processing.value},
        }

        allowed_statuses = valid_statuses.get(self.config.job_kind, set())
        if not allowed_statuses:
            logger.error(f"Unknown job kind: {self.config.job_kind}")
            return False, self._format_device_err_msg(device, "未知的作业类型")

        if device_status not in allowed_statuses:
            status_desc = DEVICE_STATUS_MAP.get(device_status)
            logger.warning(
                f"Job kind: {self.config.job_kind} - Device {device_name} status ({device_status}) "
                f"is not in allowed states: {allowed_statuses}"
            )
            msg = f"设备状态不符合要求，当前状态为: {status_desc}"
            return False, self._format_device_err_msg(device, msg)

        return True, None

    def _validate_device(
        self, device: Dict[str, Any], configs: Any, model_info: Dict[str, Any]
    ) -> Tuple[bool, str]:
        """
        Validate device compatibility and status.

        Args:
            device: Device information
            configs: Device configurations
            model_info: Model information

        Returns:
            Tuple of (is_valid, error_message)
        """
        is_status_valid, invalid_msg = self._validate_device_status(device)
        if not is_status_valid:
            return False, invalid_msg

        device_gpu = self._get_device_support_gpu(
            device["kind"], configs.device_configs
        )

        if (
            device_gpu
            != model_info["model"].preferModelServerParameters["resource"][
                "accelerator"
            ]
        ):
            logger.warning(
                f"Device {device['localName']} does not support required GPU: {device_gpu}"
            )
            return False, self._format_device_err_msg(
                device, f"设备支持GPU与模型所需不符，设备GPU为: {device_gpu}"
            )
        return True, ""

    @staticmethod
    def _get_device_support_gpu(device_kind: str, device_configs: List[Any]) -> str:
        """
        Get device GPU support information.

        Args:
            device_kind: Kind of device
            device_configs: List of device configurations

        Returns:
            GPU support string
        """
        for device_config in device_configs:
            if device_config.kind == device_kind:
                return device_config.gpu
        return ""

    def _prepare_and_upload_model(self, model_info: Dict[str, Any]) -> str:
        """
        Prepare and upload model package.

        Args:
            model_info: Model information dictionary

        Returns:
            Upload URI string

        Raises:
            FileNotFoundError: If apply.yaml is not found
        """
        filesystem = self.client.suggest_first_filesystem(
            model_info["model_name"].workspace_id,
            guest_name=model_info["model_name"].get_name(),
        )

        # Generate apply.yaml
        from windmillartifactv1.client.artifact_api_artifact import get_name

        self.client.dump_models(
            artifact_name=str(
                get_name(
                    model_info["artifact"].object_name, model_info["artifact"].version
                )
            ),
            output_uri=self.config.output_dir,
            only_generate_structure=True,
        )

        apply_yaml_path = Path(self.config.output_dir) / "apply.yaml"
        if not apply_yaml_path.exists():
            raise FileNotFoundError("apply.yaml file does not exist")

        # Create and upload tarball
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        tar_name = f"{model_info['model_name'].local_name}-{model_info['artifact'].version}-{timestamp}.tar"

        with tarfile.open(tar_name, "w:") as tar:
            tar.add(str(apply_yaml_path), arcname="apply.yaml")

        bs = blobstore(filesystem=filesystem)
        job_path = bs.build_url(self.config.job_name)
        upload_uri = os.path.join(job_path, tar_name)

        logger.info(f"Uploading {tar_name} to {upload_uri}")
        upload_by_filesystem(filesystem, tar_name, upload_uri)
        logger.info(f"Uploaded {tar_name} to {upload_uri}")

        return upload_uri

    def _handle_deployment_results(
        self,
        valid_devices: List[Any],
        all_devices: List[Any],
        invalid_device_msg: List[str],
    ) -> None:
        """Handle deployment results and update metrics accordingly."""
        valid_count = len(valid_devices)
        total_count = len(all_devices)
        invalid_count = len(invalid_device_msg)

        # 处理成功设备
        if valid_count > 0:
            self._log_success_metrics(valid_count)

        # 确定并记录状态
        status = self._determine_job_status(valid_count, total_count)
        self._log_status_metric(status)

        # 处理失败设备
        if invalid_count > 0:
            self._handle_invalid_devices(invalid_count, invalid_device_msg)

    def _log_success_metrics(self, valid_count: int) -> None:
        """Log metrics for successful deployments."""
        self.tracker.log_metric(
            local_name=MetricLocalName.Success,
            kind=MetricKind.Counter,
            counter_kind=CounterKind.Cumulative,
            data_type=DataType.Int,
            value=[str(valid_count)],
        )

    @staticmethod
    def _determine_job_status(valid_count: int, total_count: int) -> JobStatus:
        """Determine job status based on deployment results."""
        if valid_count == total_count:
            return JobStatus.Succeeded
        elif valid_count > 0:
            return JobStatus.PartialSucceeded
        return JobStatus.Failed

    def _log_status_metric(self, status: JobStatus) -> None:
        """Log job status metric."""
        self.tracker.log_metric(
            local_name=MetricLocalName.Status,
            kind=MetricKind.Gauge,
            counter_kind=CounterKind.Monotonic,
            data_type=DataType.String,
            value=[status.value],
        )

    def _handle_invalid_devices(
        self, invalid_count: int, invalid_device_msg: List[str]
    ) -> None:
        """Handle and log metrics for invalid devices."""
        error_message = "\n".join(invalid_device_msg)
        self._log_failure_metrics(invalid_count, error_message, error_message)

    def _handle_deployment_error(
        self, error: Exception, total_devices: int, context: str = "deployment"
    ) -> None:
        """Handle deployment errors with detailed logging."""
        error_details = {
            "type": type(error).__name__,
            "message": str(error),
            "context": context,
        }

        logger.error(
            "Deployment error: %s\nContext: %s\nStack trace:\n%s",
            error_details["message"],
            error_details["context"],
            traceback.format_exc(),
        )

        error_message = (
            f"部署失败\t"
            f"错误类型: {error_details['type']}\t"
            f"错误信息: {error_details['message']}\t"
            f"错误位置: {error_details['context']}"
        )

        self._log_failure_metrics(total_devices, error_message, str(error))

    def _log_failure_metrics(self, count: int, reason: str, message: str) -> None:
        """Log metrics and events for failures."""
        self.tracker.log_event(kind=EventKind.Failed, reason=reason, message=message)

        self.tracker.log_metric(
            local_name=MetricLocalName.Failed,
            kind=MetricKind.Counter,
            counter_kind=CounterKind.Cumulative,
            data_type=DataType.Int,
            value=[str(count)],
        )

        self.tracker.log_metric(
            local_name=MetricLocalName.Status,
            kind=MetricKind.Gauge,
            counter_kind=CounterKind.Cumulative,
            data_type=DataType.String,
            value=[JobStatus.Failed.value],
        )

    def _handle_no_valid_devices(self, total_devices: int) -> None:
        """Handle the case when no valid devices are found."""
        logger.warning("No valid devices found")
        self._log_failure_metrics(
            total_devices, "没有符合下发要求的设备", "没有符合下发要求的设备"
        )

    def _update_devices_status(self, devices: List[Any]) -> None:
        """Update status for all devices."""
        for device in devices:
            self._update_device_status(device, DeviceStatus.Connected)

    def _set_job_kind(self, job_name) -> None:
        """Set job kind based on job name."""
        job = self.client.get_job(
            GetJobRequest(
                workspace_id=job_name.workspace_id,
                local_name=job_name.local_name,
            )
        )
        self.config.job_kind = job.kind

    @error_handler
    def _prepare_model_info(self, artifact_name: str) -> Dict[str, Any]:
        """
        Prepare model information.

        Args:
            artifact_name: Name of the artifact

        Returns:
            Dictionary containing model information

        Raises:
            ValueError: If model information cannot be prepared
        """
        parsed_artifact = parse_artifact_name(artifact_name)
        if not parsed_artifact:
            raise ValueError(f"Failed to parse artifact name: {artifact_name}")

        logger.info(f"Model artifact object name: {parsed_artifact.object_name}")

        model_name = parse_model_name(parsed_artifact.object_name)
        if not model_name:
            raise ValueError(
                f"Failed to parse model name from: {parsed_artifact.object_name}"
            )

        logger.info(f"Parsed model name: {model_name}")

        # Validate required attributes
        if not all(
            [
                hasattr(model_name, attr) and getattr(model_name, attr)
                for attr in ["workspace_id", "model_store_name", "local_name"]
            ]
        ):
            raise ValueError("Invalid model name: missing required attributes")

        model = self.client.get_model(
            model_name.workspace_id,
            model_name.model_store_name,
            model_name.local_name,
        )

        if not model:
            raise ValueError(f"Could not find model: {model_name}")

        return {
            "artifact": parsed_artifact,
            "model_name": model_name,
            "model": model,
        }

    def _update_device_status(self, device, status):
        self.client.update_device(
            UpdateDeviceRequest(
                workspace_id=device["workspaceID"],
                device_hub_name=device["deviceHubName"],
                device_name=device["localName"],
                status=status,
            )
        )

    @staticmethod
    def _format_device_err_msg(device, msg) -> str:
        return f"{device['displayName']}({device['localName']}) - {msg}"

    def _deploy_to_devices(
        self, model_info: Dict[str, Any], devices: List[Dict[str, Any]], upload_uri: str
    ) -> Tuple[List[Dict[str, Any]], List[str]]:
        """
        Deploy model to devices.

        Args:
            model_info: Model information
            devices: List of devices
            upload_uri: URI of the uploaded model

        Returns:
            Tuple of (valid_devices, error_messages)
        """
        valid_device = []
        invalid_device_msg = []
        success_devices = {}

        for device in devices:
            try:
                with self._deployment_context(device):
                    self._prepare_device_resources(device, model_info)
                    import_job = self._create_import_job(device, model_info, upload_uri)

                    time.sleep(DEFAULT_SLEEP_TIME)

                    device_model_artifact_name = self._wait_for_import_job_completion(
                        device, import_job
                    )

                    self._create_deploy_job(device, device_model_artifact_name)

                    # 等待helm命令执行完成
                    time.sleep(DEFAULT_SLEEP_TIME)

                    if self._wait_for_endpoint_ready(device):
                        valid_device.append(device)
                        success_devices[device["name"]] = {
                            "artifactName": device_model_artifact_name,
                        }
                    else:
                        invalid_device_msg.append(
                            self._format_device_err_msg(device, "部署超时")
                        )

            except Exception as e:
                logger.error(
                    f"Deployment failed for device {device['localName']}: {str(e)}"
                )
                invalid_device_msg.append(
                    self._format_device_err_msg(device, f"部署失败: {str(e)}")
                )

        self._save_success_devices(success_devices)

        return valid_device, invalid_device_msg

    @contextmanager
    def _deployment_context(self, device: Dict[str, Any]):
        """Context manager for device deployment."""
        try:
            yield
        except Exception as e:
            logger.error(f"Deployment error for device {device['localName']}: {str(e)}")
            self._update_device_status(device, DeviceStatus.Connected)
            raise

    def _prepare_device_resources(
        self, device: Dict[str, Any], model_info: Dict[str, Any]
    ) -> None:
        """
        Prepare necessary device resources.

        Args:
            device: Device information
            model_info: Model information
        """
        resource_checks = [
            ("workspace", "/v1/workspaces/{workspace_id}", {"id": "{workspace_id}"}),
            (
                "modelstore",
                "/v1/workspaces/{workspace_id}/modelstores/{store_name}",
                {"localName": "{store_name}"},
            ),
            (
                "endpointhub",
                "/v1/workspaces/{workspace_id}/endpointhubs/{hub_name}",
                {"localName": "{hub_name}"},
            ),
            (
                "endpoint",
                "/v1/workspaces/{workspace_id}/endpointhubs/{hub_name}/endpoints/{endpoint_name}",
                {"localName": "{endpoint_name}", "kind": "BIEEndpoint"},
            ),
        ]

        workspace_id = device.get("workspaceID")
        for resource_name, check_path, create_body in resource_checks:
            try:
                self._check_and_create_resource(
                    workspace_id,
                    device,
                    resource_name,
                    check_path,
                    create_body,
                    model_info,
                )
            except Exception as e:
                logger.error(f"Failed to prepare {resource_name}: {str(e)}")
                raise

    def _check_and_create_resource(
        self,
        workspace_id: str,
        device: Dict[str, Any],
        resource_name: str,
        check_path: str,
        create_body: Dict[str, str],
        model_info: Dict[str, Any],
    ) -> None:
        """Check if resource exists and create if it doesn't."""
        try:
            check_req = HTTPContent(
                method="get",
                params=check_path.format(
                    workspace_id=workspace_id,
                    store_name=model_info["model_name"].model_store_name,
                    hub_name=DEFAULT_ENDPOINT_HUB_NAME,
                    endpoint_name=DEFAULT_ENDPOINT_NAME,
                ),
            )
            self.client.invoke_method(
                InvokeMethodRequest(
                    workspace_id=workspace_id,
                    device_hub_name=device["deviceHubName"],
                    device_name=device["localName"],
                    protocol="HTTP",
                    content=check_req.model_dump(),
                )
            )
            logger.info(f"{resource_name.capitalize()} exists")
        except Exception as e:
            logger.info(f"Get {resource_name} with error: {str(e)}")
            self._create_resource(
                workspace_id, device, resource_name, check_path, create_body, model_info
            )

    def _create_resource(
        self,
        workspace_id: str,
        device: Dict[str, Any],
        resource_name: str,
        check_path: str,
        create_body: Dict[str, str],
        model_info: Dict[str, Any],
    ) -> None:
        """Create a resource."""
        create_path = "/".join(check_path.split("/")[:-1])
        logger.info(f"Creating {resource_name} at path: {create_path}")

        body = {
            k: v.format(
                workspace_id=workspace_id,
                store_name=model_info["model_name"].model_store_name,
                hub_name="default",
                endpoint_name="default",
            )
            for k, v in create_body.items()
        }

        create_req = HTTPContent(
            method="post",
            params=create_path.format(
                workspace_id=workspace_id,
                store_name=model_info["model_name"].model_store_name,
                hub_name="default",
                endpoint_name="default",
            ),
            body=json.dumps(body),
        )

        self.client.invoke_method(
            InvokeMethodRequest(
                workspace_id=workspace_id,
                device_hub_name=device["deviceHubName"],
                device_name=device["localName"],
                protocol="HTTP",
                content=create_req.model_dump(),
            )
        )

    def _create_import_job(
        self, device: Dict[str, Any], model_info: Dict[str, Any], upload_uri: str
    ) -> Any:
        """
        Create import job for model deployment.

        Args:
            device: Device information
            model_info: Model information
            upload_uri: URI of the uploaded model

        Returns:
            Import job response
        """
        import_job_request = {
            "workspaceID": device.get("workspaceID"),
            "specURI": self.config.spec_uri,
            "sourceURI": upload_uri,
            "sourceFilesystem": self.client.suggest_first_filesystem(
                device.get("workspaceID"),
                guest_name=model_info["model_name"].get_name(),
            ),
            "specKind": "Kube",
        }

        import_job_req = HTTPContent(
            method="post",
            params=f"/v1/workspaces/{device.get('workspaceID')}"
            f"/modelstores/{model_info['model_name'].model_store_name}/models/import",
            body=json.dumps(import_job_request),
        )

        return self.client.invoke_method(
            InvokeMethodRequest(
                workspace_id=device.get("workspaceID"),
                device_hub_name=device.get("deviceHubName"),
                device_name=device.get("localName"),
                protocol="HTTP",
                content=import_job_req.model_dump(),
            )
        )

    def _wait_for_endpoint_ready(self, device: Dict[str, Any], timeout: int = 600):
        """
        Wait for endpoint to be ready.
        """
        start_time = time.time()
        get_endpoint_status_req = HTTPContent(
            method="get",
            params=f"/v1/workspaces/{device.get('workspaceID')}/endpointhubs/default"
            f"/endpoints/default/endpointstatus",
        )

        while time.time() - start_time < timeout:
            get_endpoint_status_resp = self.client.invoke_method(
                InvokeMethodRequest(
                    workspace_id=device.get("workspaceID"),
                    device_hub_name=device.get("deviceHubName"),
                    device_name=device.get("localName"),
                    protocol="HTTP",
                    content=get_endpoint_status_req.model_dump(),
                )
            )

            logger.info(
                f"Endpoint default for device {device.get('localName')}"
                f" is {get_endpoint_status_resp.status}"
            )

            if get_endpoint_status_resp.status == "Available":
                return True

            time.sleep(DEFAULT_SLEEP_TIME)

        raise TimeoutError(f"预测服务在 {timeout}秒 内未就绪")

    def _wait_for_import_job_completion(
        self,
        device: Dict[str, Any],
        import_job: Any,
        timeout: int = 6000,
    ) -> str:
        """
        Wait for import job completion with timeout.

        Args:
            device: Device information
            import_job: Import job instance
            timeout: Maximum wait time in seconds

        Returns:
            Artifact name string

        Raises:
            TimeoutError: If job doesn't complete within timeout
        """
        start_time = time.time()
        get_job_req = HTTPContent(
            method="get",
            params=f"/v1/workspaces/{device.get('workspaceID')}"
            f"/jobs/{import_job.localName}",
        )

        while time.time() - start_time < timeout:
            get_job_resp = self.client.invoke_method(
                InvokeMethodRequest(
                    workspace_id=device.get("workspaceID"),
                    device_hub_name=device.get("deviceHubName"),
                    device_name=device.get("localName"),
                    protocol="HTTP",
                    content=get_job_req.model_dump(),
                )
            )

            logger.info(
                f"Import job {import_job.localName} for device {device.get('localName')}"
                f" is {get_job_resp.status} - tags: {get_job_resp.tags}"
            )

            if get_job_resp.status == JobStatus.Succeeded.value:
                return get_job_resp.tags["artifactName"]

            time.sleep(DEFAULT_SLEEP_TIME)

        raise TimeoutError(f"模型导入任务 {timeout} 秒后未完成")

    def _create_deploy_job(self, device: Dict[str, Any], artifact_name: str) -> Any:
        """
        Deploy model to a single device.

        Args:
            device: Device information
            artifact_name: Name of the artifact

        Returns:
            Deploy job response
        """
        deploy_job_request = {
            "workspaceID": device.get("workspaceID"),
            "endpointHubName": DEFAULT_ENDPOINT_HUB_NAME,
            "kind": "Deploy",
            "endpointName": DEFAULT_ENDPOINT_NAME,
            "artifactName": artifact_name,
            "specKind": "Helm",
            "specName": "workspaces/public/endpointhubs/default/deployments/triton-bm1688/versions/latest",
        }

        deploy_job_req = HTTPContent(
            method="post",
            params=f"/v1/workspaces/{device.get('workspaceID')}"
            f"/endpointhubs/default/jobs",
            body=json.dumps(deploy_job_request),
        )

        return self.client.invoke_method(
            InvokeMethodRequest(
                workspace_id=device.get("workspaceID"),
                device_hub_name=device.get("deviceHubName"),
                device_name=device.get("localName"),
                protocol="HTTP",
                content=deploy_job_req.model_dump(),
            )
        )

    def _save_success_devices(self, success_devices: Dict[str, Any]) -> None:
        """Save successful device information to artifact."""
        if len(success_devices) == 0:
            logger.warning("No successful devices found")
            return
        success_devices_json = json.dumps(success_devices)
        with open(self.config.output_artifact_path, "w") as f:
            f.write(success_devices_json)


def parse_args() -> ArgumentParser:
    """Parse command line arguments."""
    parser = ArgumentParser(description="Model synchronization utility")
    parser.add_argument(
        "--artifact_name", required=True, type=str, help="Name of the artifact to sync"
    )
    parser.add_argument(
        "--device_names",
        required=True,
        type=str,
        help="Comma-separated list of device names",
    )
    parser.add_argument(
        "--device_hub_name", default="default", type=str, help="Name of the device hub"
    )
    return parser.parse_args()


def main() -> int:
    """
    Main entry point.

    Returns:
        0 on success, 1 on failure
    """
    try:
        args = parse_args()
        config = Config.from_env()
        config.validate()

        client = JobClient(
            endpoint=config.windmill_endpoint,
            context={"OrgID": config.org_id, "UserID": config.user_id},
        )

        sync_manager = ModelSyncManager(config, client=client)
        sync_manager.sync_model(
            args.artifact_name, args.device_names.split(","), args.device_hub_name
        )
        return 0
    except Exception as e:
        logger.error(f"Sync_model failed: {str(e)}")
        logger.debug(f"Stack trace: {traceback.format_exc()}")
        return 1


if __name__ == "__main__":
    exit(main())
