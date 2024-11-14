"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from ._hooks import SDKHooks
from .httpclient import AsyncHttpClient, HttpClient
from .utils import Logger, RetryConfig, remove_suffix
from dataclasses import dataclass, field
from enum import Enum
from plex_api_client.models import components, internal
from plex_api_client.types import OptionalNullable, UNSET
from pydantic import Field
from typing import Callable, Dict, List, Optional, Tuple, Union


SERVERS = [
    "{protocol}://{ip}:{port}",
    # The full address of your Plex Server
]
"""Contains the list of servers available to the SDK"""


class ServerProtocol(str, Enum):
    r"""The protocol to use for the server connection"""

    HTTP = "http"
    HTTPS = "https"


@dataclass
class SDKConfiguration:
    client: HttpClient
    async_client: AsyncHttpClient
    debug_logger: Logger
    globals: internal.Globals
    security: Optional[
        Union[components.Security, Callable[[], components.Security]]
    ] = None
    server_url: Optional[str] = ""
    server_idx: Optional[int] = 0
    server_defaults: List[Dict[str, str]] = field(default_factory=List)
    language: str = "python"
    openapi_doc_version: str = "0.0.3"
    sdk_version: str = "0.19.1"
    gen_version: str = "2.457.9"
    user_agent: str = "speakeasy-sdk/python 0.19.1 2.457.9 0.0.3 plex-api-client"
    retry_config: OptionalNullable[RetryConfig] = Field(default_factory=lambda: UNSET)
    timeout_ms: Optional[int] = None

    def __post_init__(self):
        self._hooks = SDKHooks()

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url is not None and self.server_url:
            return remove_suffix(self.server_url, "/"), {}
        if self.server_idx is None:
            self.server_idx = 0

        return SERVERS[self.server_idx], self.server_defaults[self.server_idx]

    def get_hooks(self) -> SDKHooks:
        return self._hooks
