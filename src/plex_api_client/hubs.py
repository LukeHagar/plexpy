"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from plex_api_client import utils
from plex_api_client._hooks import HookContext
from plex_api_client.models import errors, operations
from plex_api_client.types import BaseModel, OptionalNullable, UNSET
from typing import Any, Optional, Union, cast


class Hubs(BaseSDK):
    r"""Hubs are a structured two-dimensional container for media, generally represented by multiple horizontal rows."""

    def get_global_hubs(
        self,
        *,
        count: Optional[float] = None,
        only_transient: Optional[operations.OnlyTransient] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.GetGlobalHubsResponse:
        r"""Get Global Hubs

        Get Global Hubs filtered by the parameters provided.

        :param count: The number of items to return with each hub.
        :param only_transient: Only return hubs which are \"transient\", meaning those which are prone to changing after media playback or addition (e.g. On Deck, or Recently Added).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = operations.GetGlobalHubsRequest(
            count=count,
            only_transient=only_transient,
        )

        req = self.build_request(
            method="GET",
            path="/hubs",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="getGlobalHubs",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["400", "401", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return operations.GetGlobalHubsResponse(
                object=utils.unmarshal_json(
                    http_res.text, Optional[operations.GetGlobalHubsResponseBody]
                ),
                status_code=http_res.status_code,
                content_type=http_res.headers.get("Content-Type") or "",
                raw_response=http_res,
            )
        if utils.match_response(http_res, "400", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, errors.GetGlobalHubsBadRequestData
            )
            data.raw_response = http_res
            raise errors.GetGlobalHubsBadRequest(data=data)
        if utils.match_response(http_res, "401", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, errors.GetGlobalHubsUnauthorizedData
            )
            data.raw_response = http_res
            raise errors.GetGlobalHubsUnauthorized(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )

    async def get_global_hubs_async(
        self,
        *,
        count: Optional[float] = None,
        only_transient: Optional[operations.OnlyTransient] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.GetGlobalHubsResponse:
        r"""Get Global Hubs

        Get Global Hubs filtered by the parameters provided.

        :param count: The number of items to return with each hub.
        :param only_transient: Only return hubs which are \"transient\", meaning those which are prone to changing after media playback or addition (e.g. On Deck, or Recently Added).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = operations.GetGlobalHubsRequest(
            count=count,
            only_transient=only_transient,
        )

        req = self.build_request_async(
            method="GET",
            path="/hubs",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="getGlobalHubs",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["400", "401", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return operations.GetGlobalHubsResponse(
                object=utils.unmarshal_json(
                    http_res.text, Optional[operations.GetGlobalHubsResponseBody]
                ),
                status_code=http_res.status_code,
                content_type=http_res.headers.get("Content-Type") or "",
                raw_response=http_res,
            )
        if utils.match_response(http_res, "400", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, errors.GetGlobalHubsBadRequestData
            )
            data.raw_response = http_res
            raise errors.GetGlobalHubsBadRequest(data=data)
        if utils.match_response(http_res, "401", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, errors.GetGlobalHubsUnauthorizedData
            )
            data.raw_response = http_res
            raise errors.GetGlobalHubsUnauthorized(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )

    def get_recently_added(
        self,
        *,
        request: Union[
            operations.GetRecentlyAddedRequest,
            operations.GetRecentlyAddedRequestTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.GetRecentlyAddedResponse:
        r"""Get Recently Added

        This endpoint will return the recently added content.


        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.GetRecentlyAddedRequest)
        request = cast(operations.GetRecentlyAddedRequest, request)

        req = self.build_request(
            method="GET",
            path="/hubs/home/recentlyAdded",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="get-recently-added",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["400", "401", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return operations.GetRecentlyAddedResponse(
                object=utils.unmarshal_json(
                    http_res.text, Optional[operations.GetRecentlyAddedResponseBody]
                ),
                status_code=http_res.status_code,
                content_type=http_res.headers.get("Content-Type") or "",
                raw_response=http_res,
            )
        if utils.match_response(http_res, ["400", "401", "4XX", "5XX"], "*"):
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )

    async def get_recently_added_async(
        self,
        *,
        request: Union[
            operations.GetRecentlyAddedRequest,
            operations.GetRecentlyAddedRequestTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.GetRecentlyAddedResponse:
        r"""Get Recently Added

        This endpoint will return the recently added content.


        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.GetRecentlyAddedRequest)
        request = cast(operations.GetRecentlyAddedRequest, request)

        req = self.build_request_async(
            method="GET",
            path="/hubs/home/recentlyAdded",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="get-recently-added",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["400", "401", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return operations.GetRecentlyAddedResponse(
                object=utils.unmarshal_json(
                    http_res.text, Optional[operations.GetRecentlyAddedResponseBody]
                ),
                status_code=http_res.status_code,
                content_type=http_res.headers.get("Content-Type") or "",
                raw_response=http_res,
            )
        if utils.match_response(http_res, ["400", "401", "4XX", "5XX"], "*"):
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )

    def get_library_hubs(
        self,
        *,
        section_id: float,
        count: Optional[float] = None,
        only_transient: Optional[operations.QueryParamOnlyTransient] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.GetLibraryHubsResponse:
        r"""Get library specific hubs

        This endpoint will return a list of library specific hubs


        :param section_id: the Id of the library to query
        :param count: The number of items to return with each hub.
        :param only_transient: Only return hubs which are \"transient\", meaning those which are prone to changing after media playback or addition (e.g. On Deck, or Recently Added).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = operations.GetLibraryHubsRequest(
            section_id=section_id,
            count=count,
            only_transient=only_transient,
        )

        req = self.build_request(
            method="GET",
            path="/hubs/sections/{sectionId}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="getLibraryHubs",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["400", "401", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return operations.GetLibraryHubsResponse(
                object=utils.unmarshal_json(
                    http_res.text, Optional[operations.GetLibraryHubsResponseBody]
                ),
                status_code=http_res.status_code,
                content_type=http_res.headers.get("Content-Type") or "",
                raw_response=http_res,
            )
        if utils.match_response(http_res, "400", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, errors.GetLibraryHubsBadRequestData
            )
            data.raw_response = http_res
            raise errors.GetLibraryHubsBadRequest(data=data)
        if utils.match_response(http_res, "401", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, errors.GetLibraryHubsUnauthorizedData
            )
            data.raw_response = http_res
            raise errors.GetLibraryHubsUnauthorized(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )

    async def get_library_hubs_async(
        self,
        *,
        section_id: float,
        count: Optional[float] = None,
        only_transient: Optional[operations.QueryParamOnlyTransient] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.GetLibraryHubsResponse:
        r"""Get library specific hubs

        This endpoint will return a list of library specific hubs


        :param section_id: the Id of the library to query
        :param count: The number of items to return with each hub.
        :param only_transient: Only return hubs which are \"transient\", meaning those which are prone to changing after media playback or addition (e.g. On Deck, or Recently Added).
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = operations.GetLibraryHubsRequest(
            section_id=section_id,
            count=count,
            only_transient=only_transient,
        )

        req = self.build_request_async(
            method="GET",
            path="/hubs/sections/{sectionId}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="getLibraryHubs",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["400", "401", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return operations.GetLibraryHubsResponse(
                object=utils.unmarshal_json(
                    http_res.text, Optional[operations.GetLibraryHubsResponseBody]
                ),
                status_code=http_res.status_code,
                content_type=http_res.headers.get("Content-Type") or "",
                raw_response=http_res,
            )
        if utils.match_response(http_res, "400", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, errors.GetLibraryHubsBadRequestData
            )
            data.raw_response = http_res
            raise errors.GetLibraryHubsBadRequest(data=data)
        if utils.match_response(http_res, "401", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, errors.GetLibraryHubsUnauthorizedData
            )
            data.raw_response = http_res
            raise errors.GetLibraryHubsUnauthorized(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )