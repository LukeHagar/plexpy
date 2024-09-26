"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import httpx
from plex_api_client.types import BaseModel
from plex_api_client.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class PlaylistType(str, Enum):
    r"""limit to a type of playlist."""

    AUDIO = "audio"
    VIDEO = "video"
    PHOTO = "photo"


class QueryParamSmart(int, Enum):
    r"""type of playlists to return (default is all)."""

    ZERO = 0
    ONE = 1


class GetPlaylistsRequestTypedDict(TypedDict):
    playlist_type: NotRequired[PlaylistType]
    r"""limit to a type of playlist."""
    smart: NotRequired[QueryParamSmart]
    r"""type of playlists to return (default is all)."""


class GetPlaylistsRequest(BaseModel):
    playlist_type: Annotated[
        Optional[PlaylistType],
        pydantic.Field(alias="playlistType"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""limit to a type of playlist."""

    smart: Annotated[
        Optional[QueryParamSmart],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""type of playlists to return (default is all)."""


class GetPlaylistsMetadataTypedDict(TypedDict):
    rating_key: NotRequired[str]
    key: NotRequired[str]
    guid: NotRequired[str]
    type: NotRequired[str]
    title: NotRequired[str]
    summary: NotRequired[str]
    smart: NotRequired[bool]
    playlist_type: NotRequired[str]
    composite: NotRequired[str]
    icon: NotRequired[str]
    view_count: NotRequired[int]
    last_viewed_at: NotRequired[int]
    duration: NotRequired[int]
    leaf_count: NotRequired[int]
    added_at: NotRequired[int]
    updated_at: NotRequired[int]


class GetPlaylistsMetadata(BaseModel):
    rating_key: Annotated[Optional[str], pydantic.Field(alias="ratingKey")] = None

    key: Optional[str] = None

    guid: Optional[str] = None

    type: Optional[str] = None

    title: Optional[str] = None

    summary: Optional[str] = None

    smart: Optional[bool] = None

    playlist_type: Annotated[Optional[str], pydantic.Field(alias="playlistType")] = None

    composite: Optional[str] = None

    icon: Optional[str] = None

    view_count: Annotated[Optional[int], pydantic.Field(alias="viewCount")] = None

    last_viewed_at: Annotated[Optional[int], pydantic.Field(alias="lastViewedAt")] = (
        None
    )

    duration: Optional[int] = None

    leaf_count: Annotated[Optional[int], pydantic.Field(alias="leafCount")] = None

    added_at: Annotated[Optional[int], pydantic.Field(alias="addedAt")] = None

    updated_at: Annotated[Optional[int], pydantic.Field(alias="updatedAt")] = None


class GetPlaylistsMediaContainerTypedDict(TypedDict):
    size: NotRequired[int]
    metadata: NotRequired[List[GetPlaylistsMetadataTypedDict]]


class GetPlaylistsMediaContainer(BaseModel):
    size: Optional[int] = None

    metadata: Annotated[
        Optional[List[GetPlaylistsMetadata]], pydantic.Field(alias="Metadata")
    ] = None


class GetPlaylistsResponseBodyTypedDict(TypedDict):
    r"""returns all playlists"""

    media_container: NotRequired[GetPlaylistsMediaContainerTypedDict]


class GetPlaylistsResponseBody(BaseModel):
    r"""returns all playlists"""

    media_container: Annotated[
        Optional[GetPlaylistsMediaContainer], pydantic.Field(alias="MediaContainer")
    ] = None


class GetPlaylistsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[GetPlaylistsResponseBodyTypedDict]
    r"""returns all playlists"""


class GetPlaylistsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[GetPlaylistsResponseBody] = None
    r"""returns all playlists"""