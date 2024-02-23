"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http


@dataclasses.dataclass
class UpdatePlayProgressRequest:
    key: str = dataclasses.field(metadata={'query_param': { 'field_name': 'key', 'style': 'form', 'explode': True }})
    r"""the media key"""
    time: float = dataclasses.field(metadata={'query_param': { 'field_name': 'time', 'style': 'form', 'explode': True }})
    r"""The time, in milliseconds, used to set the media playback progress."""
    state: str = dataclasses.field(metadata={'query_param': { 'field_name': 'state', 'style': 'form', 'explode': True }})
    r"""The playback state of the media item."""
    



@dataclasses.dataclass
class UpdatePlayProgressResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    

