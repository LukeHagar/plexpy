"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import date
from enum import Enum
import httpx
from plex_api_client.types import BaseModel
from plex_api_client.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class Type(int, Enum):
    r"""The type of media to retrieve.
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


class IncludeMeta(int, Enum):
    r"""Adds the Meta object to the response"""

    DISABLE = 0
    ENABLE = 1


class GetRecentlyAddedRequestTypedDict(TypedDict):
    content_directory_id: int
    r"""The content directory ID."""
    type: Type
    r"""The type of media to retrieve.
    1 = movie
    2 = show
    3 = season
    4 = episode
    E.g. A movie library will not return anything with type 3 as there are no seasons for movie libraries

    """
    pinned_content_directory_id: NotRequired[str]
    r"""Comma-separated list of pinned content directory IDs."""
    section_id: NotRequired[int]
    r"""The library section ID for filtering content."""
    include_meta: NotRequired[IncludeMeta]
    r"""Adds the Meta object to the response

    """
    x_plex_container_start: NotRequired[int]
    r"""The index of the first item to return. If not specified, the first item will be returned.
    If the number of items exceeds the limit, the response will be paginated.
    By default this is 0

    """
    x_plex_container_size: NotRequired[int]
    r"""The number of items to return. If not specified, all items will be returned.
    If the number of items exceeds the limit, the response will be paginated.
    By default this is 50

    """


class GetRecentlyAddedRequest(BaseModel):
    content_directory_id: Annotated[
        int,
        pydantic.Field(alias="contentDirectoryID"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""The content directory ID."""

    type: Annotated[
        Type, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""The type of media to retrieve.
    1 = movie
    2 = show
    3 = season
    4 = episode
    E.g. A movie library will not return anything with type 3 as there are no seasons for movie libraries

    """

    pinned_content_directory_id: Annotated[
        Optional[str],
        pydantic.Field(alias="pinnedContentDirectoryID"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Comma-separated list of pinned content directory IDs."""

    section_id: Annotated[
        Optional[int],
        pydantic.Field(alias="sectionID"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The library section ID for filtering content."""

    include_meta: Annotated[
        Optional[IncludeMeta],
        pydantic.Field(alias="includeMeta"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = IncludeMeta.DISABLE
    r"""Adds the Meta object to the response

    """

    x_plex_container_start: Annotated[
        Optional[int],
        pydantic.Field(alias="X-Plex-Container-Start"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 0
    r"""The index of the first item to return. If not specified, the first item will be returned.
    If the number of items exceeds the limit, the response will be paginated.
    By default this is 0

    """

    x_plex_container_size: Annotated[
        Optional[int],
        pydantic.Field(alias="X-Plex-Container-Size"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 50
    r"""The number of items to return. If not specified, all items will be returned.
    If the number of items exceeds the limit, the response will be paginated.
    By default this is 50

    """


class GetRecentlyAddedFilterTypedDict(TypedDict):
    filter_: str
    filter_type: str
    key: str
    title: str
    type: str


class GetRecentlyAddedFilter(BaseModel):
    filter_: Annotated[str, pydantic.Field(alias="filter")]

    filter_type: Annotated[str, pydantic.Field(alias="filterType")]

    key: str

    title: str

    type: str


class GetRecentlyAddedActiveDirection(str, Enum):
    r"""The direction of the sort. Can be either `asc` or `desc`."""

    ASCENDING = "asc"
    DESCENDING = "desc"


class GetRecentlyAddedDefaultDirection(str, Enum):
    r"""The direction of the sort. Can be either `asc` or `desc`."""

    ASCENDING = "asc"
    DESCENDING = "desc"


class GetRecentlyAddedSortTypedDict(TypedDict):
    key: str
    title: str
    default: NotRequired[str]
    active: NotRequired[bool]
    active_direction: NotRequired[GetRecentlyAddedActiveDirection]
    r"""The direction of the sort. Can be either `asc` or `desc`.

    """
    default_direction: NotRequired[GetRecentlyAddedDefaultDirection]
    r"""The direction of the sort. Can be either `asc` or `desc`.

    """
    desc_key: NotRequired[str]
    first_character_key: NotRequired[str]


class GetRecentlyAddedSort(BaseModel):
    key: str

    title: str

    default: Optional[str] = None

    active: Optional[bool] = None

    active_direction: Annotated[
        Optional[GetRecentlyAddedActiveDirection],
        pydantic.Field(alias="activeDirection"),
    ] = GetRecentlyAddedActiveDirection.ASCENDING
    r"""The direction of the sort. Can be either `asc` or `desc`.

    """

    default_direction: Annotated[
        Optional[GetRecentlyAddedDefaultDirection],
        pydantic.Field(alias="defaultDirection"),
    ] = GetRecentlyAddedDefaultDirection.ASCENDING
    r"""The direction of the sort. Can be either `asc` or `desc`.

    """

    desc_key: Annotated[Optional[str], pydantic.Field(alias="descKey")] = None

    first_character_key: Annotated[
        Optional[str], pydantic.Field(alias="firstCharacterKey")
    ] = None


class GetRecentlyAddedFieldTypedDict(TypedDict):
    key: str
    title: str
    type: str
    sub_type: NotRequired[str]


class GetRecentlyAddedField(BaseModel):
    key: str

    title: str

    type: str

    sub_type: Annotated[Optional[str], pydantic.Field(alias="subType")] = None


class GetRecentlyAddedTypeTypedDict(TypedDict):
    key: str
    type: str
    title: str
    active: bool
    filter_: NotRequired[List[GetRecentlyAddedFilterTypedDict]]
    sort: NotRequired[List[GetRecentlyAddedSortTypedDict]]
    field: NotRequired[List[GetRecentlyAddedFieldTypedDict]]


class GetRecentlyAddedType(BaseModel):
    key: str

    type: str

    title: str

    active: bool

    filter_: Annotated[
        Optional[List[GetRecentlyAddedFilter]], pydantic.Field(alias="Filter")
    ] = None

    sort: Annotated[
        Optional[List[GetRecentlyAddedSort]], pydantic.Field(alias="Sort")
    ] = None

    field: Annotated[
        Optional[List[GetRecentlyAddedField]], pydantic.Field(alias="Field")
    ] = None


class GetRecentlyAddedOperatorTypedDict(TypedDict):
    key: str
    title: str


class GetRecentlyAddedOperator(BaseModel):
    key: str

    title: str


class GetRecentlyAddedFieldTypeTypedDict(TypedDict):
    type: str
    operator: List[GetRecentlyAddedOperatorTypedDict]


class GetRecentlyAddedFieldType(BaseModel):
    type: str

    operator: Annotated[
        List[GetRecentlyAddedOperator], pydantic.Field(alias="Operator")
    ]


class MetaTypedDict(TypedDict):
    r"""The Meta object is only included in the response if the `includeMeta` parameter is set to `1`."""

    type: NotRequired[List[GetRecentlyAddedTypeTypedDict]]
    field_type: NotRequired[List[GetRecentlyAddedFieldTypeTypedDict]]


class Meta(BaseModel):
    r"""The Meta object is only included in the response if the `includeMeta` parameter is set to `1`."""

    type: Annotated[
        Optional[List[GetRecentlyAddedType]], pydantic.Field(alias="Type")
    ] = None

    field_type: Annotated[
        Optional[List[GetRecentlyAddedFieldType]], pydantic.Field(alias="FieldType")
    ] = None


class GetRecentlyAddedHubsType(str, Enum):
    r"""The type of media content"""

    MOVIE = "movie"
    TV_SHOW = "show"
    SEASON = "season"
    EPISODE = "episode"


class FlattenSeasons(str, Enum):
    r"""Setting that indicates if seasons are set to hidden for the show. (-1 = Library default, 0 = Hide, 1 = Show)."""

    LIBRARY_DEFAULT = "-1"
    HIDE = "0"
    SHOW = "1"


class EpisodeSort(str, Enum):
    r"""Setting that indicates how episodes are sorted for the show. (-1 = Library default, 0 = Oldest first, 1 = Newest first)."""

    LIBRARY_DEFAULT = "-1"
    OLDEST_FIRST = "0"
    NEWEST_FIRST = "1"


class EnableCreditsMarkerGeneration(str, Enum):
    r"""Setting that indicates if credits markers detection is enabled. (-1 = Library default, 0 = Disabled)."""

    LIBRARY_DEFAULT = "-1"
    DISABLED = "0"


class ShowOrdering(str, Enum):
    r"""Setting that indicates the episode ordering for the show
    None = Library default,
    tmdbAiring = The Movie Database (Aired),
    tvdbAiring = TheTVDB (Aired),
    tvdbDvd = TheTVDB (DVD),
    tvdbAbsolute = TheTVDB (Absolute)).

    """

    NONE = "None"
    TMDB_AIRING = "tmdbAiring"
    TVDB_AIRING = "tvdbAiring"
    TVDB_DVD = "tvdbDvd"
    TVDB_ABSOLUTE = "tvdbAbsolute"


class OptimizedForStreaming(int, Enum):
    DISABLE = 0
    ENABLE = 1


class HasThumbnail(str, Enum):
    FALSE = "0"
    TRUE = "1"


class StreamTypedDict(TypedDict):
    id: int
    stream_type: int
    r"""Type of stream (1 = video, 2 = audio, 3 = subtitle)"""
    codec: str
    r"""Codec used by the stream"""
    index: int
    r"""The index of the stream"""
    default: NotRequired[bool]
    r"""Indicates if this is the default stream"""
    selected: NotRequired[bool]
    r"""Indicates if the stream is selected"""
    bitrate: NotRequired[int]
    r"""The bitrate of the stream in kbps"""
    color_primaries: NotRequired[str]
    r"""The color primaries of the video stream"""
    color_range: NotRequired[str]
    r"""The color range of the video stream"""
    color_space: NotRequired[str]
    r"""The color space of the video stream"""
    color_trc: NotRequired[str]
    r"""The transfer characteristics (TRC) of the video stream"""
    bit_depth: NotRequired[int]
    r"""The bit depth of the video stream"""
    chroma_location: NotRequired[str]
    r"""The chroma location of the video stream"""
    stream_identifier: NotRequired[str]
    r"""The identifier of the video stream"""
    chroma_subsampling: NotRequired[str]
    r"""The chroma subsampling format"""
    coded_height: NotRequired[int]
    r"""The coded height of the video stream"""
    coded_width: NotRequired[int]
    r"""The coded width of the video stream"""
    frame_rate: NotRequired[float]
    r"""The frame rate of the video stream"""
    has_scaling_matrix: NotRequired[bool]
    r"""Indicates if the stream has a scaling matrix"""
    hearing_impaired: NotRequired[bool]
    closed_captions: NotRequired[bool]
    embedded_in_video: NotRequired[str]
    height: NotRequired[int]
    r"""The height of the video stream"""
    level: NotRequired[int]
    r"""The level of the video codec"""
    profile: NotRequired[str]
    r"""The profile of the video codec"""
    ref_frames: NotRequired[int]
    r"""Number of reference frames"""
    scan_type: NotRequired[str]
    r"""The scan type (progressive or interlaced)"""
    width: NotRequired[int]
    r"""The width of the video stream"""
    display_title: NotRequired[str]
    r"""Display title of the stream"""
    extended_display_title: NotRequired[str]
    r"""Extended display title of the stream"""
    channels: NotRequired[int]
    r"""Number of audio channels (for audio streams)"""
    language: NotRequired[str]
    r"""The language of the stream (for audio/subtitle streams)"""
    language_tag: NotRequired[str]
    r"""Language tag of the stream"""
    language_code: NotRequired[str]
    r"""Language code of the stream"""
    audio_channel_layout: NotRequired[str]
    r"""The audio channel layout"""
    sampling_rate: NotRequired[int]
    r"""Sampling rate of the audio stream in Hz"""
    title: NotRequired[str]
    r"""Title of the subtitle track (for subtitle streams)"""
    can_auto_sync: NotRequired[bool]
    r"""Indicates if the subtitle stream can auto-sync"""


class Stream(BaseModel):
    id: int

    stream_type: Annotated[int, pydantic.Field(alias="streamType")]
    r"""Type of stream (1 = video, 2 = audio, 3 = subtitle)"""

    codec: str
    r"""Codec used by the stream"""

    index: int
    r"""The index of the stream"""

    default: Optional[bool] = None
    r"""Indicates if this is the default stream"""

    selected: Optional[bool] = None
    r"""Indicates if the stream is selected"""

    bitrate: Optional[int] = None
    r"""The bitrate of the stream in kbps"""

    color_primaries: Annotated[
        Optional[str], pydantic.Field(alias="colorPrimaries")
    ] = None
    r"""The color primaries of the video stream"""

    color_range: Annotated[Optional[str], pydantic.Field(alias="colorRange")] = None
    r"""The color range of the video stream"""

    color_space: Annotated[Optional[str], pydantic.Field(alias="colorSpace")] = None
    r"""The color space of the video stream"""

    color_trc: Annotated[Optional[str], pydantic.Field(alias="colorTrc")] = None
    r"""The transfer characteristics (TRC) of the video stream"""

    bit_depth: Annotated[Optional[int], pydantic.Field(alias="bitDepth")] = None
    r"""The bit depth of the video stream"""

    chroma_location: Annotated[
        Optional[str], pydantic.Field(alias="chromaLocation")
    ] = None
    r"""The chroma location of the video stream"""

    stream_identifier: Annotated[
        Optional[str], pydantic.Field(alias="streamIdentifier")
    ] = None
    r"""The identifier of the video stream"""

    chroma_subsampling: Annotated[
        Optional[str], pydantic.Field(alias="chromaSubsampling")
    ] = None
    r"""The chroma subsampling format"""

    coded_height: Annotated[Optional[int], pydantic.Field(alias="codedHeight")] = None
    r"""The coded height of the video stream"""

    coded_width: Annotated[Optional[int], pydantic.Field(alias="codedWidth")] = None
    r"""The coded width of the video stream"""

    frame_rate: Annotated[Optional[float], pydantic.Field(alias="frameRate")] = None
    r"""The frame rate of the video stream"""

    has_scaling_matrix: Annotated[
        Optional[bool], pydantic.Field(alias="hasScalingMatrix")
    ] = None
    r"""Indicates if the stream has a scaling matrix"""

    hearing_impaired: Annotated[
        Optional[bool], pydantic.Field(alias="hearingImpaired")
    ] = None

    closed_captions: Annotated[
        Optional[bool], pydantic.Field(alias="closedCaptions")
    ] = None

    embedded_in_video: Annotated[
        Optional[str], pydantic.Field(alias="embeddedInVideo")
    ] = None

    height: Optional[int] = None
    r"""The height of the video stream"""

    level: Optional[int] = None
    r"""The level of the video codec"""

    profile: Optional[str] = None
    r"""The profile of the video codec"""

    ref_frames: Annotated[Optional[int], pydantic.Field(alias="refFrames")] = None
    r"""Number of reference frames"""

    scan_type: Annotated[Optional[str], pydantic.Field(alias="scanType")] = None
    r"""The scan type (progressive or interlaced)"""

    width: Optional[int] = None
    r"""The width of the video stream"""

    display_title: Annotated[Optional[str], pydantic.Field(alias="displayTitle")] = None
    r"""Display title of the stream"""

    extended_display_title: Annotated[
        Optional[str], pydantic.Field(alias="extendedDisplayTitle")
    ] = None
    r"""Extended display title of the stream"""

    channels: Optional[int] = None
    r"""Number of audio channels (for audio streams)"""

    language: Optional[str] = None
    r"""The language of the stream (for audio/subtitle streams)"""

    language_tag: Annotated[Optional[str], pydantic.Field(alias="languageTag")] = None
    r"""Language tag of the stream"""

    language_code: Annotated[Optional[str], pydantic.Field(alias="languageCode")] = None
    r"""Language code of the stream"""

    audio_channel_layout: Annotated[
        Optional[str], pydantic.Field(alias="audioChannelLayout")
    ] = None
    r"""The audio channel layout"""

    sampling_rate: Annotated[Optional[int], pydantic.Field(alias="samplingRate")] = None
    r"""Sampling rate of the audio stream in Hz"""

    title: Optional[str] = None
    r"""Title of the subtitle track (for subtitle streams)"""

    can_auto_sync: Annotated[Optional[bool], pydantic.Field(alias="canAutoSync")] = None
    r"""Indicates if the subtitle stream can auto-sync"""


class PartTypedDict(TypedDict):
    id: int
    key: str
    file: str
    size: int
    container: str
    r"""The container format of the media file.

    """
    duration: NotRequired[int]
    audio_profile: NotRequired[str]
    has64bit_offsets: NotRequired[bool]
    optimized_for_streaming: NotRequired[bool]
    video_profile: NotRequired[str]
    indexes: NotRequired[str]
    has_thumbnail: NotRequired[HasThumbnail]
    stream: NotRequired[List[StreamTypedDict]]


class Part(BaseModel):
    id: int

    key: str

    file: str

    size: int

    container: str
    r"""The container format of the media file.

    """

    duration: Optional[int] = None

    audio_profile: Annotated[Optional[str], pydantic.Field(alias="audioProfile")] = None

    has64bit_offsets: Annotated[
        Optional[bool], pydantic.Field(alias="has64bitOffsets")
    ] = None

    optimized_for_streaming: Annotated[
        Optional[bool], pydantic.Field(alias="optimizedForStreaming")
    ] = None

    video_profile: Annotated[Optional[str], pydantic.Field(alias="videoProfile")] = None

    indexes: Optional[str] = None

    has_thumbnail: Annotated[
        Optional[HasThumbnail], pydantic.Field(alias="hasThumbnail")
    ] = HasThumbnail.FALSE

    stream: Annotated[Optional[List[Stream]], pydantic.Field(alias="Stream")] = None


class MediaTypedDict(TypedDict):
    id: int
    container: str
    part: List[PartTypedDict]
    duration: NotRequired[int]
    bitrate: NotRequired[int]
    width: NotRequired[int]
    height: NotRequired[int]
    aspect_ratio: NotRequired[float]
    audio_profile: NotRequired[str]
    audio_channels: NotRequired[int]
    audio_codec: NotRequired[str]
    video_codec: NotRequired[str]
    video_resolution: NotRequired[str]
    video_frame_rate: NotRequired[str]
    video_profile: NotRequired[str]
    has_voice_activity: NotRequired[bool]
    optimized_for_streaming: NotRequired[OptimizedForStreaming]
    has64bit_offsets: NotRequired[bool]


class Media(BaseModel):
    id: int

    container: str

    part: Annotated[List[Part], pydantic.Field(alias="Part")]

    duration: Optional[int] = None

    bitrate: Optional[int] = None

    width: Optional[int] = None

    height: Optional[int] = None

    aspect_ratio: Annotated[Optional[float], pydantic.Field(alias="aspectRatio")] = None

    audio_profile: Annotated[Optional[str], pydantic.Field(alias="audioProfile")] = None

    audio_channels: Annotated[Optional[int], pydantic.Field(alias="audioChannels")] = (
        None
    )

    audio_codec: Annotated[Optional[str], pydantic.Field(alias="audioCodec")] = None

    video_codec: Annotated[Optional[str], pydantic.Field(alias="videoCodec")] = None

    video_resolution: Annotated[
        Optional[str], pydantic.Field(alias="videoResolution")
    ] = None

    video_frame_rate: Annotated[
        Optional[str], pydantic.Field(alias="videoFrameRate")
    ] = None

    video_profile: Annotated[Optional[str], pydantic.Field(alias="videoProfile")] = None

    has_voice_activity: Annotated[
        Optional[bool], pydantic.Field(alias="hasVoiceActivity")
    ] = None

    optimized_for_streaming: Annotated[
        Optional[OptimizedForStreaming], pydantic.Field(alias="optimizedForStreaming")
    ] = OptimizedForStreaming.DISABLE

    has64bit_offsets: Annotated[
        Optional[bool], pydantic.Field(alias="has64bitOffsets")
    ] = None


class GenreTypedDict(TypedDict):
    tag: NotRequired[str]


class Genre(BaseModel):
    tag: Optional[str] = None


class CountryTypedDict(TypedDict):
    tag: NotRequired[str]


class Country(BaseModel):
    tag: Optional[str] = None


class DirectorTypedDict(TypedDict):
    tag: NotRequired[str]


class Director(BaseModel):
    tag: Optional[str] = None


class WriterTypedDict(TypedDict):
    tag: NotRequired[str]


class Writer(BaseModel):
    tag: Optional[str] = None


class CollectionTypedDict(TypedDict):
    tag: NotRequired[str]


class Collection(BaseModel):
    tag: Optional[str] = None


class RoleTypedDict(TypedDict):
    id: NotRequired[int]
    r"""The ID of the tag or actor."""
    filter_: NotRequired[str]
    r"""The filter used to find the actor or tag."""
    thumb: NotRequired[str]
    r"""The thumbnail of the actor"""
    tag: NotRequired[str]
    r"""The name of the tag or actor."""
    tag_key: NotRequired[str]
    r"""Unique identifier for the tag."""
    role: NotRequired[str]
    r"""The role of the actor or tag in the media."""


class Role(BaseModel):
    id: Optional[int] = None
    r"""The ID of the tag or actor."""

    filter_: Annotated[Optional[str], pydantic.Field(alias="filter")] = None
    r"""The filter used to find the actor or tag."""

    thumb: Optional[str] = None
    r"""The thumbnail of the actor"""

    tag: Optional[str] = None
    r"""The name of the tag or actor."""

    tag_key: Annotated[Optional[str], pydantic.Field(alias="tagKey")] = None
    r"""Unique identifier for the tag."""

    role: Optional[str] = None
    r"""The role of the actor or tag in the media."""


class LocationTypedDict(TypedDict):
    path: NotRequired[str]


class Location(BaseModel):
    path: Optional[str] = None


class MediaGUIDTypedDict(TypedDict):
    id: str
    r"""Can be one of the following formats:
    imdb://tt13015952, tmdb://2434012, tvdb://7945991

    """


class MediaGUID(BaseModel):
    id: str
    r"""Can be one of the following formats:
    imdb://tt13015952, tmdb://2434012, tvdb://7945991

    """


class UltraBlurColorsTypedDict(TypedDict):
    top_left: str
    top_right: str
    bottom_right: str
    bottom_left: str


class UltraBlurColors(BaseModel):
    top_left: Annotated[str, pydantic.Field(alias="topLeft")]

    top_right: Annotated[str, pydantic.Field(alias="topRight")]

    bottom_right: Annotated[str, pydantic.Field(alias="bottomRight")]

    bottom_left: Annotated[str, pydantic.Field(alias="bottomLeft")]


class MetaDataRatingTypedDict(TypedDict):
    image: str
    r"""A URI or path to the rating image."""
    value: float
    r"""The value of the rating."""
    type: str
    r"""The type of rating (e.g., audience, critic)."""


class MetaDataRating(BaseModel):
    image: str
    r"""A URI or path to the rating image."""

    value: float
    r"""The value of the rating."""

    type: str
    r"""The type of rating (e.g., audience, critic)."""


class GetRecentlyAddedHubsResponseType(str, Enum):
    COVER_POSTER = "coverPoster"
    BACKGROUND = "background"
    SNAPSHOT = "snapshot"
    CLEAR_LOGO = "clearLogo"


class GetRecentlyAddedImageTypedDict(TypedDict):
    alt: str
    type: GetRecentlyAddedHubsResponseType
    url: str


class GetRecentlyAddedImage(BaseModel):
    alt: str

    type: GetRecentlyAddedHubsResponseType

    url: str


class GetRecentlyAddedMetadataTypedDict(TypedDict):
    rating_key: str
    r"""The rating key (Media ID) of this media item.
    Note: This is always an integer, but is represented as a string in the API.

    """
    key: str
    guid: str
    type: GetRecentlyAddedHubsType
    r"""The type of media content

    """
    title: str
    summary: str
    added_at: int
    r"""Unix epoch datetime in seconds"""
    studio: NotRequired[str]
    skip_children: NotRequired[bool]
    library_section_id: NotRequired[int]
    library_section_title: NotRequired[str]
    library_section_key: NotRequired[str]
    slug: NotRequired[str]
    content_rating: NotRequired[str]
    rating: NotRequired[float]
    audience_rating: NotRequired[float]
    year: NotRequired[int]
    season_count: NotRequired[int]
    tagline: NotRequired[str]
    flatten_seasons: NotRequired[FlattenSeasons]
    r"""Setting that indicates if seasons are set to hidden for the show. (-1 = Library default, 0 = Hide, 1 = Show)."""
    episode_sort: NotRequired[EpisodeSort]
    r"""Setting that indicates how episodes are sorted for the show. (-1 = Library default, 0 = Oldest first, 1 = Newest first)."""
    enable_credits_marker_generation: NotRequired[EnableCreditsMarkerGeneration]
    r"""Setting that indicates if credits markers detection is enabled. (-1 = Library default, 0 = Disabled)."""
    show_ordering: NotRequired[ShowOrdering]
    r"""Setting that indicates the episode ordering for the show
    None = Library default,
    tmdbAiring = The Movie Database (Aired),
    tvdbAiring = TheTVDB (Aired),
    tvdbDvd = TheTVDB (DVD),
    tvdbAbsolute = TheTVDB (Absolute)).

    """
    thumb: NotRequired[str]
    art: NotRequired[str]
    banner: NotRequired[str]
    duration: NotRequired[int]
    originally_available_at: NotRequired[date]
    updated_at: NotRequired[int]
    r"""Unix epoch datetime in seconds"""
    audience_rating_image: NotRequired[str]
    chapter_source: NotRequired[str]
    primary_extra_key: NotRequired[str]
    rating_image: NotRequired[str]
    grandparent_rating_key: NotRequired[str]
    grandparent_guid: NotRequired[str]
    grandparent_key: NotRequired[str]
    grandparent_title: NotRequired[str]
    grandparent_thumb: NotRequired[str]
    parent_slug: NotRequired[str]
    grandparent_slug: NotRequired[str]
    grandparent_art: NotRequired[str]
    grandparent_theme: NotRequired[str]
    media: NotRequired[List[MediaTypedDict]]
    r"""The Media object is only included when type query is `4` or higher.

    """
    genre: NotRequired[List[GenreTypedDict]]
    country: NotRequired[List[CountryTypedDict]]
    director: NotRequired[List[DirectorTypedDict]]
    writer: NotRequired[List[WriterTypedDict]]
    collection: NotRequired[List[CollectionTypedDict]]
    role: NotRequired[List[RoleTypedDict]]
    location: NotRequired[List[LocationTypedDict]]
    media_guid: NotRequired[List[MediaGUIDTypedDict]]
    r"""The Guid object is only included in the response if the `includeGuids` parameter is set to `1`.

    """
    ultra_blur_colors: NotRequired[UltraBlurColorsTypedDict]
    meta_data_rating: NotRequired[List[MetaDataRatingTypedDict]]
    image: NotRequired[List[GetRecentlyAddedImageTypedDict]]
    title_sort: NotRequired[str]
    view_count: NotRequired[int]
    last_viewed_at: NotRequired[int]
    original_title: NotRequired[str]
    view_offset: NotRequired[int]
    skip_count: NotRequired[int]
    index: NotRequired[int]
    theme: NotRequired[str]
    leaf_count: NotRequired[int]
    viewed_leaf_count: NotRequired[int]
    child_count: NotRequired[int]
    has_premium_extras: NotRequired[str]
    has_premium_primary_extra: NotRequired[str]
    parent_rating_key: NotRequired[str]
    r"""The rating key of the parent item.

    """
    parent_guid: NotRequired[str]
    parent_studio: NotRequired[str]
    parent_key: NotRequired[str]
    parent_title: NotRequired[str]
    parent_index: NotRequired[int]
    parent_year: NotRequired[int]
    parent_thumb: NotRequired[str]
    parent_theme: NotRequired[str]


class GetRecentlyAddedMetadata(BaseModel):
    rating_key: Annotated[str, pydantic.Field(alias="ratingKey")]
    r"""The rating key (Media ID) of this media item.
    Note: This is always an integer, but is represented as a string in the API.

    """

    key: str

    guid: str

    type: GetRecentlyAddedHubsType
    r"""The type of media content

    """

    title: str

    summary: str

    added_at: Annotated[int, pydantic.Field(alias="addedAt")]
    r"""Unix epoch datetime in seconds"""

    studio: Optional[str] = None

    skip_children: Annotated[Optional[bool], pydantic.Field(alias="skipChildren")] = (
        None
    )

    library_section_id: Annotated[
        Optional[int], pydantic.Field(alias="librarySectionID")
    ] = None

    library_section_title: Annotated[
        Optional[str], pydantic.Field(alias="librarySectionTitle")
    ] = None

    library_section_key: Annotated[
        Optional[str], pydantic.Field(alias="librarySectionKey")
    ] = None

    slug: Optional[str] = None

    content_rating: Annotated[Optional[str], pydantic.Field(alias="contentRating")] = (
        None
    )

    rating: Optional[float] = None

    audience_rating: Annotated[
        Optional[float], pydantic.Field(alias="audienceRating")
    ] = None

    year: Optional[int] = None

    season_count: Annotated[Optional[int], pydantic.Field(alias="seasonCount")] = None

    tagline: Optional[str] = None

    flatten_seasons: Annotated[
        Optional[FlattenSeasons], pydantic.Field(alias="flattenSeasons")
    ] = None
    r"""Setting that indicates if seasons are set to hidden for the show. (-1 = Library default, 0 = Hide, 1 = Show)."""

    episode_sort: Annotated[
        Optional[EpisodeSort], pydantic.Field(alias="episodeSort")
    ] = None
    r"""Setting that indicates how episodes are sorted for the show. (-1 = Library default, 0 = Oldest first, 1 = Newest first)."""

    enable_credits_marker_generation: Annotated[
        Optional[EnableCreditsMarkerGeneration],
        pydantic.Field(alias="enableCreditsMarkerGeneration"),
    ] = None
    r"""Setting that indicates if credits markers detection is enabled. (-1 = Library default, 0 = Disabled)."""

    show_ordering: Annotated[
        Optional[ShowOrdering], pydantic.Field(alias="showOrdering")
    ] = None
    r"""Setting that indicates the episode ordering for the show
    None = Library default,
    tmdbAiring = The Movie Database (Aired),
    tvdbAiring = TheTVDB (Aired),
    tvdbDvd = TheTVDB (DVD),
    tvdbAbsolute = TheTVDB (Absolute)).

    """

    thumb: Optional[str] = None

    art: Optional[str] = None

    banner: Optional[str] = None

    duration: Optional[int] = None

    originally_available_at: Annotated[
        Optional[date], pydantic.Field(alias="originallyAvailableAt")
    ] = None

    updated_at: Annotated[Optional[int], pydantic.Field(alias="updatedAt")] = None
    r"""Unix epoch datetime in seconds"""

    audience_rating_image: Annotated[
        Optional[str], pydantic.Field(alias="audienceRatingImage")
    ] = None

    chapter_source: Annotated[Optional[str], pydantic.Field(alias="chapterSource")] = (
        None
    )

    primary_extra_key: Annotated[
        Optional[str], pydantic.Field(alias="primaryExtraKey")
    ] = None

    rating_image: Annotated[Optional[str], pydantic.Field(alias="ratingImage")] = None

    grandparent_rating_key: Annotated[
        Optional[str], pydantic.Field(alias="grandparentRatingKey")
    ] = None

    grandparent_guid: Annotated[
        Optional[str], pydantic.Field(alias="grandparentGuid")
    ] = None

    grandparent_key: Annotated[
        Optional[str], pydantic.Field(alias="grandparentKey")
    ] = None

    grandparent_title: Annotated[
        Optional[str], pydantic.Field(alias="grandparentTitle")
    ] = None

    grandparent_thumb: Annotated[
        Optional[str], pydantic.Field(alias="grandparentThumb")
    ] = None

    parent_slug: Annotated[Optional[str], pydantic.Field(alias="parentSlug")] = None

    grandparent_slug: Annotated[
        Optional[str], pydantic.Field(alias="grandparentSlug")
    ] = None

    grandparent_art: Annotated[
        Optional[str], pydantic.Field(alias="grandparentArt")
    ] = None

    grandparent_theme: Annotated[
        Optional[str], pydantic.Field(alias="grandparentTheme")
    ] = None

    media: Annotated[Optional[List[Media]], pydantic.Field(alias="Media")] = None
    r"""The Media object is only included when type query is `4` or higher.

    """

    genre: Annotated[Optional[List[Genre]], pydantic.Field(alias="Genre")] = None

    country: Annotated[Optional[List[Country]], pydantic.Field(alias="Country")] = None

    director: Annotated[Optional[List[Director]], pydantic.Field(alias="Director")] = (
        None
    )

    writer: Annotated[Optional[List[Writer]], pydantic.Field(alias="Writer")] = None

    collection: Annotated[
        Optional[List[Collection]], pydantic.Field(alias="Collection")
    ] = None

    role: Annotated[Optional[List[Role]], pydantic.Field(alias="Role")] = None

    location: Annotated[Optional[List[Location]], pydantic.Field(alias="Location")] = (
        None
    )

    media_guid: Annotated[Optional[List[MediaGUID]], pydantic.Field(alias="Guid")] = (
        None
    )
    r"""The Guid object is only included in the response if the `includeGuids` parameter is set to `1`.

    """

    ultra_blur_colors: Annotated[
        Optional[UltraBlurColors], pydantic.Field(alias="UltraBlurColors")
    ] = None

    meta_data_rating: Annotated[
        Optional[List[MetaDataRating]], pydantic.Field(alias="Rating")
    ] = None

    image: Annotated[
        Optional[List[GetRecentlyAddedImage]], pydantic.Field(alias="Image")
    ] = None

    title_sort: Annotated[Optional[str], pydantic.Field(alias="titleSort")] = None

    view_count: Annotated[Optional[int], pydantic.Field(alias="viewCount")] = None

    last_viewed_at: Annotated[Optional[int], pydantic.Field(alias="lastViewedAt")] = (
        None
    )

    original_title: Annotated[Optional[str], pydantic.Field(alias="originalTitle")] = (
        None
    )

    view_offset: Annotated[Optional[int], pydantic.Field(alias="viewOffset")] = None

    skip_count: Annotated[Optional[int], pydantic.Field(alias="skipCount")] = None

    index: Optional[int] = None

    theme: Optional[str] = None

    leaf_count: Annotated[Optional[int], pydantic.Field(alias="leafCount")] = None

    viewed_leaf_count: Annotated[
        Optional[int], pydantic.Field(alias="viewedLeafCount")
    ] = None

    child_count: Annotated[Optional[int], pydantic.Field(alias="childCount")] = None

    has_premium_extras: Annotated[
        Optional[str], pydantic.Field(alias="hasPremiumExtras")
    ] = None

    has_premium_primary_extra: Annotated[
        Optional[str], pydantic.Field(alias="hasPremiumPrimaryExtra")
    ] = None

    parent_rating_key: Annotated[
        Optional[str], pydantic.Field(alias="parentRatingKey")
    ] = None
    r"""The rating key of the parent item.

    """

    parent_guid: Annotated[Optional[str], pydantic.Field(alias="parentGuid")] = None

    parent_studio: Annotated[Optional[str], pydantic.Field(alias="parentStudio")] = None

    parent_key: Annotated[Optional[str], pydantic.Field(alias="parentKey")] = None

    parent_title: Annotated[Optional[str], pydantic.Field(alias="parentTitle")] = None

    parent_index: Annotated[Optional[int], pydantic.Field(alias="parentIndex")] = None

    parent_year: Annotated[Optional[int], pydantic.Field(alias="parentYear")] = None

    parent_thumb: Annotated[Optional[str], pydantic.Field(alias="parentThumb")] = None

    parent_theme: Annotated[Optional[str], pydantic.Field(alias="parentTheme")] = None


class GetRecentlyAddedMediaContainerTypedDict(TypedDict):
    size: float
    offset: NotRequired[int]
    total_size: NotRequired[int]
    identifier: NotRequired[str]
    allow_sync: NotRequired[bool]
    meta: NotRequired[MetaTypedDict]
    r"""The Meta object is only included in the response if the `includeMeta` parameter is set to `1`.

    """
    metadata: NotRequired[List[GetRecentlyAddedMetadataTypedDict]]


class GetRecentlyAddedMediaContainer(BaseModel):
    size: float

    offset: Optional[int] = None

    total_size: Annotated[Optional[int], pydantic.Field(alias="totalSize")] = None

    identifier: Optional[str] = None

    allow_sync: Annotated[Optional[bool], pydantic.Field(alias="allowSync")] = None

    meta: Annotated[Optional[Meta], pydantic.Field(alias="Meta")] = None
    r"""The Meta object is only included in the response if the `includeMeta` parameter is set to `1`.

    """

    metadata: Annotated[
        Optional[List[GetRecentlyAddedMetadata]], pydantic.Field(alias="Metadata")
    ] = None


class GetRecentlyAddedResponseBodyTypedDict(TypedDict):
    r"""A successful response with recently added content."""

    media_container: NotRequired[GetRecentlyAddedMediaContainerTypedDict]


class GetRecentlyAddedResponseBody(BaseModel):
    r"""A successful response with recently added content."""

    media_container: Annotated[
        Optional[GetRecentlyAddedMediaContainer], pydantic.Field(alias="MediaContainer")
    ] = None


class GetRecentlyAddedResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[GetRecentlyAddedResponseBodyTypedDict]
    r"""A successful response with recently added content."""


class GetRecentlyAddedResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[GetRecentlyAddedResponseBody] = None
    r"""A successful response with recently added content."""
