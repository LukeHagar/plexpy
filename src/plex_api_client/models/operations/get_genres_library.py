"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from plex_api_client.types import BaseModel
from plex_api_client.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetGenresLibraryRequestTypedDict(TypedDict):
    section_key: int
    r"""The unique key of the Plex library.
    Note: This is unique in the context of the Plex server.

    """


class GetGenresLibraryRequest(BaseModel):
    section_key: Annotated[
        int,
        pydantic.Field(alias="sectionKey"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The unique key of the Plex library.
    Note: This is unique in the context of the Plex server.

    """


class GetGenresLibraryDirectoryTypedDict(TypedDict):
    fast_key: str
    key: str
    title: str
    type: str


class GetGenresLibraryDirectory(BaseModel):
    fast_key: Annotated[str, pydantic.Field(alias="fastKey")]

    key: str

    title: str

    type: str


class GetGenresLibraryMediaContainerTypedDict(TypedDict):
    size: float
    identifier: str
    allow_sync: bool
    art: str
    content: str
    media_tag_prefix: str
    media_tag_version: int
    nocache: bool
    thumb: str
    title1: str
    title2: str
    view_group: str
    offset: NotRequired[int]
    total_size: NotRequired[int]
    directory: NotRequired[List[GetGenresLibraryDirectoryTypedDict]]


class GetGenresLibraryMediaContainer(BaseModel):
    size: float

    identifier: str

    allow_sync: Annotated[bool, pydantic.Field(alias="allowSync")]

    art: str

    content: str

    media_tag_prefix: Annotated[str, pydantic.Field(alias="mediaTagPrefix")]

    media_tag_version: Annotated[int, pydantic.Field(alias="mediaTagVersion")]

    nocache: bool

    thumb: str

    title1: str

    title2: str

    view_group: Annotated[str, pydantic.Field(alias="viewGroup")]

    offset: Optional[int] = None

    total_size: Annotated[Optional[int], pydantic.Field(alias="totalSize")] = None

    directory: Annotated[
        Optional[List[GetGenresLibraryDirectory]], pydantic.Field(alias="Directory")
    ] = None


class GetGenresLibraryResponseBodyTypedDict(TypedDict):
    r"""Successful response containing media container data."""

    media_container: NotRequired[GetGenresLibraryMediaContainerTypedDict]


class GetGenresLibraryResponseBody(BaseModel):
    r"""Successful response containing media container data."""

    media_container: Annotated[
        Optional[GetGenresLibraryMediaContainer], pydantic.Field(alias="MediaContainer")
    ] = None


class GetGenresLibraryResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[GetGenresLibraryResponseBodyTypedDict]
    r"""Successful response containing media container data."""


class GetGenresLibraryResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[GetGenresLibraryResponseBody] = None
    r"""Successful response containing media container data."""
