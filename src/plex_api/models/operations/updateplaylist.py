"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class UpdatePlaylistRequest:
    playlist_id: float = dataclasses.field(metadata={'path_param': { 'field_name': 'playlistID', 'style': 'simple', 'explode': False }})
    r"""the ID of the playlist"""
    title: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'title', 'style': 'form', 'explode': True }})
    r"""name of the playlist"""
    summary: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'summary', 'style': 'form', 'explode': True }})
    r"""summary description of the playlist"""
    



@dataclasses.dataclass
class UpdatePlaylistResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    

