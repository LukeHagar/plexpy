"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from plex_api_client import utils
from plex_api_client.types import BaseModel
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GetTokenByPinIDPlexErrorsTypedDict(TypedDict):
    code: NotRequired[int]
    message: NotRequired[str]


class GetTokenByPinIDPlexErrors(BaseModel):
    code: Optional[int] = None

    message: Optional[str] = None


class GetTokenByPinIDResponseBodyData(BaseModel):
    errors: Optional[List[GetTokenByPinIDPlexErrors]] = None

    raw_response: Annotated[Optional[httpx.Response], pydantic.Field(exclude=True)] = (
        None
    )
    r"""Raw HTTP response; suitable for custom response parsing"""


class GetTokenByPinIDResponseBody(Exception):
    r"""Not Found or Expired"""

    data: GetTokenByPinIDResponseBodyData

    def __init__(self, data: GetTokenByPinIDResponseBodyData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, GetTokenByPinIDResponseBodyData)


class GetTokenByPinIDErrorsTypedDict(TypedDict):
    code: NotRequired[int]
    message: NotRequired[str]
    status: NotRequired[int]


class GetTokenByPinIDErrors(BaseModel):
    code: Optional[int] = None

    message: Optional[str] = None

    status: Optional[int] = None


class GetTokenByPinIDBadRequestData(BaseModel):
    errors: Optional[List[GetTokenByPinIDErrors]] = None

    raw_response: Annotated[Optional[httpx.Response], pydantic.Field(exclude=True)] = (
        None
    )
    r"""Raw HTTP response; suitable for custom response parsing"""


class GetTokenByPinIDBadRequest(Exception):
    r"""Bad Request - A parameter was not specified, or was specified incorrectly."""

    data: GetTokenByPinIDBadRequestData

    def __init__(self, data: GetTokenByPinIDBadRequestData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, GetTokenByPinIDBadRequestData)
