"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from plex_api_client.types import BaseModel
from plex_api_client.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetResourcesStatisticsRequestTypedDict(TypedDict):
    timespan: NotRequired[int]
    r"""The timespan to retrieve statistics for
    the exact meaning of this parameter is not known

    """


class GetResourcesStatisticsRequest(BaseModel):
    timespan: Annotated[
        Optional[int],
        pydantic.Field(alias="Timespan"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The timespan to retrieve statistics for
    the exact meaning of this parameter is not known

    """


class StatisticsResourcesTypedDict(TypedDict):
    timespan: NotRequired[int]
    at: NotRequired[int]
    host_cpu_utilization: NotRequired[float]
    process_cpu_utilization: NotRequired[float]
    host_memory_utilization: NotRequired[float]
    process_memory_utilization: NotRequired[float]


class StatisticsResources(BaseModel):
    timespan: Optional[int] = None

    at: Optional[int] = None

    host_cpu_utilization: Annotated[
        Optional[float], pydantic.Field(alias="hostCpuUtilization")
    ] = None

    process_cpu_utilization: Annotated[
        Optional[float], pydantic.Field(alias="processCpuUtilization")
    ] = None

    host_memory_utilization: Annotated[
        Optional[float], pydantic.Field(alias="hostMemoryUtilization")
    ] = None

    process_memory_utilization: Annotated[
        Optional[float], pydantic.Field(alias="processMemoryUtilization")
    ] = None


class GetResourcesStatisticsMediaContainerTypedDict(TypedDict):
    size: NotRequired[int]
    statistics_resources: NotRequired[List[StatisticsResourcesTypedDict]]


class GetResourcesStatisticsMediaContainer(BaseModel):
    size: Optional[int] = None

    statistics_resources: Annotated[
        Optional[List[StatisticsResources]], pydantic.Field(alias="StatisticsResources")
    ] = None


class GetResourcesStatisticsResponseBodyTypedDict(TypedDict):
    r"""Resource Statistics"""

    media_container: NotRequired[GetResourcesStatisticsMediaContainerTypedDict]


class GetResourcesStatisticsResponseBody(BaseModel):
    r"""Resource Statistics"""

    media_container: Annotated[
        Optional[GetResourcesStatisticsMediaContainer],
        pydantic.Field(alias="MediaContainer"),
    ] = None


class GetResourcesStatisticsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[GetResourcesStatisticsResponseBodyTypedDict]
    r"""Resource Statistics"""


class GetResourcesStatisticsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[GetResourcesStatisticsResponseBody] = None
    r"""Resource Statistics"""
