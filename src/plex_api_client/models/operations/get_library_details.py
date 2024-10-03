"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import httpx
from plex_api_client.types import BaseModel
from plex_api_client.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class IncludeDetails(int, Enum):
    r"""Whether or not to include details for a section (types, filters, and sorts).
    Only exists for backwards compatibility, media providers other than the server libraries have it on always.

    """

    ZERO = 0
    ONE = 1


class GetLibraryDetailsRequestTypedDict(TypedDict):
    section_key: int
    r"""The unique key of the Plex library.
    Note: This is unique in the context of the Plex server.

    """
    include_details: NotRequired[IncludeDetails]
    r"""Whether or not to include details for a section (types, filters, and sorts).
    Only exists for backwards compatibility, media providers other than the server libraries have it on always.

    """


class GetLibraryDetailsRequest(BaseModel):
    section_key: Annotated[
        int,
        pydantic.Field(alias="sectionKey"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The unique key of the Plex library.
    Note: This is unique in the context of the Plex server.

    """

    include_details: Annotated[
        Optional[IncludeDetails],
        pydantic.Field(alias="includeDetails"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = IncludeDetails.ZERO
    r"""Whether or not to include details for a section (types, filters, and sorts).
    Only exists for backwards compatibility, media providers other than the server libraries have it on always.

    """


class GetLibraryDetailsDirectoryTypedDict(TypedDict):
    key: NotRequired[str]
    title: NotRequired[str]
    secondary: NotRequired[bool]
    prompt: NotRequired[str]
    search: NotRequired[bool]


class GetLibraryDetailsDirectory(BaseModel):
    key: Optional[str] = None

    title: Optional[str] = None

    secondary: Optional[bool] = None

    prompt: Optional[str] = None

    search: Optional[bool] = None


class GetLibraryDetailsFilterTypedDict(TypedDict):
    filter_: NotRequired[str]
    filter_type: NotRequired[str]
    key: NotRequired[str]
    title: NotRequired[str]
    type: NotRequired[str]


class GetLibraryDetailsFilter(BaseModel):
    filter_: Annotated[Optional[str], pydantic.Field(alias="filter")] = None

    filter_type: Annotated[Optional[str], pydantic.Field(alias="filterType")] = None

    key: Optional[str] = None

    title: Optional[str] = None

    type: Optional[str] = None


class GetLibraryDetailsSortTypedDict(TypedDict):
    default: NotRequired[str]
    default_direction: NotRequired[str]
    desc_key: NotRequired[str]
    first_character_key: NotRequired[str]
    key: NotRequired[str]
    title: NotRequired[str]


class GetLibraryDetailsSort(BaseModel):
    default: Optional[str] = None

    default_direction: Annotated[
        Optional[str], pydantic.Field(alias="defaultDirection")
    ] = None

    desc_key: Annotated[Optional[str], pydantic.Field(alias="descKey")] = None

    first_character_key: Annotated[
        Optional[str], pydantic.Field(alias="firstCharacterKey")
    ] = None

    key: Optional[str] = None

    title: Optional[str] = None


class GetLibraryDetailsFieldTypedDict(TypedDict):
    key: NotRequired[str]
    title: NotRequired[str]
    type: NotRequired[str]
    sub_type: NotRequired[str]


class GetLibraryDetailsField(BaseModel):
    key: Optional[str] = None

    title: Optional[str] = None

    type: Optional[str] = None

    sub_type: Annotated[Optional[str], pydantic.Field(alias="subType")] = None


class GetLibraryDetailsTypeTypedDict(TypedDict):
    key: NotRequired[str]
    type: NotRequired[str]
    title: NotRequired[str]
    active: NotRequired[bool]
    filter_: NotRequired[List[GetLibraryDetailsFilterTypedDict]]
    sort: NotRequired[List[GetLibraryDetailsSortTypedDict]]
    field: NotRequired[List[GetLibraryDetailsFieldTypedDict]]


class GetLibraryDetailsType(BaseModel):
    key: Optional[str] = None

    type: Optional[str] = None

    title: Optional[str] = None

    active: Optional[bool] = None

    filter_: Annotated[
        Optional[List[GetLibraryDetailsFilter]], pydantic.Field(alias="Filter")
    ] = None

    sort: Annotated[
        Optional[List[GetLibraryDetailsSort]], pydantic.Field(alias="Sort")
    ] = None

    field: Annotated[
        Optional[List[GetLibraryDetailsField]], pydantic.Field(alias="Field")
    ] = None


class GetLibraryDetailsOperatorTypedDict(TypedDict):
    key: NotRequired[str]
    title: NotRequired[str]


class GetLibraryDetailsOperator(BaseModel):
    key: Optional[str] = None

    title: Optional[str] = None


class GetLibraryDetailsFieldTypeTypedDict(TypedDict):
    type: NotRequired[str]
    operator: NotRequired[List[GetLibraryDetailsOperatorTypedDict]]


class GetLibraryDetailsFieldType(BaseModel):
    type: Optional[str] = None

    operator: Annotated[
        Optional[List[GetLibraryDetailsOperator]], pydantic.Field(alias="Operator")
    ] = None


class GetLibraryDetailsMediaContainerTypedDict(TypedDict):
    size: NotRequired[int]
    allow_sync: NotRequired[bool]
    art: NotRequired[str]
    content: NotRequired[str]
    identifier: NotRequired[str]
    library_section_id: NotRequired[int]
    media_tag_prefix: NotRequired[str]
    media_tag_version: NotRequired[int]
    thumb: NotRequired[str]
    title1: NotRequired[str]
    view_group: NotRequired[str]
    view_mode: NotRequired[int]
    directory: NotRequired[List[GetLibraryDetailsDirectoryTypedDict]]
    type: NotRequired[List[GetLibraryDetailsTypeTypedDict]]
    field_type: NotRequired[List[GetLibraryDetailsFieldTypeTypedDict]]


class GetLibraryDetailsMediaContainer(BaseModel):
    size: Optional[int] = None

    allow_sync: Annotated[Optional[bool], pydantic.Field(alias="allowSync")] = None

    art: Optional[str] = None

    content: Optional[str] = None

    identifier: Optional[str] = None

    library_section_id: Annotated[
        Optional[int], pydantic.Field(alias="librarySectionID")
    ] = None

    media_tag_prefix: Annotated[
        Optional[str], pydantic.Field(alias="mediaTagPrefix")
    ] = None

    media_tag_version: Annotated[
        Optional[int], pydantic.Field(alias="mediaTagVersion")
    ] = None

    thumb: Optional[str] = None

    title1: Optional[str] = None

    view_group: Annotated[Optional[str], pydantic.Field(alias="viewGroup")] = None

    view_mode: Annotated[Optional[int], pydantic.Field(alias="viewMode")] = None

    directory: Annotated[
        Optional[List[GetLibraryDetailsDirectory]], pydantic.Field(alias="Directory")
    ] = None

    type: Annotated[
        Optional[List[GetLibraryDetailsType]], pydantic.Field(alias="Type")
    ] = None

    field_type: Annotated[
        Optional[List[GetLibraryDetailsFieldType]], pydantic.Field(alias="FieldType")
    ] = None


class GetLibraryDetailsResponseBodyTypedDict(TypedDict):
    r"""The details of the library"""

    media_container: NotRequired[GetLibraryDetailsMediaContainerTypedDict]


class GetLibraryDetailsResponseBody(BaseModel):
    r"""The details of the library"""

    media_container: Annotated[
        Optional[GetLibraryDetailsMediaContainer],
        pydantic.Field(alias="MediaContainer"),
    ] = None


class GetLibraryDetailsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[GetLibraryDetailsResponseBodyTypedDict]
    r"""The details of the library"""


class GetLibraryDetailsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[GetLibraryDetailsResponseBody] = None
    r"""The details of the library"""
