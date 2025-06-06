"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import date
from enum import Enum
import httpx
from plex_api_client import utils
from plex_api_client.types import BaseModel
from plex_api_client.utils import FieldMetadata, QueryParamMetadata, validate_open_enum
import pydantic
from pydantic.functional_validators import PlainValidator
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetTopWatchedContentQueryParamType(int, Enum, metaclass=utils.OpenEnumMeta):
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
    ARTIST = 5
    ALBUM = 6
    TRACK = 7
    PHOTO_ALBUM = 8
    PHOTO = 9


class GetTopWatchedContentQueryParamIncludeGuids(int, Enum):
    r"""Adds the Guid object to the response"""

    DISABLE = 0
    ENABLE = 1


class GetTopWatchedContentRequestTypedDict(TypedDict):
    type: GetTopWatchedContentQueryParamType
    r"""The type of media to retrieve or filter by.
    1 = movie
    2 = show
    3 = season
    4 = episode
    E.g. A movie library will not return anything with type 3 as there are no seasons for movie libraries

    """
    include_guids: NotRequired[GetTopWatchedContentQueryParamIncludeGuids]
    r"""Adds the Guid object to the response

    """


class GetTopWatchedContentRequest(BaseModel):
    type: Annotated[
        Annotated[
            GetTopWatchedContentQueryParamType, PlainValidator(validate_open_enum(True))
        ],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""The type of media to retrieve or filter by.
    1 = movie
    2 = show
    3 = season
    4 = episode
    E.g. A movie library will not return anything with type 3 as there are no seasons for movie libraries

    """

    include_guids: Annotated[
        Optional[GetTopWatchedContentQueryParamIncludeGuids],
        pydantic.Field(alias="includeGuids"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = GetTopWatchedContentQueryParamIncludeGuids.DISABLE
    r"""Adds the Guid object to the response

    """


class GetTopWatchedContentGenreTypedDict(TypedDict):
    id: NotRequired[int]
    filter_: NotRequired[str]
    tag: NotRequired[str]


class GetTopWatchedContentGenre(BaseModel):
    id: Optional[int] = None

    filter_: Annotated[Optional[str], pydantic.Field(alias="filter")] = None

    tag: Optional[str] = None


class GetTopWatchedContentCountryTypedDict(TypedDict):
    id: NotRequired[int]
    filter_: NotRequired[str]
    tag: NotRequired[str]


class GetTopWatchedContentCountry(BaseModel):
    id: Optional[int] = None

    filter_: Annotated[Optional[str], pydantic.Field(alias="filter")] = None

    tag: Optional[str] = None


class GetTopWatchedContentGuidsTypedDict(TypedDict):
    id: NotRequired[str]


class GetTopWatchedContentGuids(BaseModel):
    id: Optional[str] = None


class GetTopWatchedContentRoleTypedDict(TypedDict):
    id: NotRequired[int]
    filter_: NotRequired[str]
    tag: NotRequired[str]
    tag_key: NotRequired[str]
    role: NotRequired[str]
    thumb: NotRequired[str]


class GetTopWatchedContentRole(BaseModel):
    id: Optional[int] = None

    filter_: Annotated[Optional[str], pydantic.Field(alias="filter")] = None

    tag: Optional[str] = None

    tag_key: Annotated[Optional[str], pydantic.Field(alias="tagKey")] = None

    role: Optional[str] = None

    thumb: Optional[str] = None


class GetTopWatchedContentUserTypedDict(TypedDict):
    id: NotRequired[int]


class GetTopWatchedContentUser(BaseModel):
    id: Optional[int] = None


class GetTopWatchedContentMetadataTypedDict(TypedDict):
    rating_key: NotRequired[str]
    key: NotRequired[str]
    guid: NotRequired[str]
    slug: NotRequired[str]
    studio: NotRequired[str]
    type: NotRequired[str]
    title: NotRequired[str]
    library_section_title: NotRequired[str]
    library_section_id: NotRequired[int]
    library_section_key: NotRequired[str]
    content_rating: NotRequired[str]
    summary: NotRequired[str]
    index: NotRequired[int]
    audience_rating: NotRequired[float]
    year: NotRequired[int]
    tagline: NotRequired[str]
    thumb: NotRequired[str]
    art: NotRequired[str]
    duration: NotRequired[int]
    originally_available_at: NotRequired[date]
    leaf_count: NotRequired[int]
    viewed_leaf_count: NotRequired[int]
    child_count: NotRequired[int]
    added_at: NotRequired[int]
    updated_at: NotRequired[int]
    global_view_count: NotRequired[int]
    audience_rating_image: NotRequired[str]
    genre: NotRequired[List[GetTopWatchedContentGenreTypedDict]]
    country: NotRequired[List[GetTopWatchedContentCountryTypedDict]]
    guids: NotRequired[List[GetTopWatchedContentGuidsTypedDict]]
    role: NotRequired[List[GetTopWatchedContentRoleTypedDict]]
    user: NotRequired[List[GetTopWatchedContentUserTypedDict]]


class GetTopWatchedContentMetadata(BaseModel):
    rating_key: Annotated[Optional[str], pydantic.Field(alias="ratingKey")] = None

    key: Optional[str] = None

    guid: Optional[str] = None

    slug: Optional[str] = None

    studio: Optional[str] = None

    type: Optional[str] = None

    title: Optional[str] = None

    library_section_title: Annotated[
        Optional[str], pydantic.Field(alias="librarySectionTitle")
    ] = None

    library_section_id: Annotated[
        Optional[int], pydantic.Field(alias="librarySectionID")
    ] = None

    library_section_key: Annotated[
        Optional[str], pydantic.Field(alias="librarySectionKey")
    ] = None

    content_rating: Annotated[Optional[str], pydantic.Field(alias="contentRating")] = (
        None
    )

    summary: Optional[str] = None

    index: Optional[int] = None

    audience_rating: Annotated[
        Optional[float], pydantic.Field(alias="audienceRating")
    ] = None

    year: Optional[int] = None

    tagline: Optional[str] = None

    thumb: Optional[str] = None

    art: Optional[str] = None

    duration: Optional[int] = None

    originally_available_at: Annotated[
        Optional[date], pydantic.Field(alias="originallyAvailableAt")
    ] = None

    leaf_count: Annotated[Optional[int], pydantic.Field(alias="leafCount")] = None

    viewed_leaf_count: Annotated[
        Optional[int], pydantic.Field(alias="viewedLeafCount")
    ] = None

    child_count: Annotated[Optional[int], pydantic.Field(alias="childCount")] = None

    added_at: Annotated[Optional[int], pydantic.Field(alias="addedAt")] = None

    updated_at: Annotated[Optional[int], pydantic.Field(alias="updatedAt")] = None

    global_view_count: Annotated[
        Optional[int], pydantic.Field(alias="globalViewCount")
    ] = None

    audience_rating_image: Annotated[
        Optional[str], pydantic.Field(alias="audienceRatingImage")
    ] = None

    genre: Annotated[
        Optional[List[GetTopWatchedContentGenre]], pydantic.Field(alias="Genre")
    ] = None

    country: Annotated[
        Optional[List[GetTopWatchedContentCountry]], pydantic.Field(alias="Country")
    ] = None

    guids: Annotated[
        Optional[List[GetTopWatchedContentGuids]], pydantic.Field(alias="Guid")
    ] = None

    role: Annotated[
        Optional[List[GetTopWatchedContentRole]], pydantic.Field(alias="Role")
    ] = None

    user: Annotated[
        Optional[List[GetTopWatchedContentUser]], pydantic.Field(alias="User")
    ] = None


class GetTopWatchedContentMediaContainerTypedDict(TypedDict):
    size: int
    r"""Number of media items returned in this response."""
    allow_sync: bool
    r"""Indicates whether syncing is allowed."""
    identifier: str
    r"""An plugin identifier for the media container."""
    media_tag_prefix: str
    r"""The prefix used for media tag resource paths."""
    media_tag_version: int
    r"""The version number for media tags."""
    metadata: NotRequired[List[GetTopWatchedContentMetadataTypedDict]]


class GetTopWatchedContentMediaContainer(BaseModel):
    size: int
    r"""Number of media items returned in this response."""

    allow_sync: Annotated[bool, pydantic.Field(alias="allowSync")]
    r"""Indicates whether syncing is allowed."""

    identifier: str
    r"""An plugin identifier for the media container."""

    media_tag_prefix: Annotated[str, pydantic.Field(alias="mediaTagPrefix")]
    r"""The prefix used for media tag resource paths."""

    media_tag_version: Annotated[int, pydantic.Field(alias="mediaTagVersion")]
    r"""The version number for media tags."""

    metadata: Annotated[
        Optional[List[GetTopWatchedContentMetadata]], pydantic.Field(alias="Metadata")
    ] = None


class GetTopWatchedContentResponseBodyTypedDict(TypedDict):
    r"""The metadata of the library item."""

    media_container: NotRequired[GetTopWatchedContentMediaContainerTypedDict]


class GetTopWatchedContentResponseBody(BaseModel):
    r"""The metadata of the library item."""

    media_container: Annotated[
        Optional[GetTopWatchedContentMediaContainer],
        pydantic.Field(alias="MediaContainer"),
    ] = None


class GetTopWatchedContentResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[GetTopWatchedContentResponseBodyTypedDict]
    r"""The metadata of the library item."""


class GetTopWatchedContentResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[GetTopWatchedContentResponseBody] = None
    r"""The metadata of the library item."""
