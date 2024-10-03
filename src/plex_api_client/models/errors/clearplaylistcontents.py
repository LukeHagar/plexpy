"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from plex_api_client import utils
from plex_api_client.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ClearPlaylistContentsPlaylistsErrorsTypedDict(TypedDict):
    code: NotRequired[int]
    message: NotRequired[str]
    status: NotRequired[int]


class ClearPlaylistContentsPlaylistsErrors(BaseModel):
    code: Optional[int] = None

    message: Optional[str] = None

    status: Optional[int] = None


class ClearPlaylistContentsUnauthorizedData(BaseModel):
    errors: Optional[List[ClearPlaylistContentsPlaylistsErrors]] = None

    raw_response: Annotated[Optional[httpx.Response], pydantic.Field(exclude=True)] = (
        None
    )
    r"""Raw HTTP response; suitable for custom response parsing"""


class ClearPlaylistContentsUnauthorized(Exception):
    r"""Unauthorized - Returned if the X-Plex-Token is missing from the header or query."""

    data: ClearPlaylistContentsUnauthorizedData

    def __init__(self, data: ClearPlaylistContentsUnauthorizedData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, ClearPlaylistContentsUnauthorizedData)


class ClearPlaylistContentsErrorsTypedDict(TypedDict):
    code: NotRequired[int]
    message: NotRequired[str]
    status: NotRequired[int]


class ClearPlaylistContentsErrors(BaseModel):
    code: Optional[int] = None

    message: Optional[str] = None

    status: Optional[int] = None


class ClearPlaylistContentsBadRequestData(BaseModel):
    errors: Optional[List[ClearPlaylistContentsErrors]] = None

    raw_response: Annotated[Optional[httpx.Response], pydantic.Field(exclude=True)] = (
        None
    )
    r"""Raw HTTP response; suitable for custom response parsing"""


class ClearPlaylistContentsBadRequest(Exception):
    r"""Bad Request - A parameter was not specified, or was specified incorrectly."""

    data: ClearPlaylistContentsBadRequestData

    def __init__(self, data: ClearPlaylistContentsBadRequestData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, ClearPlaylistContentsBadRequestData)
