"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import httpx
from plex_api_client.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from plex_api_client.utils import FieldMetadata, HeaderMetadata
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


GET_USERS_SERVERS = [
    "https://plex.tv/api",
]


class GetUsersRequestTypedDict(TypedDict):
    client_id: str
    r"""An opaque identifier unique to the client (UUID, serial number, or other unique device ID)"""
    x_plex_token: str
    r"""An authentication token, obtained from plex.tv"""
    client_name: NotRequired[str]
    r"""The name of the client application. (Plex Web, Plex Media Server, etc.)"""
    device_nickname: NotRequired[str]
    r"""A relatively friendly name for the client device"""
    device_name: NotRequired[str]
    r"""The name of the device the client application is running on. This is used to track the client application and its usage. (Chrome, Safari, etc.)"""
    device_screen_resolution: NotRequired[str]
    r"""The resolution of the device the client application is running on. This is used to track the client application and its usage. (1487x1165,2560x1440)"""
    client_version: NotRequired[str]
    r"""The version of the client application."""
    platform: NotRequired[str]
    r"""The platform of the client application."""
    client_features: NotRequired[str]
    r"""The features of the client application. This is used to track the client application and its usage. (external-media,indirect-media,hub-style-list)"""
    model: NotRequired[str]
    r"""A potentially less friendly identifier for the device model"""
    x_plex_session_id: NotRequired[str]
    r"""The session ID of the client application. This is used to track the client application and its usage. (97e136ef-4ddd-4ff3-89a7-a5820c96c2ca)"""
    x_plex_language: NotRequired[str]
    r"""The language of the client application."""
    platform_version: NotRequired[str]
    r"""The version of the platform"""


