"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from plex_api_client import utils
from plex_api_client._hooks import HookContext
from plex_api_client.models import errors, operations
from plex_api_client.types import BaseModel, OptionalNullable, UNSET
from typing import Any, Optional, Union, cast


class Watchlist(BaseSDK):
    r"""API Calls that perform operations with Plex Media Server Watchlists"""

    def get_watch_list(
        self,
        *,
        request: Union[
            operations.GetWatchListRequest, operations.GetWatchListRequestTypedDict
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.GetWatchListResponse:
        r"""Get User Watchlist

        Get User Watchlist

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
        else:
            base_url = operations.GET_WATCH_LIST_SERVERS[0]

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.GetWatchListRequest)
        request = cast(operations.GetWatchListRequest, request)

        req = self.build_request(
            method="GET",
            path="/library/sections/watchlist/{filter}",
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
                operation_id="get-watch-list",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["400", "401", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return operations.GetWatchListResponse(
                object=utils.unmarshal_json(
                    http_res.text, Optional[operations.GetWatchListResponseBody]
                ),
                status_code=http_res.status_code,
                content_type=http_res.headers.get("Content-Type") or "",
                raw_response=http_res,
            )
        if utils.match_response(http_res, "400", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, errors.GetWatchListBadRequestData
            )
            data.raw_response = http_res
            raise errors.GetWatchListBadRequest(data=data)
        if utils.match_response(http_res, "401", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, errors.GetWatchListUnauthorizedData
            )
            data.raw_response = http_res
            raise errors.GetWatchListUnauthorized(data=data)
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

    async def get_watch_list_async(
        self,
        *,
        request: Union[
            operations.GetWatchListRequest, operations.GetWatchListRequestTypedDict
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.GetWatchListResponse:
        r"""Get User Watchlist

        Get User Watchlist

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
        else:
            base_url = operations.GET_WATCH_LIST_SERVERS[0]

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.GetWatchListRequest)
        request = cast(operations.GetWatchListRequest, request)

        req = self.build_request_async(
            method="GET",
            path="/library/sections/watchlist/{filter}",
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
                operation_id="get-watch-list",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["400", "401", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return operations.GetWatchListResponse(
                object=utils.unmarshal_json(
                    http_res.text, Optional[operations.GetWatchListResponseBody]
                ),
                status_code=http_res.status_code,
                content_type=http_res.headers.get("Content-Type") or "",
                raw_response=http_res,
            )
        if utils.match_response(http_res, "400", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, errors.GetWatchListBadRequestData
            )
            data.raw_response = http_res
            raise errors.GetWatchListBadRequest(data=data)
        if utils.match_response(http_res, "401", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, errors.GetWatchListUnauthorizedData
            )
            data.raw_response = http_res
            raise errors.GetWatchListUnauthorized(data=data)
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
