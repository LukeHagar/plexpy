from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService


class Media(BaseService):
    def mark_played(self, key: float):
        """
        Mark Media Played
        Parameters:
        ----------
            key: float
                The media key to mark as played
        """

        url_endpoint = "/:/scrobble"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not key:
            raise ValueError("Parameter key is required, cannot be empty or blank.")
        query_params.append(query_serializer.serialize_query("form", False, "key", key))
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        return res

    def mark_unplayed(self, key: float):
        """
        Mark Media Unplayed
        Parameters:
        ----------
            key: float
                The media key to mark as Unplayed
        """

        url_endpoint = "/:/unscrobble"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not key:
            raise ValueError("Parameter key is required, cannot be empty or blank.")
        query_params.append(query_serializer.serialize_query("form", False, "key", key))
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        return res

    def update_play_progress(self, state: str, time: float, key: str):
        """
        Update Media Play Progress
        Parameters:
        ----------
            key: str
                the media key
            time: float
                The time, in milliseconds, used to set the media playback progress.
            state: str
                The playback state of the media item.
        """

        url_endpoint = "/:/progress"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not key:
            raise ValueError("Parameter key is required, cannot be empty or blank.")
        query_params.append(query_serializer.serialize_query("form", False, "key", key))
        if not time:
            raise ValueError("Parameter time is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "time", time)
        )
        if not state:
            raise ValueError("Parameter state is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "state", state)
        )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.post(final_url, headers, {}, True)
        return res
