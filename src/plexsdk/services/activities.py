from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.GetServerActivitiesResponse import (
    GetServerActivitiesResponse as GetServerActivitiesResponseModel,
)


class Activities(BaseService):
    def get_server_activities(self) -> GetServerActivitiesResponseModel:
        """
        Get Server Activities
        """

        url_endpoint = "/activities"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetServerActivitiesResponseModel(**res)
        return res

    def cancel_server_activities(self, activity_uuid: str):
        """
        Cancel Server Activities
        Parameters:
        ----------
            activity_uuid: str
                The UUID of the activity to cancel.
        """

        url_endpoint = "/activities/{activity_uuid}"
        headers = {}
        self._add_required_headers(headers)
        if not activity_uuid:
            raise ValueError(
                "Parameter activity_uuid is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{activity_uuid}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, activity_uuid, None
                    )
                )
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        return res
