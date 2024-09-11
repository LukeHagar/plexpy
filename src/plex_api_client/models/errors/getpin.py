"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from plex_api_client import utils
from plex_api_client.types import BaseModel
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GetPinErrorsTypedDict(TypedDict):
    code: NotRequired[int]
    message: NotRequired[str]
    status: NotRequired[int]


class GetPinErrors(BaseModel):
    code: Optional[int] = None

    message: Optional[str] = None

    status: Optional[int] = None


class GetPinBadRequestData(BaseModel):
    errors: Optional[List[GetPinErrors]] = None

    raw_response: Annotated[Optional[httpx.Response], pydantic.Field(exclude=True)] = (
        None
    )
    r"""Raw HTTP response; suitable for custom response parsing"""


class GetPinBadRequest(Exception):
    r"""Bad Request - A parameter was not specified, or was specified incorrectly."""

    data: GetPinBadRequestData

    def __init__(self, data: GetPinBadRequestData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, GetPinBadRequestData)
