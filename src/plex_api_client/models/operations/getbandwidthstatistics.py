"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from plex_api_client.types import BaseModel
from plex_api_client.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetBandwidthStatisticsRequestTypedDict(TypedDict):
    timespan: NotRequired[int]
    r"""The timespan to retrieve statistics for
    the exact meaning of this parameter is not known

    """


class GetBandwidthStatisticsRequest(BaseModel):
    timespan: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The timespan to retrieve statistics for
    the exact meaning of this parameter is not known

    """


class GetBandwidthStatisticsDeviceTypedDict(TypedDict):
    id: NotRequired[int]
    name: NotRequired[str]
    platform: NotRequired[str]
    client_identifier: NotRequired[str]
    created_at: NotRequired[int]


class GetBandwidthStatisticsDevice(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None

    platform: Optional[str] = None

    client_identifier: Annotated[
        Optional[str], pydantic.Field(alias="clientIdentifier")
    ] = None

    created_at: Annotated[Optional[int], pydantic.Field(alias="createdAt")] = None


class GetBandwidthStatisticsAccountTypedDict(TypedDict):
    id: NotRequired[int]
    key: NotRequired[str]
    name: NotRequired[str]
    default_audio_language: NotRequired[str]
    auto_select_audio: NotRequired[bool]
    default_subtitle_language: NotRequired[str]
    subtitle_mode: NotRequired[int]
    thumb: NotRequired[str]


class GetBandwidthStatisticsAccount(BaseModel):
    id: Optional[int] = None

    key: Optional[str] = None

    name: Optional[str] = None

    default_audio_language: Annotated[
        Optional[str], pydantic.Field(alias="defaultAudioLanguage")
    ] = None

    auto_select_audio: Annotated[
        Optional[bool], pydantic.Field(alias="autoSelectAudio")
    ] = None

    default_subtitle_language: Annotated[
        Optional[str], pydantic.Field(alias="defaultSubtitleLanguage")
    ] = None

    subtitle_mode: Annotated[Optional[int], pydantic.Field(alias="subtitleMode")] = None

    thumb: Optional[str] = None


class StatisticsBandwidthTypedDict(TypedDict):
    account_id: NotRequired[int]
    device_id: NotRequired[int]
    timespan: NotRequired[int]
    at: NotRequired[int]
    lan: NotRequired[bool]
    bytes_: NotRequired[int]


class StatisticsBandwidth(BaseModel):
    account_id: Annotated[Optional[int], pydantic.Field(alias="accountID")] = None

    device_id: Annotated[Optional[int], pydantic.Field(alias="deviceID")] = None

    timespan: Optional[int] = None

    at: Optional[int] = None

    lan: Optional[bool] = None

    bytes_: Annotated[Optional[int], pydantic.Field(alias="bytes")] = None


class GetBandwidthStatisticsMediaContainerTypedDict(TypedDict):
    size: NotRequired[int]
    device: NotRequired[List[GetBandwidthStatisticsDeviceTypedDict]]
    account: NotRequired[List[GetBandwidthStatisticsAccountTypedDict]]
    statistics_bandwidth: NotRequired[List[StatisticsBandwidthTypedDict]]


class GetBandwidthStatisticsMediaContainer(BaseModel):
    size: Optional[int] = None

    device: Annotated[
        Optional[List[GetBandwidthStatisticsDevice]], pydantic.Field(alias="Device")
    ] = None

    account: Annotated[
        Optional[List[GetBandwidthStatisticsAccount]], pydantic.Field(alias="Account")
    ] = None

    statistics_bandwidth: Annotated[
        Optional[List[StatisticsBandwidth]], pydantic.Field(alias="StatisticsBandwidth")
    ] = None


class GetBandwidthStatisticsResponseBodyTypedDict(TypedDict):
    r"""Bandwidth Statistics"""

    media_container: NotRequired[GetBandwidthStatisticsMediaContainerTypedDict]


class GetBandwidthStatisticsResponseBody(BaseModel):
    r"""Bandwidth Statistics"""

    media_container: Annotated[
        Optional[GetBandwidthStatisticsMediaContainer],
        pydantic.Field(alias="MediaContainer"),
    ] = None


class GetBandwidthStatisticsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[GetBandwidthStatisticsResponseBodyTypedDict]
    r"""Bandwidth Statistics"""


class GetBandwidthStatisticsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[GetBandwidthStatisticsResponseBody] = None
    r"""Bandwidth Statistics"""
