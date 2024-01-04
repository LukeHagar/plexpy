"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class StartUniversalTranscodeRequest:
    has_mde: float = dataclasses.field(metadata={'query_param': { 'field_name': 'hasMDE', 'style': 'form', 'explode': True }})
    r"""Whether the media item has MDE"""
    media_index: float = dataclasses.field(metadata={'query_param': { 'field_name': 'mediaIndex', 'style': 'form', 'explode': True }})
    r"""The index of the media item to transcode"""
    part_index: float = dataclasses.field(metadata={'query_param': { 'field_name': 'partIndex', 'style': 'form', 'explode': True }})
    r"""The index of the part to transcode"""
    path: str = dataclasses.field(metadata={'query_param': { 'field_name': 'path', 'style': 'form', 'explode': True }})
    r"""The path to the media item to transcode"""
    protocol: str = dataclasses.field(metadata={'query_param': { 'field_name': 'protocol', 'style': 'form', 'explode': True }})
    r"""The protocol to use for the transcode session"""
    add_debug_overlay: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'addDebugOverlay', 'style': 'form', 'explode': True }})
    r"""Whether to add a debug overlay or not"""
    audio_boost: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'audioBoost', 'style': 'form', 'explode': True }})
    r"""The audio boost"""
    auto_adjust_quality: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'autoAdjustQuality', 'style': 'form', 'explode': True }})
    r"""Whether to auto adjust quality or not"""
    direct_play: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'directPlay', 'style': 'form', 'explode': True }})
    r"""Whether to use direct play or not"""
    direct_stream: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'directStream', 'style': 'form', 'explode': True }})
    r"""Whether to use direct stream or not"""
    fast_seek: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'fastSeek', 'style': 'form', 'explode': True }})
    r"""Whether to use fast seek or not"""
    location: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'location', 'style': 'form', 'explode': True }})
    r"""The location of the transcode session"""
    media_buffer_size: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'mediaBufferSize', 'style': 'form', 'explode': True }})
    r"""The size of the media buffer"""
    session: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'session', 'style': 'form', 'explode': True }})
    r"""The session ID"""
    subtites: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'subtites', 'style': 'form', 'explode': True }})
    r"""The subtitles"""
    subtitle_size: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'subtitleSize', 'style': 'form', 'explode': True }})
    r"""The size of the subtitles"""
    



@dataclasses.dataclass
class StartUniversalTranscodeResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    
