"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import httpx
from plex_api_client.types import BaseModel
from plex_api_client.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetActorsLibraryQueryParamType(int, Enum):
    r"""The type of media to retrieve or filter by.
    1 = movie
    2 = show
    3 = season
    4 = episode
    E.g. A movie library will not return anything with type 3 as there are no seasons for movie libraries

    """

    MOVIE = 1
    TV_SHOW = 2
    SEASON = 3
    EPISODE = 4
    AUDIO = 8
    ALBUM = 9
    TRACK = 10


class GetActorsLibraryRequestTypedDict(TypedDict):
    section_key: int
    r"""The unique key of the Plex library.
    Note: This is unique in the context of the Plex server.

    """
    type: GetActorsLibraryQueryParamType
    r"""The type of media to retrieve or filter by.
    1 = movie
    2 = show
    3 = season
    4 = episode
    E.g. A movie library will not return anything with type 3 as there are no seasons for movie libraries

    """


class GetActorsLibraryRequest(BaseModel):
    section_key: Annotated[
        int,
        pydantic.Field(alias="sectionKey"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The unique key of the Plex library.
    Note: This is unique in the context of the Plex server.

    """

    type: Annotated[
        GetActorsLibraryQueryParamType,
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""The type of media to retrieve or filter by.
    1 = movie
    2 = show
    3 = season
    4 = episode
    E.g. A movie library will not return anything with type 3 as there are no seasons for movie libraries

    """


class GetActorsLibraryDirectoryTypedDict(TypedDict):
    fast_key: str
    r"""A fast lookup key for the actor relative url."""
    thumb: str
    r"""URL for the thumbnail image of the actor."""
    key: str
    r"""A unique key representing the actor."""
    title: str
    r"""The name of the actor."""


class GetActorsLibraryDirectory(BaseModel):
    fast_key: Annotated[str, pydantic.Field(alias="fastKey")]
    r"""A fast lookup key for the actor relative url."""

    thumb: str
    r"""URL for the thumbnail image of the actor."""

    key: str
    r"""A unique key representing the actor."""

    title: str
    r"""The name of the actor."""


class GetActorsLibraryMediaContainerTypedDict(TypedDict):
    size: float
    allow_sync: bool
    r"""Indicates whether syncing is allowed."""
    art: str
    r"""URL for the background artwork of the media container."""
    identifier: str
    r"""An plugin identifier for the media container."""
    media_tag_prefix: str
    r"""The prefix used for media tag resource paths."""
    media_tag_version: int
    r"""The version number for media tags."""
    nocache: bool
    r"""Specifies whether caching is disabled."""
    thumb: str
    r"""URL for the thumbnail image of the media container."""
    title1: str
    r"""The primary title of the media container."""
    title2: str
    r"""The secondary title of the media container."""
    view_group: str
    r"""Identifier for the view group layout."""
    view_mode: str
    r"""Identifier for the view mode."""
    directory: NotRequired[List[GetActorsLibraryDirectoryTypedDict]]
    r"""An array of actor entries for media items."""


class GetActorsLibraryMediaContainer(BaseModel):
    size: float

    allow_sync: Annotated[bool, pydantic.Field(alias="allowSync")]
    r"""Indicates whether syncing is allowed."""

    art: str
    r"""URL for the background artwork of the media container."""

    identifier: str
    r"""An plugin identifier for the media container."""

    media_tag_prefix: Annotated[str, pydantic.Field(alias="mediaTagPrefix")]
    r"""The prefix used for media tag resource paths."""

    media_tag_version: Annotated[int, pydantic.Field(alias="mediaTagVersion")]
    r"""The version number for media tags."""

    nocache: bool
    r"""Specifies whether caching is disabled."""

    thumb: str
    r"""URL for the thumbnail image of the media container."""

    title1: str
    r"""The primary title of the media container."""

    title2: str
    r"""The secondary title of the media container."""

    view_group: Annotated[str, pydantic.Field(alias="viewGroup")]
    r"""Identifier for the view group layout."""

    view_mode: Annotated[str, pydantic.Field(alias="viewMode")]
    r"""Identifier for the view mode."""

    directory: Annotated[
        Optional[List[GetActorsLibraryDirectory]], pydantic.Field(alias="Directory")
    ] = None
    r"""An array of actor entries for media items."""


class GetActorsLibraryResponseBodyTypedDict(TypedDict):
    r"""Successful response containing media container data."""

    media_container: NotRequired[GetActorsLibraryMediaContainerTypedDict]


class GetActorsLibraryResponseBody(BaseModel):
    r"""Successful response containing media container data."""

    media_container: Annotated[
        Optional[GetActorsLibraryMediaContainer], pydantic.Field(alias="MediaContainer")
    ] = None


class GetActorsLibraryResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[GetActorsLibraryResponseBodyTypedDict]
    r"""Successful response containing media container data."""


class GetActorsLibraryResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[GetActorsLibraryResponseBody] = None
    r"""Successful response containing media container data."""
