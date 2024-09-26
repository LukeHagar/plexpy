"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from plex_api_client import utils
from plex_api_client.types import BaseModel
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class UpdatePlayProgressMediaErrorsTypedDict(TypedDict):
    code: NotRequired[int]
    message: NotRequired[str]
    status: NotRequired[int]


class UpdatePlayProgressMediaErrors(BaseModel):
    code: Optional[int] = None

    message: Optional[str] = None

    status: Optional[int] = None


class UpdatePlayProgressUnauthorizedData(BaseModel):
    errors: Optional[List[UpdatePlayProgressMediaErrors]] = None

    raw_response: Annotated[Optional[httpx.Response], pydantic.Field(exclude=True)] = (
        None
    )
    r"""Raw HTTP response; suitable for custom response parsing"""


class UpdatePlayProgressUnauthorized(Exception):
    r"""Unauthorized - Returned if the X-Plex-Token is missing from the header or query."""

    data: UpdatePlayProgressUnauthorizedData

    def __init__(self, data: UpdatePlayProgressUnauthorizedData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, UpdatePlayProgressUnauthorizedData)


class UpdatePlayProgressErrorsTypedDict(TypedDict):
    code: NotRequired[int]
    message: NotRequired[str]
    status: NotRequired[int]


class UpdatePlayProgressErrors(BaseModel):
    code: Optional[int] = None

    message: Optional[str] = None

    status: Optional[int] = None


class UpdatePlayProgressBadRequestData(BaseModel):
    errors: Optional[List[UpdatePlayProgressErrors]] = None

    raw_response: Annotated[Optional[httpx.Response], pydantic.Field(exclude=True)] = (
        None
    )
    r"""Raw HTTP response; suitable for custom response parsing"""


class UpdatePlayProgressBadRequest(Exception):
    r"""Bad Request - A parameter was not specified, or was specified incorrectly."""

    data: UpdatePlayProgressBadRequestData

    def __init__(self, data: UpdatePlayProgressBadRequestData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, UpdatePlayProgressBadRequestData)