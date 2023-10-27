"""
Creates a BaseService class.
Performs API calls,sets authentication tokens and handles http exceptions.

Class:
    BaseService
"""
from typing import List, Union
from enum import Enum
import re
from ..net.http_client import HTTPClient


class BaseService:
    """
    A class to represent a base serivce

    Attributes
    ----------
    _url_prefix : str
        The base URL

    Methods
    -------

    set_api_key(api_key: str, api_key_header: str = None) -> None:
        Sets api key and api key header name
    def _add_required_headers(headers: dict):
        Request authorization headers
    def set_base_url(url: str):
        Sets the base url
    """

    _url_prefix = "http://10.10.10.47:32400"

    _http = HTTPClient(None)

    def __init__(self, api_key: str = "", api_key_header: str = "X-Plex-Token") -> None:
        """
        Initialize client

        Parameters:
        ----------
            api_key : str
                The API Key access token
            api_key_header : str
                The API Key header name
        """
        self._api_key = api_key
        self._api_key_header = api_key_header

    def _pattern_matching(cls, value: str, pattern: str, variable_name: str):
        if re.match(r"{}".format(pattern), value):
            return value
        else:
            raise ValueError(f"Invalid value for {variable_name}: must match {pattern}")

    def _enum_matching(
        cls, value: Union[str, Enum], enum_values: List[str], variable_name: str
    ):
        str_value = value.value if isinstance(value, Enum) else value
        if str_value in enum_values:
            return value
        else:
            raise ValueError(
                f"Invalid value for {variable_name}: must match one of {enum_values}"
            )

    def set_base_url(self, url: str) -> None:
        """
        Sets the base URL

        Parameters:
        ----------
            url:
                The base URL
        """
        self._url_prefix = url

    def set_api_key(self, api_key: str, api_key_header: str = None) -> None:
        """
        Sets api key and api key header name

        Parameters
        ----------
        api_key: string
            API Key value
        api_key_header: string
            Name of API Key
        """
        self._api_key = api_key
        if api_key_header is not None:
            self._api_key_header = api_key_header

    def _add_required_headers(self, headers: dict):
        """
        Request authorization headers

        Parameters
        ----------
        headers: dict
            Headers dict to add auth headers to
        """
        headers["User-Agent"] = "liblab/0.1.25 PlexSDK/0.0.1 python/2.7"
        headers[f"{self._api_key_header}"] = f"{self._api_key}"
        return headers
