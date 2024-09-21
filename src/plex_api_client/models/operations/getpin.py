"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
import httpx
from plex_api_client.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from plex_api_client.utils import FieldMetadata, QueryParamMetadata
import pydantic
from pydantic import model_serializer
from typing import Any, Optional, TypedDict
from typing_extensions import Annotated, NotRequired

GET_PIN_SERVERS = [
    "https://plex.tv/api/v2/",
]


class GetPinGlobalsTypedDict(TypedDict):
    client_name: NotRequired[str]
    device_name: NotRequired[str]
    client_version: NotRequired[str]
    client_platform: NotRequired[str]


class GetPinGlobals(BaseModel):
    client_name: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Plex-Product"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    device_name: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Plex-Device"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    client_version: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Plex-Version"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    client_platform: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Plex-Platform"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None


class GetPinRequestTypedDict(TypedDict):
    strong: NotRequired[bool]
    r"""Determines the kind of code returned by the API call
    Strong codes are used for Pin authentication flows
    Non-Strong codes are used for `Plex.tv/link`

    """
    client_name: NotRequired[str]
    device_name: NotRequired[str]
    client_version: NotRequired[str]
    client_platform: NotRequired[str]


class GetPinRequest(BaseModel):
    strong: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = False
    r"""Determines the kind of code returned by the API call
    Strong codes are used for Pin authentication flows
    Non-Strong codes are used for `Plex.tv/link`

    """

    client_name: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Plex-Product"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    device_name: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Plex-Device"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    client_version: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Plex-Version"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    client_platform: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Plex-Platform"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None


class GeoDataTypedDict(TypedDict):
    r"""Geo location data"""

    code: str
    r"""The ISO 3166-1 alpha-2 code of the country."""
    continent_code: str
    r"""The continent code where the country is located."""
    country: str
    r"""The official name of the country."""
    city: str
    r"""The name of the city."""
    time_zone: str
    r"""The time zone of the country."""
    postal_code: str
    r"""The postal code of the location."""
    subdivisions: str
    r"""The name of the primary administrative subdivision."""
    coordinates: str
    r"""The geographical coordinates (latitude, longitude) of the location."""
    european_union_member: NotRequired[bool]
    r"""Indicates if the country is a member of the European Union."""
    in_privacy_restricted_country: NotRequired[bool]
    r"""Indicates if the country has privacy restrictions."""
    in_privacy_restricted_region: NotRequired[bool]
    r"""Indicates if the region has privacy restrictions."""


class GeoData(BaseModel):
    r"""Geo location data"""

    code: str
    r"""The ISO 3166-1 alpha-2 code of the country."""

    continent_code: str
    r"""The continent code where the country is located."""

    country: str
    r"""The official name of the country."""

    city: str
    r"""The name of the city."""

    time_zone: str
    r"""The time zone of the country."""

    postal_code: str
    r"""The postal code of the location."""

    subdivisions: str
    r"""The name of the primary administrative subdivision."""

    coordinates: str
    r"""The geographical coordinates (latitude, longitude) of the location."""

    european_union_member: Optional[bool] = False
    r"""Indicates if the country is a member of the European Union."""

    in_privacy_restricted_country: Optional[bool] = False
    r"""Indicates if the country has privacy restrictions."""

    in_privacy_restricted_region: Optional[bool] = False
    r"""Indicates if the region has privacy restrictions."""


class GetPinAuthPinContainerTypedDict(TypedDict):
    r"""Requests a new pin id used in the authentication flow"""

    id: int
    code: str
    product: str
    qr: str
    client_identifier: str
    r"""The X-Client-Identifier used in the request"""
    location: GeoDataTypedDict
    r"""Geo location data"""
    created_at: datetime
    expires_at: datetime
    trusted: NotRequired[bool]
    expires_in: NotRequired[int]
    r"""The number of seconds this pin expires, by default 900 seconds"""
    auth_token: NotRequired[Nullable[str]]
    new_registration: NotRequired[Nullable[Any]]


class GetPinAuthPinContainer(BaseModel):
    r"""Requests a new pin id used in the authentication flow"""

    id: int

    code: str

    product: str

    qr: str

    client_identifier: Annotated[str, pydantic.Field(alias="clientIdentifier")]
    r"""The X-Client-Identifier used in the request"""

    location: GeoData
    r"""Geo location data"""

    created_at: Annotated[datetime, pydantic.Field(alias="createdAt")]

    expires_at: Annotated[datetime, pydantic.Field(alias="expiresAt")]

    trusted: Optional[bool] = False

    expires_in: Annotated[Optional[int], pydantic.Field(alias="expiresIn")] = 900
    r"""The number of seconds this pin expires, by default 900 seconds"""

    auth_token: Annotated[OptionalNullable[str], pydantic.Field(alias="authToken")] = (
        UNSET
    )

    new_registration: Annotated[
        OptionalNullable[Any], pydantic.Field(alias="newRegistration")
    ] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["trusted", "expiresIn", "authToken", "newRegistration"]
        nullable_fields = ["authToken", "newRegistration"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
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


class GetPinResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    auth_pin_container: NotRequired[GetPinAuthPinContainerTypedDict]
    r"""Requests a new pin id used in the authentication flow"""


class GetPinResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    auth_pin_container: Optional[GetPinAuthPinContainer] = None
    r"""Requests a new pin id used in the authentication flow"""
