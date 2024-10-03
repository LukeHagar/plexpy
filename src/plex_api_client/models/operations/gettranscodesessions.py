"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from plex_api_client.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class TranscodeSessionTypedDict(TypedDict):
    key: NotRequired[str]
    throttled: NotRequired[bool]
    complete: NotRequired[bool]
    progress: NotRequired[float]
    size: NotRequired[int]
    speed: NotRequired[float]
    error: NotRequired[bool]
    duration: NotRequired[int]
    remaining: NotRequired[int]
    context: NotRequired[str]
    source_video_codec: NotRequired[str]
    source_audio_codec: NotRequired[str]
    video_decision: NotRequired[str]
    audio_decision: NotRequired[str]
    subtitle_decision: NotRequired[str]
    protocol: NotRequired[str]
    container: NotRequired[str]
    video_codec: NotRequired[str]
    audio_codec: NotRequired[str]
    audio_channels: NotRequired[int]
    transcode_hw_requested: NotRequired[bool]
    time_stamp: NotRequired[float]
    max_offset_available: NotRequired[float]
    min_offset_available: NotRequired[float]


class TranscodeSession(BaseModel):
    key: Optional[str] = None

    throttled: Optional[bool] = None

    complete: Optional[bool] = None

    progress: Optional[float] = None

    size: Optional[int] = None

    speed: Optional[float] = None

    error: Optional[bool] = None

    duration: Optional[int] = None

    remaining: Optional[int] = None

    context: Optional[str] = None

    source_video_codec: Annotated[
        Optional[str], pydantic.Field(alias="sourceVideoCodec")
    ] = None

    source_audio_codec: Annotated[
        Optional[str], pydantic.Field(alias="sourceAudioCodec")
    ] = None

    video_decision: Annotated[Optional[str], pydantic.Field(alias="videoDecision")] = (
        None
    )

    audio_decision: Annotated[Optional[str], pydantic.Field(alias="audioDecision")] = (
        None
    )

    subtitle_decision: Annotated[
        Optional[str], pydantic.Field(alias="subtitleDecision")
    ] = None

    protocol: Optional[str] = None

    container: Optional[str] = None

    video_codec: Annotated[Optional[str], pydantic.Field(alias="videoCodec")] = None

    audio_codec: Annotated[Optional[str], pydantic.Field(alias="audioCodec")] = None

    audio_channels: Annotated[Optional[int], pydantic.Field(alias="audioChannels")] = (
        None
    )

    transcode_hw_requested: Annotated[
        Optional[bool], pydantic.Field(alias="transcodeHwRequested")
    ] = None

    time_stamp: Annotated[Optional[float], pydantic.Field(alias="timeStamp")] = None

    max_offset_available: Annotated[
        Optional[float], pydantic.Field(alias="maxOffsetAvailable")
    ] = None

    min_offset_available: Annotated[
        Optional[float], pydantic.Field(alias="minOffsetAvailable")
    ] = None


class GetTranscodeSessionsMediaContainerTypedDict(TypedDict):
    size: NotRequired[int]
    transcode_session: NotRequired[List[TranscodeSessionTypedDict]]


class GetTranscodeSessionsMediaContainer(BaseModel):
    size: Optional[int] = None

    transcode_session: Annotated[
        Optional[List[TranscodeSession]], pydantic.Field(alias="TranscodeSession")
    ] = None


class GetTranscodeSessionsResponseBodyTypedDict(TypedDict):
    r"""The Transcode Sessions"""

    media_container: NotRequired[GetTranscodeSessionsMediaContainerTypedDict]


class GetTranscodeSessionsResponseBody(BaseModel):
    r"""The Transcode Sessions"""

    media_container: Annotated[
        Optional[GetTranscodeSessionsMediaContainer],
        pydantic.Field(alias="MediaContainer"),
    ] = None


class GetTranscodeSessionsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[GetTranscodeSessionsResponseBodyTypedDict]
    r"""The Transcode Sessions"""


class GetTranscodeSessionsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[GetTranscodeSessionsResponseBody] = None
    r"""The Transcode Sessions"""
