"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from plex_api_client.types import BaseModel
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ContextTypedDict(TypedDict):
    library_section_id: NotRequired[str]


class Context(BaseModel):
    library_section_id: Annotated[
        Optional[str], pydantic.Field(alias="librarySectionID")
    ] = None


class ActivityTypedDict(TypedDict):
    uuid: NotRequired[str]
    type: NotRequired[str]
    cancellable: NotRequired[bool]
    user_id: NotRequired[float]
    title: NotRequired[str]
    subtitle: NotRequired[str]
    progress: NotRequired[float]
    context: NotRequired[ContextTypedDict]


class Activity(BaseModel):
    uuid: Optional[str] = None

    type: Optional[str] = None

    cancellable: Optional[bool] = None

    user_id: Annotated[Optional[float], pydantic.Field(alias="userID")] = None

    title: Optional[str] = None

    subtitle: Optional[str] = None

    progress: Optional[float] = None

    context: Annotated[Optional[Context], pydantic.Field(alias="Context")] = None


class GetServerActivitiesMediaContainerTypedDict(TypedDict):
    size: NotRequired[float]
    activity: NotRequired[List[ActivityTypedDict]]


class GetServerActivitiesMediaContainer(BaseModel):
    size: Optional[float] = None

    activity: Annotated[Optional[List[Activity]], pydantic.Field(alias="Activity")] = (
        None
    )


class GetServerActivitiesResponseBodyTypedDict(TypedDict):
    r"""The Server Activities"""

    media_container: NotRequired[GetServerActivitiesMediaContainerTypedDict]


class GetServerActivitiesResponseBody(BaseModel):
    r"""The Server Activities"""

    media_container: Annotated[
        Optional[GetServerActivitiesMediaContainer],
        pydantic.Field(alias="MediaContainer"),
    ] = None


class GetServerActivitiesResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[GetServerActivitiesResponseBodyTypedDict]
    r"""The Server Activities"""


class GetServerActivitiesResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[GetServerActivitiesResponseBody] = None
    r"""The Server Activities"""