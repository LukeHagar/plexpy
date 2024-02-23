"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from enum import Enum
from typing import Optional

class Tonight(int, Enum):
    r"""Indicate that you want the update to run during the next Butler execution. Omitting this or setting it to false indicates that the update should install"""
    ZERO = 0
    ONE = 1

class Skip(int, Enum):
    r"""Indicate that the latest version should be marked as skipped. The <Release> entry for this version will have the `state` set to `skipped`."""
    ZERO = 0
    ONE = 1


@dataclasses.dataclass
class ApplyUpdatesRequest:
    tonight: Optional[Tonight] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'tonight', 'style': 'form', 'explode': True }})
    r"""Indicate that you want the update to run during the next Butler execution. Omitting this or setting it to false indicates that the update should install"""
    skip: Optional[Skip] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'skip', 'style': 'form', 'explode': True }})
    r"""Indicate that the latest version should be marked as skipped. The <Release> entry for this version will have the `state` set to `skipped`."""
    



@dataclasses.dataclass
class ApplyUpdatesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    

