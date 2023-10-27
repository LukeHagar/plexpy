from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.GetButlerTasksResponse import (
    GetButlerTasksResponse as GetButlerTasksResponseModel,
)
from ..models.TaskName import TaskName as TaskNameModel


class Butler(BaseService):
    def get_butler_tasks(self) -> GetButlerTasksResponseModel:
        """
        Get Butler tasks
        """

        url_endpoint = "/butler"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetButlerTasksResponseModel(**res)
        return res

    def start_all_tasks(self):
        """
        Start all Butler tasks
        """

        url_endpoint = "/butler"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, {}, True)
        return res

    def stop_all_tasks(self):
        """
        Stop all Butler tasks
        """

        url_endpoint = "/butler"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        return res

    def start_task(self, task_name: TaskNameModel):
        """
        Start a single Butler task
        Parameters:
        ----------
            task_name: TaskName
                the name of the task to be started.
        """

        url_endpoint = "/butler/{task_name}"
        headers = {}
        self._add_required_headers(headers)
        if not task_name:
            raise ValueError(
                "Parameter task_name is required, cannot be empty or blank."
            )
        validated_task_name = self._enum_matching(
            task_name, TaskNameModel.list(), "task_name"
        )
        url_endpoint = url_endpoint.replace(
            "{task_name}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, validated_task_name, None
                    )
                )
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, {}, True)
        return res

    def stop_task(self, task_name: TaskNameModel):
        """
        Stop a single Butler task
        Parameters:
        ----------
            task_name: TaskName
                The name of the task to be started.
        """

        url_endpoint = "/butler/{task_name}"
        headers = {}
        self._add_required_headers(headers)
        if not task_name:
            raise ValueError(
                "Parameter task_name is required, cannot be empty or blank."
            )
        validated_task_name = self._enum_matching(
            task_name, TaskNameModel.list(), "task_name"
        )
        url_endpoint = url_endpoint.replace(
            "{task_name}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, validated_task_name, None
                    )
                )
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        return res
