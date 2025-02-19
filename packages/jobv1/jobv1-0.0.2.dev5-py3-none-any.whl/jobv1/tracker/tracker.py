#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/11/1
# @Author  : zhoubohan
# @File    : tracker.py
"""

import atexit
import os
import queue
import threading
from typing import Optional, Union, List

from jobv1.client.job_api_event import CreateEventRequest, EventKind
from jobv1.client.job_api_job import parse_job_name, JobName
from jobv1.client.job_api_metric import (
    CreateMetricRequest,
    MetricLocalName,
    MetricKind,
    CounterKind,
    DataType,
)
from jobv1.client.job_api_task import CreateTaskRequest, parse_task_name, TaskName
from jobv1.client.job_client import JobClient
from windmillclient.client.windmill_client import WindmillClient


class Tracker:
    """Tracker is an agent to track metrics & events."""

    def __init__(
        self,
        client: Optional[Union[WindmillClient, JobClient]] = None,
        workspace_id: Optional[str] = None,
        job_name: Optional[str] = None,
        task_name: Optional[str] = None,
    ):
        """Initialize a new Tracker.

        Args:
            client: WindmillClient or JobClient instance.
            workspace_id: Workspace ID.
            job_name: Job name.
            task_name: Task name.

        Raises:
            ValueError: If required environment variables are not set when client is None.
            TypeError: If client is not an instance of WindmillClient or JobClient.
        """
        self._workspace_id = workspace_id or os.getenv("WORKSPACE_ID")
        self._job_name = job_name or os.getenv("JOB_NAME")
        self._task_name = task_name or os.getenv("TASK_NAME")

        self._client = client or self._initialize_client()

        self._validate_client()
        self._update_names()

        self._queue = queue.Queue()
        self._thread = threading.Thread(target=self._process_queue, daemon=True)
        self._thread.start()

        atexit.register(self._cleanup)

    @staticmethod
    def _initialize_client(self) -> JobClient:
        """Initialize the JobClient if not provided."""
        endpoint = os.getenv("WINDMILL_ENDPOINT")
        org_id = os.getenv("ORG_ID")
        user_id = os.getenv("USER_ID")

        if not all([endpoint, org_id, user_id]):
            raise ValueError(
                "Environment variables WINDMILL_ENDPOINT, ORG_ID, and USER_ID must be set "
                "when client is not provided."
            )

        return JobClient(
            endpoint=endpoint, context={"OrgID": org_id, "UserID": user_id}
        )

    def _validate_client(self):
        """Validate the provided client."""
        if not isinstance(self._client, (WindmillClient, JobClient)):
            raise TypeError(
                f"Client must be either WindmillClient or JobClient, got {type(self._client)}"
            )

    def _update_names(self):
        """Update job and task names based on parsed values."""
        if self._job_name:
            self.set_job_name(self._job_name)
        if self._task_name:
            self.set_task_name(self._task_name)

    def _process_queue(self):
        """Process the queue asynchronously."""
        while True:
            func, args = self._queue.get()
            if func is None:
                break
            func(args)
            self._queue.task_done()

    def _cleanup(self):
        """Cleanup the tracker."""
        self._queue.put((None, ()))
        self._thread.join()

    def set_job_name(self, job_name: str):
        """Set job name."""
        if (jn := parse_job_name(job_name)) is not None:
            self._job_name, self._workspace_id = jn.local_name, jn.workspace_id
        else:
            self._job_name = job_name

    def set_task_name(self, task_name: str):
        """Set task name."""
        if (tn := parse_task_name(task_name)) is not None:
            self._task_name, self._job_name, self._workspace_id = (
                tn.local_name,
                tn.job_name,
                tn.workspace_id,
            )
        else:
            self._task_name = task_name

    def _set_default(
        self, request: Union[CreateTaskRequest, CreateMetricRequest, CreateEventRequest]
    ):
        """Set default values for request."""
        request.workspace_id = request.workspace_id or self._workspace_id
        request.job_name = (
            request.job_name
            or JobName(
                workspace_id=self._workspace_id, local_name=self._job_name
            ).get_name()
        )

        if request.field_exists("task_name") and self._task_name is not None:
            request.task_name = (
                request.task_name
                or TaskName(
                    workspace_id=self._workspace_id,
                    job_name=self._job_name,
                    local_name=self._task_name,
                ).get_name()
            )

    def create_task(
        self,
        kind: str,
        local_name: Optional[str] = None,
        job_name: Optional[str] = None,
        display_name: Optional[str] = None,
        description: Optional[str] = None,
        order: Optional[int] = 0,
    ):
        """Create a task."""
        self._update_job_and_task_names(job_name, local_name)

        request = CreateTaskRequest(
            kind=kind,
            local_name=self._task_name,
            job_name=JobName(
                workspace_id=self._workspace_id, local_name=self._job_name
            ).get_name(),
            display_name=display_name,
            description=description,
            order=order,
        )
        self._set_default(request)
        self._queue.put((self._client.create_task, request))

    def log_metric(
        self,
        value: List[str],
        local_name: MetricLocalName = MetricLocalName.Status,
        kind: MetricKind = MetricKind.Gauge,
        data_type: DataType = DataType.String,
        counter_kind: CounterKind = CounterKind.Cumulative,
        job_name: Optional[str] = None,
        task_name: Optional[str] = None,
    ):
        """Log a metric."""
        self._update_job_and_task_names(job_name, task_name)

        request = CreateMetricRequest(
            value=value,
            local_name=local_name,
            kind=kind,
            data_type=data_type,
            counter_kind=counter_kind,
            job_name=JobName(
                workspace_id=self._workspace_id, local_name=self._job_name
            ).get_name(),
        )
        self._set_default(request)
        self._queue.put((self._client.create_metric, request))

    def log_event(
        self,
        reason: str,
        message: str,
        kind: Optional[EventKind] = EventKind.Normal,
        task_name: Optional[str] = None,
        job_name: Optional[str] = None,
    ):
        """Log an event."""
        self._update_job_and_task_names(job_name, task_name)

        request = CreateEventRequest(
            reason=reason,
            message=message,
            kind=kind,
            job_name=JobName(
                workspace_id=self._workspace_id, local_name=self._job_name
            ).get_name(),
        )
        self._set_default(request)
        self._queue.put((self._client.create_event, request))

    def _update_job_and_task_names(
        self, job_name: Optional[str], task_name: Optional[str]
    ):
        """Update job_name and task_name attributes based on parsed inputs."""
        if job_name:
            if (jn := parse_job_name(job_name)) is not None:
                self._workspace_id, self._job_name = jn.workspace_id, jn.local_name
            else:
                self._job_name = job_name

        if task_name:
            if (tn := parse_task_name(task_name)) is not None:
                self._workspace_id, self._job_name, self._task_name = (
                    tn.workspace_id,
                    tn.job_name,
                    tn.local_name,
                )
            else:
                self._task_name = task_name
