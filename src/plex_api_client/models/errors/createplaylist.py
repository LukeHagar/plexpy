"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from plex_api_client import utils
from plex_api_client.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreatePlaylistPlaylistsErrorsTypedDict(TypedDict):
    code: NotRequired[int]
    message: NotRequired[str]
    status: NotRequired[int]


class CreatePlaylistPlaylistsErrors(BaseModel):
    code: Optional[int] = None

    message: Optional[str] = None

    status: Optional[int] = None


class CreatePlaylistUnauthorizedData(BaseModel):
    errors: Optional[List[CreatePlaylistPlaylistsErrors]] = None

    raw_response: Annotated[Optional[httpx.Response], pydantic.Field(exclude=True)] = (
        None
    )
    r"""Raw HTTP response; suitable for custom response parsing"""


class CreatePlaylistUnauthorized(Exception):
    r"""Unauthorized - Returned if the X-Plex-Token is missing from the header or query."""

    data: CreatePlaylistUnauthorizedData

    def __init__(self, data: CreatePlaylistUnauthorizedData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, CreatePlaylistUnauthorizedData)


class CreatePlaylistErrorsTypedDict(TypedDict):
    code: NotRequired[int]
    message: NotRequired[str]
    status: NotRequired[int]


class CreatePlaylistErrors(BaseModel):
    code: Optional[int] = None

    message: Optional[str] = None

    status: Optional[int] = None


class CreatePlaylistBadRequestData(BaseModel):
    errors: Optional[List[CreatePlaylistErrors]] = None

    raw_response: Annotated[Optional[httpx.Response], pydantic.Field(exclude=True)] = (
        None
    )
    r"""Raw HTTP response; suitable for custom response parsing"""


class CreatePlaylistBadRequest(Exception):
    r"""Bad Request - A parameter was not specified, or was specified incorrectly."""

    data: CreatePlaylistBadRequestData

    def __init__(self, data: CreatePlaylistBadRequestData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, CreatePlaylistBadRequestData)
