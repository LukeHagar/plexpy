"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
import httpx
from plex_api_client.types import BaseModel, Nullable, UNSET_SENTINEL
from plex_api_client.utils import FieldMetadata, HeaderMetadata, QueryParamMetadata
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


GET_SERVER_RESOURCES_SERVERS = [
    "https://plex.tv/api/v2",
]


class IncludeHTTPS(int, Enum):
    r"""Include Https entries in the results"""

    DISABLE = 0
    ENABLE = 1


class IncludeRelay(int, Enum):
    r"""Include Relay addresses in the results
    E.g: https://10-0-0-25.bbf8e10c7fa20447cacee74cd9914cde.plex.direct:32400

    """

    DISABLE = 0
    ENABLE = 1


class IncludeIPv6(int, Enum):
    r"""Include IPv6 entries in the results"""

    DISABLE = 0
    ENABLE = 1


class GetServerResourcesRequestTypedDict(TypedDict):
    client_id: str
    r"""An opaque identifier unique to the client (UUID, serial number, or other unique device ID)"""
    include_https: NotRequired[IncludeHTTPS]
    r"""Include Https entries in the results"""
    include_relay: NotRequired[IncludeRelay]
    r"""Include Relay addresses in the results
    E.g: https://10-0-0-25.bbf8e10c7fa20447cacee74cd9914cde.plex.direct:32400

    """
    include_i_pv6: NotRequired[IncludeIPv6]
    r"""Include IPv6 entries in the results"""


class GetServerResourcesRequest(BaseModel):
    client_id: Annotated[
        str,
        pydantic.Field(alias="X-Plex-Client-Identifier"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ]
    r"""An opaque identifier unique to the client (UUID, serial number, or other unique device ID)"""

    include_https: Annotated[
        Optional[IncludeHTTPS],
        pydantic.Field(alias="includeHttps"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = IncludeHTTPS.DISABLE
    r"""Include Https entries in the results"""

    include_relay: Annotated[
        Optional[IncludeRelay],
        pydantic.Field(alias="includeRelay"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = IncludeRelay.DISABLE
    r"""Include Relay addresses in the results
    E.g: https://10-0-0-25.bbf8e10c7fa20447cacee74cd9914cde.plex.direct:32400

    """

    include_i_pv6: Annotated[
        Optional[IncludeIPv6],
        pydantic.Field(alias="includeIPv6"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = IncludeIPv6.DISABLE
    r"""Include IPv6 entries in the results"""


class Protocol(str, Enum):
    r"""The protocol used for the connection (http, https, etc)"""

    HTTP = "http"
    HTTPS = "https"


class ConnectionsTypedDict(TypedDict):
    protocol: Protocol
    r"""The protocol used for the connection (http, https, etc)"""
    address: str
    r"""The (ip) address or domain name used for the connection"""
    port: int
    r"""The port used for the connection"""
    uri: str
    r"""The full URI of the connection"""
    local: bool
    r"""If the connection is local address"""
    relay: bool
    r"""If the connection is relayed through plex.direct"""
    i_pv6: bool
    r"""If the connection is using IPv6"""


class Connections(BaseModel):
    protocol: Protocol
    r"""The protocol used for the connection (http, https, etc)"""

    address: str
    r"""The (ip) address or domain name used for the connection"""

    port: int
    r"""The port used for the connection"""

    uri: str
    r"""The full URI of the connection"""

    local: bool
    r"""If the connection is local address"""

    relay: bool
    r"""If the connection is relayed through plex.direct"""

    i_pv6: Annotated[bool, pydantic.Field(alias="IPv6")]
    r"""If the connection is using IPv6"""


class PlexDeviceTypedDict(TypedDict):
    name: str
    product: str
    product_version: str
    platform: Nullable[str]
    platform_version: Nullable[str]
    device: Nullable[str]
    client_identifier: str
    created_at: datetime
    last_seen_at: datetime
    provides: str
    owner_id: Nullable[int]
    r"""ownerId is null when the device is owned by the token used to send the request"""
    source_title: Nullable[str]
    public_address: str
    access_token: str
    owned: bool
    home: bool
    synced: bool
    relay: bool
    presence: bool
    https_required: bool
    public_address_matches: bool
    dns_rebinding_protection: bool
    nat_loopback_supported: bool
    connections: List[ConnectionsTypedDict]


class PlexDevice(BaseModel):
    name: str

    product: str

    product_version: Annotated[str, pydantic.Field(alias="productVersion")]

    platform: Nullable[str]

    platform_version: Annotated[Nullable[str], pydantic.Field(alias="platformVersion")]

    device: Nullable[str]

    client_identifier: Annotated[str, pydantic.Field(alias="clientIdentifier")]

    created_at: Annotated[datetime, pydantic.Field(alias="createdAt")]

    last_seen_at: Annotated[datetime, pydantic.Field(alias="lastSeenAt")]

    provides: str

    owner_id: Annotated[Nullable[int], pydantic.Field(alias="ownerId")]
    r"""ownerId is null when the device is owned by the token used to send the request"""

    source_title: Annotated[Nullable[str], pydantic.Field(alias="sourceTitle")]

    public_address: Annotated[str, pydantic.Field(alias="publicAddress")]

    access_token: Annotated[str, pydantic.Field(alias="accessToken")]

    owned: bool

    home: bool

    synced: bool

    relay: bool

    presence: bool

    https_required: Annotated[bool, pydantic.Field(alias="httpsRequired")]

    public_address_matches: Annotated[
        bool, pydantic.Field(alias="publicAddressMatches")
    ]

    dns_rebinding_protection: Annotated[
        bool, pydantic.Field(alias="dnsRebindingProtection")
    ]

    nat_loopback_supported: Annotated[
        bool, pydantic.Field(alias="natLoopbackSupported")
    ]

    connections: List[Connections]

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = [
            "platform",
            "platformVersion",
            "device",
            "ownerId",
            "sourceTitle",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class GetServerResourcesResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    plex_devices: NotRequired[List[PlexDeviceTypedDict]]
    r"""List of Plex Devices. This includes Plex hosted servers and clients"""


class GetServerResourcesResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    plex_devices: Optional[List[PlexDevice]] = None
    r"""List of Plex Devices. This includes Plex hosted servers and clients"""
