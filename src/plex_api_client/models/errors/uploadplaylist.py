"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from plex_api_client import utils
from plex_api_client.types import BaseModel
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class UploadPlaylistPlaylistsErrorsTypedDict(TypedDict):
    code: NotRequired[int]
    message: NotRequired[str]
    status: NotRequired[int]


class UploadPlaylistPlaylistsErrors(BaseModel):
    code: Optional[int] = None

    message: Optional[str] = None

    status: Optional[int] = None


class UploadPlaylistUnauthorizedData(BaseModel):
    errors: Optional[List[UploadPlaylistPlaylistsErrors]] = None

    raw_response: Annotated[Optional[httpx.Response], pydantic.Field(exclude=True)] = (
        None
    )
    r"""Raw HTTP response; suitable for custom response parsing"""


class UploadPlaylistUnauthorized(Exception):
    r"""Unauthorized - Returned if the X-Plex-Token is missing from the header or query."""

    data: UploadPlaylistUnauthorizedData

    def __init__(self, data: UploadPlaylistUnauthorizedData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, UploadPlaylistUnauthorizedData)


class UploadPlaylistErrorsTypedDict(TypedDict):
    code: NotRequired[int]
    message: NotRequired[str]
    status: NotRequired[int]


class UploadPlaylistErrors(BaseModel):
    code: Optional[int] = None

    message: Optional[str] = None

    status: Optional[int] = None


class UploadPlaylistBadRequestData(BaseModel):
    errors: Optional[List[UploadPlaylistErrors]] = None

    raw_response: Annotated[Optional[httpx.Response], pydantic.Field(exclude=True)] = (
        None
    )
    r"""Raw HTTP response; suitable for custom response parsing"""


class UploadPlaylistBadRequest(Exception):
    r"""Bad Request - A parameter was not specified, or was specified incorrectly."""

    data: UploadPlaylistBadRequestData

    def __init__(self, data: UploadPlaylistBadRequestData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, UploadPlaylistBadRequestData)
