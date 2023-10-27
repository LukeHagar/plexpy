from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.GetTranscodeSessionsResponse import (
    GetTranscodeSessionsResponse as GetTranscodeSessionsResponseModel,
)


class Sessions(BaseService):
    def get_sessions(self):
        """
        Get Active Sessions
        """

        url_endpoint = "/status/sessions"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        return res

    def get_session_history(self):
        """
        Get Session History
        """

        url_endpoint = "/status/sessions/history/all"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        return res

    def get_transcode_sessions(self) -> GetTranscodeSessionsResponseModel:
        """
        Get Transcode Sessions
        """

        url_endpoint = "/transcode/sessions"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetTranscodeSessionsResponseModel(**res)
        return res

    def stop_transcode_session(self, session_key: str):
        """
        Stop a Transcode Session
        Parameters:
        ----------
            session_key: str
                the Key of the transcode session to stop
        """

        url_endpoint = "/transcode/sessions/{session_key}"
        headers = {}
        self._add_required_headers(headers)
        if not session_key:
            raise ValueError(
                "Parameter session_key is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{session_key}",
            quote(
                str(query_serializer.serialize_path("simple", False, session_key, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        return res