class GetUsersRequest(BaseModel):
    client_id: Annotated[
        str,
        pydantic.Field(alias="X-Plex-Client-Identifier"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ]
    r"""An opaque identifier unique to the client (UUID, serial number, or other unique device ID)"""

    x_plex_token: Annotated[
        str,
        pydantic.Field(alias="X-Plex-Token"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ]
    r"""An authentication token, obtained from plex.tv"""

    client_name: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Plex-Product"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The name of the client application. (Plex Web, Plex Media Server, etc.)"""

    device_nickname: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Plex-Device"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""A relatively friendly name for the client device"""

    device_name: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Plex-Device-Name"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The name of the device the client application is running on. This is used to track the client application and its usage. (Chrome, Safari, etc.)"""

    device_screen_resolution: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Plex-Device-Screen-Resolution"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The resolution of the device the client application is running on. This is used to track the client application and its usage. (1487x1165,2560x1440)"""

    client_version: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Plex-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The version of the client application."""

    platform: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Plex-Platform"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The platform of the client application."""

    client_features: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Plex-Features"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The features of the client application. This is used to track the client application and its usage. (external-media,indirect-media,hub-style-list)"""

    model: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Plex-Model"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""A potentially less friendly identifier for the device model"""

    x_plex_session_id: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Plex-Session-Id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The session ID of the client application. This is used to track the client application and its usage. (97e136ef-4ddd-4ff3-89a7-a5820c96c2ca)"""

    x_plex_language: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Plex-Language"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The language of the client application."""

    platform_version: Annotated[
        Optional[str],
        pydantic.Field(alias="X-Plex-Platform-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The version of the platform"""


class Protected(int, Enum):
    r"""Indicates whether the account is protected."""

    DISABLE = 0
    ENABLE = 1


class Home(int, Enum):
    r"""Indicates if the user is part of a home group."""

    DISABLE = 0
    ENABLE = 1


class AllowTuners(int, Enum):
    r"""Indicates if the user is allowed to use tuners."""

    DISABLE = 0
    ENABLE = 1


class AllowSync(int, Enum):
    r"""Indicates if the user is allowed to sync media."""

    DISABLE = 0
    ENABLE = 1


class AllowCameraUpload(int, Enum):
    r"""Indicates if the user is allowed to upload from a camera."""

    DISABLE = 0
    ENABLE = 1


class AllowChannels(int, Enum):
    r"""Indicates if the user has access to channels."""

    DISABLE = 0
    ENABLE = 1


class AllowSubtitleAdmin(int, Enum):
    r"""Indicates if the user can manage subtitles."""

    DISABLE = 0
    ENABLE = 1


class Restricted(int, Enum):
    r"""Indicates if the user has restricted access."""

    DISABLE = 0
    ENABLE = 1


class AllLibraries(int, Enum):
    r"""Indicates if the user has access to all libraries."""

    DISABLE = 0
    ENABLE = 1


class Owned(int, Enum):
    r"""Indicates if the user owns the server."""

    DISABLE = 0
    ENABLE = 1


class Pending(int, Enum):
    r"""Indicates if the server is pending approval."""

    DISABLE = 0
    ENABLE = 1


class GetUsersServerTypedDict(TypedDict):
    id: int
    r"""Unique ID of the server of the connected user"""
    server_id: int
    r"""ID of the actual Plex server."""
    machine_identifier: str
    r"""Machine identifier of the Plex server."""
    name: str
    r"""Name of the Plex server of the connected user."""
    last_seen_at: int
    num_libraries: int
    r"""Number of libraries in the server this user has access to."""
    all_libraries: NotRequired[AllLibraries]
    owned: NotRequired[Owned]
    pending: NotRequired[Pending]


class GetUsersServer(BaseModel):
    id: int
    r"""Unique ID of the server of the connected user"""

    server_id: int
    r"""ID of the actual Plex server."""

    machine_identifier: str
    r"""Machine identifier of the Plex server."""

    name: str
    r"""Name of the Plex server of the connected user."""

    last_seen_at: int

    num_libraries: int
    r"""Number of libraries in the server this user has access to."""

    all_libraries: Optional[AllLibraries] = AllLibraries.DISABLE

    owned: Optional[Owned] = Owned.DISABLE

    pending: Optional[Pending] = Pending.DISABLE


class UserTypedDict(TypedDict):
    id: int
    r"""User's unique ID."""
    title: str
    r"""User's display name."""
    username: str
    r"""User's username."""
    email: str
    r"""User's email address."""
    thumb: str
    r"""URL to the user's avatar image."""
    server: List[GetUsersServerTypedDict]
    r"""List of servers owned by the user."""
    recommendations_playlist_id: NotRequired[Nullable[str]]
    r"""ID of the user's recommendation playlist."""
    protected: NotRequired[Protected]
    home: NotRequired[Home]
    allow_tuners: NotRequired[AllowTuners]
    allow_sync: NotRequired[AllowSync]
    allow_camera_upload: NotRequired[AllowCameraUpload]
    allow_channels: NotRequired[AllowChannels]
    allow_subtitle_admin: NotRequired[AllowSubtitleAdmin]
    filter_all: NotRequired[Nullable[str]]
    r"""Filters applied for all content."""
    filter_movies: NotRequired[Nullable[str]]
    r"""Filters applied for movies."""
    filter_music: NotRequired[Nullable[str]]
    r"""Filters applied for music."""
    filter_photos: NotRequired[Nullable[str]]
    r"""Filters applied for photos."""
    filter_television: NotRequired[str]
    r"""Filters applied for television."""
    restricted: NotRequired[Restricted]


class User(BaseModel):
    id: int
    r"""User's unique ID."""

    title: str
    r"""User's display name."""

    username: str
    r"""User's username."""

    email: str
    r"""User's email address."""

    thumb: str
    r"""URL to the user's avatar image."""

    server: List[GetUsersServer]
    r"""List of servers owned by the user."""

    recommendations_playlist_id: OptionalNullable[str] = UNSET
    r"""ID of the user's recommendation playlist."""

    protected: Optional[Protected] = Protected.DISABLE

    home: Optional[Home] = Home.DISABLE

    allow_tuners: Optional[AllowTuners] = AllowTuners.DISABLE

    allow_sync: Optional[AllowSync] = AllowSync.DISABLE

    allow_camera_upload: Optional[AllowCameraUpload] = AllowCameraUpload.DISABLE

    allow_channels: Optional[AllowChannels] = AllowChannels.DISABLE

    allow_subtitle_admin: Optional[AllowSubtitleAdmin] = AllowSubtitleAdmin.DISABLE

    filter_all: OptionalNullable[str] = UNSET
    r"""Filters applied for all content."""

    filter_movies: OptionalNullable[str] = UNSET
    r"""Filters applied for movies."""

    filter_music: OptionalNullable[str] = UNSET
    r"""Filters applied for music."""

    filter_photos: OptionalNullable[str] = UNSET
    r"""Filters applied for photos."""

    filter_television: Optional[str] = None
    r"""Filters applied for television."""

    restricted: Optional[Restricted] = Restricted.DISABLE

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "recommendationsPlaylistId",
            "protected",
            "home",
            "allowTuners",
            "allowSync",
            "allowCameraUpload",
            "allowChannels",
            "allowSubtitleAdmin",
            "filterAll",
            "filterMovies",
            "filterMusic",
            "filterPhotos",
            "filterTelevision",
            "restricted",
        ]
        nullable_fields = [
            "recommendationsPlaylistId",
            "filterAll",
            "filterMovies",
            "filterMusic",
            "filterPhotos",
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


class GetUsersMediaContainerTypedDict(TypedDict):
    r"""Container holding user and server details."""

    friendly_name: str
    r"""The friendly name of the Plex instance."""
    identifier: str
    machine_identifier: str
    r"""Unique Machine identifier of the Plex server."""
    total_size: int
    r"""Total number of users."""
    size: int
    r"""Number of users in the current response."""
    user: List[UserTypedDict]
    r"""List of users with access to the Plex server."""


class GetUsersMediaContainer(BaseModel):
    r"""Container holding user and server details."""

    friendly_name: str
    r"""The friendly name of the Plex instance."""

    identifier: str

    machine_identifier: str
    r"""Unique Machine identifier of the Plex server."""

    total_size: int
    r"""Total number of users."""

    size: int
    r"""Number of users in the current response."""

    user: List[User]
    r"""List of users with access to the Plex server."""


class GetUsersResponseBodyTypedDict(TypedDict):
    r"""Successful response with media container data in XML"""

    media_container: NotRequired[GetUsersMediaContainerTypedDict]
    r"""Container holding user and server details."""


class GetUsersResponseBody(BaseModel):
    r"""Successful response with media container data in XML"""

    media_container: Optional[GetUsersMediaContainer] = None
    r"""Container holding user and server details."""


class GetUsersResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    body: NotRequired[bytes]


class GetUsersResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    body: Optional[bytes] = None
