"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from plex_api import utils
from typing import List, Optional

class PlaylistType(str, Enum):
    r"""limit to a type of playlist."""
    AUDIO = 'audio'
    VIDEO = 'video'
    PHOTO = 'photo'

class QueryParamSmart(int, Enum):
    r"""type of playlists to return (default is all)."""
    ZERO = 0
    ONE = 1


@dataclasses.dataclass
class GetPlaylistsRequest:
    playlist_type: Optional[PlaylistType] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'playlistType', 'style': 'form', 'explode': True }})
    r"""limit to a type of playlist."""
    smart: Optional[QueryParamSmart] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'smart', 'style': 'form', 'explode': True }})
    r"""type of playlists to return (default is all)."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetPlaylistsMetadata:
    rating_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ratingKey'), 'exclude': lambda f: f is None }})
    key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('key'), 'exclude': lambda f: f is None }})
    guid: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('guid'), 'exclude': lambda f: f is None }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    summary: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('summary'), 'exclude': lambda f: f is None }})
    smart: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('smart'), 'exclude': lambda f: f is None }})
    playlist_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('playlistType'), 'exclude': lambda f: f is None }})
    composite: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('composite'), 'exclude': lambda f: f is None }})
    icon: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('icon'), 'exclude': lambda f: f is None }})
    view_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('viewCount'), 'exclude': lambda f: f is None }})
    last_viewed_at: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lastViewedAt'), 'exclude': lambda f: f is None }})
    duration: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('duration'), 'exclude': lambda f: f is None }})
    leaf_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('leafCount'), 'exclude': lambda f: f is None }})
    added_at: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('addedAt'), 'exclude': lambda f: f is None }})
    updated_at: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetPlaylistsMediaContainer:
    size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('size'), 'exclude': lambda f: f is None }})
    metadata: Optional[List[GetPlaylistsMetadata]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Metadata'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetPlaylistsResponseBody:
    r"""returns all playlists"""
    media_container: Optional[GetPlaylistsMediaContainer] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('MediaContainer'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class GetPlaylistsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: Optional[GetPlaylistsResponseBody] = dataclasses.field(default=None)
    r"""returns all playlists"""
    

