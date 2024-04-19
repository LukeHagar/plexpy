"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""


import requests as requests_http
from ._hooks import SDKHooks
from .utils import utils
from .utils.retries import RetryConfig
from dataclasses import dataclass, field
from enum import Enum
from plex_api.models import components, internal
from typing import Callable, Dict, List, Optional, Tuple, Union


SERVERS = [
    '{protocol}://{ip}:{port}',
    # The full address of your Plex Server
]
"""Contains the list of servers available to the SDK"""

class ServerProtocol(str, Enum):
    r"""The protocol to use when connecting to your plex server."""
    HTTP = 'http'
    HTTPS = 'https'


@dataclass
class SDKConfiguration:
    client: requests_http.Session
    globals: internal.Globals
    security: Union[components.Security,Callable[[], components.Security]] = None
    server_url: Optional[str] = ''
    server_idx: Optional[int] = 0
    server_defaults: List[Dict[str, str]] = field(default_factory=List)
    language: str = 'python'
    openapi_doc_version: str = '0.0.3'
    sdk_version: str = '0.6.4'
    gen_version: str = '2.311.1'
    user_agent: str = 'speakeasy-sdk/python 0.6.4 2.311.1 0.0.3 plex-api-client'
    retry_config: Optional[RetryConfig] = None

    def __post_init__(self):
        self._hooks = SDKHooks()

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url is not None and self.server_url != '':
            return utils.remove_suffix(self.server_url, '/'), {}
        if self.server_idx is None:
            self.server_idx = 0

        return SERVERS[self.server_idx], self.server_defaults[self.server_idx]


    def get_hooks(self) -> SDKHooks:
        return self._hooks
