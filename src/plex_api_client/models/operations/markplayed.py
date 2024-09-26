"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from plex_api_client.types import BaseModel
from plex_api_client.utils import FieldMetadata, QueryParamMetadata
from typing import TypedDict
from typing_extensions import Annotated


class MarkPlayedRequestTypedDict(TypedDict):
    key: float
    r"""The media key to mark as played"""


class MarkPlayedRequest(BaseModel):
    key: Annotated[
        float, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""The media key to mark as played"""


class MarkPlayedResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""


class MarkPlayedResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""