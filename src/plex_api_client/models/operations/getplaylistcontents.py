"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import date
from enum import Enum
import httpx
from plex_api_client import utils
from plex_api_client.types import BaseModel
from plex_api_client.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    validate_open_enum,
)
import pydantic
from pydantic.functional_validators import PlainValidator
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetPlaylistContentsQueryParamType(int, Enum, metaclass=utils.OpenEnumMeta):
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


class GetPlaylistContentsRequestTypedDict(TypedDict):
    playlist_id: float
    r"""the ID of the playlist"""
    type: GetPlaylistContentsQueryParamType
    r"""The type of media to retrieve or filter by.
    1 = movie
    2 = show
    3 = season
    4 = episode
    E.g. A movie library will not return anything with type 3 as there are no seasons for movie libraries

    """


class GetPlaylistContentsRequest(BaseModel):
    playlist_id: Annotated[
        float,
        pydantic.Field(alias="playlistID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""the ID of the playlist"""

    type: Annotated[
        Annotated[
            GetPlaylistContentsQueryParamType, PlainValidator(validate_open_enum(True))
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


class GetPlaylistContentsPartTypedDict(TypedDict):
    id: NotRequired[int]
    key: NotRequired[str]
    duration: NotRequired[int]
    file: NotRequired[str]
    size: NotRequired[int]
    audio_profile: NotRequired[str]
    container: NotRequired[str]
    has64bit_offsets: NotRequired[bool]
    optimized_for_streaming: NotRequired[bool]
    video_profile: NotRequired[str]


class GetPlaylistContentsPart(BaseModel):
    id: Optional[int] = None

    key: Optional[str] = None

    duration: Optional[int] = None

    file: Optional[str] = None

    size: Optional[int] = None

    audio_profile: Annotated[Optional[str], pydantic.Field(alias="audioProfile")] = None

    container: Optional[str] = None

    has64bit_offsets: Annotated[
        Optional[bool], pydantic.Field(alias="has64bitOffsets")
    ] = None

    optimized_for_streaming: Annotated[
        Optional[bool], pydantic.Field(alias="optimizedForStreaming")
    ] = None

    video_profile: Annotated[Optional[str], pydantic.Field(alias="videoProfile")] = None


class GetPlaylistContentsMediaTypedDict(TypedDict):
    id: NotRequired[int]
    duration: NotRequired[int]
    bitrate: NotRequired[int]
    width: NotRequired[int]
    height: NotRequired[int]
    aspect_ratio: NotRequired[float]
    audio_channels: NotRequired[int]
    audio_codec: NotRequired[str]
    video_codec: NotRequired[str]
    video_resolution: NotRequired[str]
    container: NotRequired[str]
    video_frame_rate: NotRequired[str]
    optimized_for_streaming: NotRequired[int]
    audio_profile: NotRequired[str]
    has64bit_offsets: NotRequired[bool]
    video_profile: NotRequired[str]
    part: NotRequired[List[GetPlaylistContentsPartTypedDict]]


class GetPlaylistContentsMedia(BaseModel):
    id: Optional[int] = None

    duration: Optional[int] = None

    bitrate: Optional[int] = None

    width: Optional[int] = None

    height: Optional[int] = None

    aspect_ratio: Annotated[Optional[float], pydantic.Field(alias="aspectRatio")] = None

    audio_channels: Annotated[Optional[int], pydantic.Field(alias="audioChannels")] = (
        None
    )

    audio_codec: Annotated[Optional[str], pydantic.Field(alias="audioCodec")] = None

    video_codec: Annotated[Optional[str], pydantic.Field(alias="videoCodec")] = None

    video_resolution: Annotated[
        Optional[str], pydantic.Field(alias="videoResolution")
    ] = None

    container: Optional[str] = None

    video_frame_rate: Annotated[
        Optional[str], pydantic.Field(alias="videoFrameRate")
    ] = None

    optimized_for_streaming: Annotated[
        Optional[int], pydantic.Field(alias="optimizedForStreaming")
    ] = None

    audio_profile: Annotated[Optional[str], pydantic.Field(alias="audioProfile")] = None

    has64bit_offsets: Annotated[
        Optional[bool], pydantic.Field(alias="has64bitOffsets")
    ] = None

    video_profile: Annotated[Optional[str], pydantic.Field(alias="videoProfile")] = None

    part: Annotated[
        Optional[List[GetPlaylistContentsPart]], pydantic.Field(alias="Part")
    ] = None


class GetPlaylistContentsGenreTypedDict(TypedDict):
    tag: NotRequired[str]


class GetPlaylistContentsGenre(BaseModel):
    tag: Optional[str] = None


class GetPlaylistContentsCountryTypedDict(TypedDict):
    tag: NotRequired[str]


class GetPlaylistContentsCountry(BaseModel):
    tag: Optional[str] = None


class GetPlaylistContentsDirectorTypedDict(TypedDict):
    tag: NotRequired[str]


class GetPlaylistContentsDirector(BaseModel):
    tag: Optional[str] = None


class GetPlaylistContentsWriterTypedDict(TypedDict):
    tag: NotRequired[str]


class GetPlaylistContentsWriter(BaseModel):
    tag: Optional[str] = None


class GetPlaylistContentsRoleTypedDict(TypedDict):
    tag: NotRequired[str]


class GetPlaylistContentsRole(BaseModel):
    tag: Optional[str] = None


class GetPlaylistContentsMetadataTypedDict(TypedDict):
    rating_key: NotRequired[str]
    key: NotRequired[str]
    guid: NotRequired[str]
    studio: NotRequired[str]
    type: NotRequired[str]
    title: NotRequired[str]
    title_sort: NotRequired[str]
    library_section_title: NotRequired[str]
    library_section_id: NotRequired[int]
    library_section_key: NotRequired[str]
    content_rating: NotRequired[str]
    summary: NotRequired[str]
    rating: NotRequired[float]
    audience_rating: NotRequired[float]
    year: NotRequired[int]
    tagline: NotRequired[str]
    thumb: NotRequired[str]
    art: NotRequired[str]
    duration: NotRequired[int]
    originally_available_at: NotRequired[date]
    added_at: NotRequired[int]
    updated_at: NotRequired[int]
    audience_rating_image: NotRequired[str]
    has_premium_extras: NotRequired[str]
    has_premium_primary_extra: NotRequired[str]
    rating_image: NotRequired[str]
    media: NotRequired[List[GetPlaylistContentsMediaTypedDict]]
    genre: NotRequired[List[GetPlaylistContentsGenreTypedDict]]
    country: NotRequired[List[GetPlaylistContentsCountryTypedDict]]
    director: NotRequired[List[GetPlaylistContentsDirectorTypedDict]]
    writer: NotRequired[List[GetPlaylistContentsWriterTypedDict]]
    role: NotRequired[List[GetPlaylistContentsRoleTypedDict]]


class GetPlaylistContentsMetadata(BaseModel):
    rating_key: Annotated[Optional[str], pydantic.Field(alias="ratingKey")] = None

    key: Optional[str] = None

    guid: Optional[str] = None

    studio: Optional[str] = None

    type: Optional[str] = None

    title: Optional[str] = None

    title_sort: Annotated[Optional[str], pydantic.Field(alias="titleSort")] = None

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

    rating: Optional[float] = None

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

    added_at: Annotated[Optional[int], pydantic.Field(alias="addedAt")] = None

    updated_at: Annotated[Optional[int], pydantic.Field(alias="updatedAt")] = None

    audience_rating_image: Annotated[
        Optional[str], pydantic.Field(alias="audienceRatingImage")
    ] = None

    has_premium_extras: Annotated[
        Optional[str], pydantic.Field(alias="hasPremiumExtras")
    ] = None

    has_premium_primary_extra: Annotated[
        Optional[str], pydantic.Field(alias="hasPremiumPrimaryExtra")
    ] = None

    rating_image: Annotated[Optional[str], pydantic.Field(alias="ratingImage")] = None

    media: Annotated[
        Optional[List[GetPlaylistContentsMedia]], pydantic.Field(alias="Media")
    ] = None

    genre: Annotated[
        Optional[List[GetPlaylistContentsGenre]], pydantic.Field(alias="Genre")
    ] = None

    country: Annotated[
        Optional[List[GetPlaylistContentsCountry]], pydantic.Field(alias="Country")
    ] = None

    director: Annotated[
        Optional[List[GetPlaylistContentsDirector]], pydantic.Field(alias="Director")
    ] = None

    writer: Annotated[
        Optional[List[GetPlaylistContentsWriter]], pydantic.Field(alias="Writer")
    ] = None

    role: Annotated[
        Optional[List[GetPlaylistContentsRole]], pydantic.Field(alias="Role")
    ] = None


class GetPlaylistContentsMediaContainerTypedDict(TypedDict):
    size: NotRequired[int]
    composite: NotRequired[str]
    duration: NotRequired[int]
    leaf_count: NotRequired[int]
    playlist_type: NotRequired[str]
    rating_key: NotRequired[str]
    smart: NotRequired[bool]
    title: NotRequired[str]
    metadata: NotRequired[List[GetPlaylistContentsMetadataTypedDict]]


class GetPlaylistContentsMediaContainer(BaseModel):
    size: Optional[int] = None

    composite: Optional[str] = None

    duration: Optional[int] = None

    leaf_count: Annotated[Optional[int], pydantic.Field(alias="leafCount")] = None

    playlist_type: Annotated[Optional[str], pydantic.Field(alias="playlistType")] = None

    rating_key: Annotated[Optional[str], pydantic.Field(alias="ratingKey")] = None

    smart: Optional[bool] = None

    title: Optional[str] = None

    metadata: Annotated[
        Optional[List[GetPlaylistContentsMetadata]], pydantic.Field(alias="Metadata")
    ] = None


class GetPlaylistContentsResponseBodyTypedDict(TypedDict):
    r"""The playlist contents"""

    media_container: NotRequired[GetPlaylistContentsMediaContainerTypedDict]


class GetPlaylistContentsResponseBody(BaseModel):
    r"""The playlist contents"""

    media_container: Annotated[
        Optional[GetPlaylistContentsMediaContainer],
        pydantic.Field(alias="MediaContainer"),
    ] = None


class GetPlaylistContentsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[GetPlaylistContentsResponseBodyTypedDict]
    r"""The playlist contents"""


class GetPlaylistContentsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[GetPlaylistContentsResponseBody] = None
    r"""The playlist contents"""
