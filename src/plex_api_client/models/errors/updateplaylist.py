"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from plex_api_client import utils
from plex_api_client.types import BaseModel
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class UpdatePlaylistPlaylistsErrorsTypedDict(TypedDict):
    code: NotRequired[int]
    message: NotRequired[str]
    status: NotRequired[int]


class UpdatePlaylistPlaylistsErrors(BaseModel):
    code: Optional[int] = None

    message: Optional[str] = None

    status: Optional[int] = None


class UpdatePlaylistUnauthorizedData(BaseModel):
    errors: Optional[List[UpdatePlaylistPlaylistsErrors]] = None

    raw_response: Annotated[Optional[httpx.Response], pydantic.Field(exclude=True)] = (
        None
    )
    r"""Raw HTTP response; suitable for custom response parsing"""


class UpdatePlaylistUnauthorized(Exception):
    r"""Unauthorized - Returned if the X-Plex-Token is missing from the header or query."""

    data: UpdatePlaylistUnauthorizedData

    def __init__(self, data: UpdatePlaylistUnauthorizedData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, UpdatePlaylistUnauthorizedData)


class UpdatePlaylistErrorsTypedDict(TypedDict):
    code: NotRequired[int]
    message: NotRequired[str]
    status: NotRequired[int]


class UpdatePlaylistErrors(BaseModel):
    code: Optional[int] = None

    message: Optional[str] = None

    status: Optional[int] = None


class UpdatePlaylistBadRequestData(BaseModel):
    errors: Optional[List[UpdatePlaylistErrors]] = None

    raw_response: Annotated[Optional[httpx.Response], pydantic.Field(exclude=True)] = (
        None
    )
    r"""Raw HTTP response; suitable for custom response parsing"""


class UpdatePlaylistBadRequest(Exception):
    r"""Bad Request - A parameter was not specified, or was specified incorrectly."""

    data: UpdatePlaylistBadRequestData

    def __init__(self, data: UpdatePlaylistBadRequestData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, UpdatePlaylistBadRequestData)