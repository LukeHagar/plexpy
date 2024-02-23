"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from enum import Enum

class State(str, Enum):
    r"""The state of the media item"""
    PLAYING = 'playing'
    PAUSED = 'paused'
    STOPPED = 'stopped'


@dataclasses.dataclass
class GetTimelineRequest:
    rating_key: float = dataclasses.field(metadata={'query_param': { 'field_name': 'ratingKey', 'style': 'form', 'explode': True }})
    r"""The rating key of the media item"""
    key: str = dataclasses.field(metadata={'query_param': { 'field_name': 'key', 'style': 'form', 'explode': True }})
    r"""The key of the media item to get the timeline for"""
    state: State = dataclasses.field(metadata={'query_param': { 'field_name': 'state', 'style': 'form', 'explode': True }})
    r"""The state of the media item"""
    has_mde: float = dataclasses.field(metadata={'query_param': { 'field_name': 'hasMDE', 'style': 'form', 'explode': True }})
    r"""Whether the media item has MDE"""
    time: float = dataclasses.field(metadata={'query_param': { 'field_name': 'time', 'style': 'form', 'explode': True }})
    r"""The time of the media item"""
    duration: float = dataclasses.field(metadata={'query_param': { 'field_name': 'duration', 'style': 'form', 'explode': True }})
    r"""The duration of the media item"""
    context: str = dataclasses.field(metadata={'query_param': { 'field_name': 'context', 'style': 'form', 'explode': True }})
    r"""The context of the media item"""
    play_queue_item_id: float = dataclasses.field(metadata={'query_param': { 'field_name': 'playQueueItemID', 'style': 'form', 'explode': True }})
    r"""The play queue item ID of the media item"""
    play_back_time: float = dataclasses.field(metadata={'query_param': { 'field_name': 'playBackTime', 'style': 'form', 'explode': True }})
    r"""The playback time of the media item"""
    row: float = dataclasses.field(metadata={'query_param': { 'field_name': 'row', 'style': 'form', 'explode': True }})
    r"""The row of the media item"""
    



@dataclasses.dataclass
class GetTimelineResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    

