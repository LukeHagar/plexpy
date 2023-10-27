from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.Level import Level as LevelModel


class Log(BaseService):
    def log_line(self, source: str, message: str, level: LevelModel):
        """
        Logging a single line message.
        Parameters:
        ----------
            level: Level
                An integer log level to write to the PMS log with.
        0: Error
        1: Warning
        2: Info
        3: Debug
        4: Verbose

            message: str
                The text of the message to write to the log.
            source: str
                a string indicating the source of the message.
        """

        url_endpoint = "/log"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not level:
            raise ValueError("Parameter level is required, cannot be empty or blank.")
        validated_level = self._enum_matching(level, LevelModel.list(), "level")
        query_params.append(
            query_serializer.serialize_query("form", False, "level", validated_level)
        )
        if not message:
            raise ValueError("Parameter message is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "message", message)
        )
        if not source:
            raise ValueError("Parameter source is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "source", source)
        )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        return res

    def log_multi_line(self):
        """
        Logging a multi-line message
        """

        url_endpoint = "/log"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, {}, True)
        return res

    def enable_paper_trail(self):
        """
        Enabling Papertrail
        """

        url_endpoint = "/log/networked"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        return res
