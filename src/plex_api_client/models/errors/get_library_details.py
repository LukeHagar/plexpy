"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from plex_api_client import utils
from plex_api_client.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetLibraryDetailsLibraryErrorsTypedDict(TypedDict):
    code: NotRequired[int]
    message: NotRequired[str]
    status: NotRequired[int]


class GetLibraryDetailsLibraryErrors(BaseModel):
    code: Optional[int] = None

    message: Optional[str] = None

    status: Optional[int] = None


class GetLibraryDetailsUnauthorizedData(BaseModel):
    errors: Optional[List[GetLibraryDetailsLibraryErrors]] = None

    raw_response: Annotated[Optional[httpx.Response], pydantic.Field(exclude=True)] = (
        None
    )
    r"""Raw HTTP response; suitable for custom response parsing"""


class GetLibraryDetailsUnauthorized(Exception):
    r"""Unauthorized - Returned if the X-Plex-Token is missing from the header or query."""

    data: GetLibraryDetailsUnauthorizedData

    def __init__(self, data: GetLibraryDetailsUnauthorizedData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, GetLibraryDetailsUnauthorizedData)


class GetLibraryDetailsErrorsTypedDict(TypedDict):
    code: NotRequired[int]
    message: NotRequired[str]
    status: NotRequired[int]


class GetLibraryDetailsErrors(BaseModel):
    code: Optional[int] = None

    message: Optional[str] = None

    status: Optional[int] = None


class GetLibraryDetailsBadRequestData(BaseModel):
    errors: Optional[List[GetLibraryDetailsErrors]] = None

    raw_response: Annotated[Optional[httpx.Response], pydantic.Field(exclude=True)] = (
        None
    )
    r"""Raw HTTP response; suitable for custom response parsing"""


class GetLibraryDetailsBadRequest(Exception):
    r"""Bad Request - A parameter was not specified, or was specified incorrectly."""

    data: GetLibraryDetailsBadRequestData

    def __init__(self, data: GetLibraryDetailsBadRequestData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, GetLibraryDetailsBadRequestData)
