"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from enum import Enum

class Level(int, Enum):
    r"""An integer log level to write to the PMS log with.
    0: Error  
    1: Warning  
    2: Info  
    3: Debug  
    4: Verbose
    """
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4


@dataclasses.dataclass
class LogLineRequest:
    level: Level = dataclasses.field(metadata={'query_param': { 'field_name': 'level', 'style': 'form', 'explode': True }})
    r"""An integer log level to write to the PMS log with.
    0: Error  
    1: Warning  
    2: Info  
    3: Debug  
    4: Verbose
    """
    message: str = dataclasses.field(metadata={'query_param': { 'field_name': 'message', 'style': 'form', 'explode': True }})
    r"""The text of the message to write to the log."""
    source: str = dataclasses.field(metadata={'query_param': { 'field_name': 'source', 'style': 'form', 'explode': True }})
    r"""a string indicating the source of the message."""
    



@dataclasses.dataclass
class LogLineResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    

