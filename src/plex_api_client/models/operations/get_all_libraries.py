"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from plex_api_client.types import BaseModel
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class LocationTypedDict(TypedDict):
    id: int
    path: str


class Location(BaseModel):
    id: int

    path: str


class GetAllLibrariesDirectoryTypedDict(TypedDict):
    allow_sync: bool
    art: str
    composite: str
    filters: bool
    refreshing: bool
    thumb: str
    key: str
    type: str
    title: str
    agent: str
    scanner: str
    language: str
    uuid: str
    updated_at: int
    r"""Unix epoch datetime in seconds"""
    created_at: int
    r"""Unix epoch datetime in seconds"""
    scanned_at: int
    r"""Unix epoch datetime in seconds"""
    content: bool
    directory: bool
    content_changed_at: int
    hidden: int
    location: List[LocationTypedDict]


class GetAllLibrariesDirectory(BaseModel):
    allow_sync: Annotated[bool, pydantic.Field(alias="allowSync")]

    art: str

    composite: str

    filters: bool

    refreshing: bool

    thumb: str

    key: str

    type: str

    title: str

    agent: str

    scanner: str

    language: str

    uuid: str

    updated_at: Annotated[int, pydantic.Field(alias="updatedAt")]
    r"""Unix epoch datetime in seconds"""

    created_at: Annotated[int, pydantic.Field(alias="createdAt")]
    r"""Unix epoch datetime in seconds"""

    scanned_at: Annotated[int, pydantic.Field(alias="scannedAt")]
    r"""Unix epoch datetime in seconds"""

    content: bool

    directory: bool

    content_changed_at: Annotated[int, pydantic.Field(alias="contentChangedAt")]

    hidden: int

    location: Annotated[List[Location], pydantic.Field(alias="Location")]


class GetAllLibrariesMediaContainerTypedDict(TypedDict):
    size: int
    allow_sync: bool
    title1: str
    directory: List[GetAllLibrariesDirectoryTypedDict]


class GetAllLibrariesMediaContainer(BaseModel):
    size: int

    allow_sync: Annotated[bool, pydantic.Field(alias="allowSync")]

    title1: str

    directory: Annotated[
        List[GetAllLibrariesDirectory], pydantic.Field(alias="Directory")
    ]


class GetAllLibrariesResponseBodyTypedDict(TypedDict):
    r"""The libraries available on the Server"""

    media_container: GetAllLibrariesMediaContainerTypedDict


class GetAllLibrariesResponseBody(BaseModel):
    r"""The libraries available on the Server"""

    media_container: Annotated[
        GetAllLibrariesMediaContainer, pydantic.Field(alias="MediaContainer")
    ]


class GetAllLibrariesResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[GetAllLibrariesResponseBodyTypedDict]
    r"""The libraries available on the Server"""


class GetAllLibrariesResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[GetAllLibrariesResponseBody] = None
    r"""The libraries available on the Server"""
