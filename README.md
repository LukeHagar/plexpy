# plexpy

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>

<!-- Start Summary [summary] -->
## Summary

Plex-API: An Open API Spec for interacting with Plex.tv and Plex Media Server

# Plex Media Server OpenAPI Specification

An Open Source OpenAPI Specification for Plex Media Server

Automation and SDKs provided by [Speakeasy](https://speakeasyapi.dev/)

## Documentation

[API Documentation](https://plexapi.dev)

## SDKs

The following SDKs are generated from the OpenAPI Specification. They are automatically generated and may not be fully tested. If you find any issues, please open an issue on the [main specification Repository](https://github.com/LukeHagar/plex-api-spec).

| Language              | Repository                                        | Releases                                                                                         | Other                                                   |
| --------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------- |
| Python                | [GitHub](https://github.com/LukeHagar/plexpy)     | [PyPI](https://pypi.org/project/plex-api-client/)                                                | -                                                       |
| JavaScript/TypeScript | [GitHub](https://github.com/LukeHagar/plexjs)     | [NPM](https://www.npmjs.com/package/@lukehagar/plexjs) \ [JSR](https://jsr.io/@lukehagar/plexjs) | -                                                       |
| Go                    | [GitHub](https://github.com/LukeHagar/plexgo)     | [Releases](https://github.com/LukeHagar/plexgo/releases)                                         | [GoDoc](https://pkg.go.dev/github.com/LukeHagar/plexgo) |
| Ruby                  | [GitHub](https://github.com/LukeHagar/plexruby)   | [Releases](https://github.com/LukeHagar/plexruby/releases)                                       | -                                                       |
| Swift                 | [GitHub](https://github.com/LukeHagar/plexswift)  | [Releases](https://github.com/LukeHagar/plexswift/releases)                                      | -                                                       |
| PHP                   | [GitHub](https://github.com/LukeHagar/plexphp)    | [Releases](https://github.com/LukeHagar/plexphp/releases)                                        | -                                                       |
| Java                  | [GitHub](https://github.com/LukeHagar/plexjava)   | [Releases](https://github.com/LukeHagar/plexjava/releases)                                       | -                                                       |
| C#                    | [GitHub](https://github.com/LukeHagar/plexcsharp) | [Releases](https://github.com/LukeHagar/plexcsharp/releases)                                     | -
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [plexpy](#plexpy)
* [Plex Media Server OpenAPI Specification](#plex-media-server-openapi-specification)
  * [Documentation](#documentation)
  * [SDKs](#sdks)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Authentication](#authentication)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install plex-api-client
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add plex-api-client
```
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from plex_api_client import PlexAPI

with PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.server.get_server_capabilities()

    assert res.object is not None

    # Handle response
    print(res.object)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from plex_api_client import PlexAPI

async def main():
    async with PlexAPI(
        access_token="<YOUR_API_KEY_HERE>",
    ) as plex_api:

        res = await plex_api.server.get_server_capabilities_async()

        assert res.object is not None

        # Handle response
        print(res.object)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [activities](docs/sdks/activities/README.md)

* [get_server_activities](docs/sdks/activities/README.md#get_server_activities) - Get Server Activities
* [cancel_server_activities](docs/sdks/activities/README.md#cancel_server_activities) - Cancel Server Activities

### [authentication](docs/sdks/authentication/README.md)

* [get_transient_token](docs/sdks/authentication/README.md#get_transient_token) - Get a Transient Token
* [get_source_connection_information](docs/sdks/authentication/README.md#get_source_connection_information) - Get Source Connection Information
* [get_token_details](docs/sdks/authentication/README.md#get_token_details) - Get Token Details
* [post_users_sign_in_data](docs/sdks/authentication/README.md#post_users_sign_in_data) - Get User Sign In Data

### [butler](docs/sdks/butler/README.md)

* [get_butler_tasks](docs/sdks/butler/README.md#get_butler_tasks) - Get Butler tasks
* [start_all_tasks](docs/sdks/butler/README.md#start_all_tasks) - Start all Butler tasks
* [stop_all_tasks](docs/sdks/butler/README.md#stop_all_tasks) - Stop all Butler tasks
* [start_task](docs/sdks/butler/README.md#start_task) - Start a single Butler task
* [stop_task](docs/sdks/butler/README.md#stop_task) - Stop a single Butler task

### [hubs](docs/sdks/hubs/README.md)

* [get_global_hubs](docs/sdks/hubs/README.md#get_global_hubs) - Get Global Hubs
* [get_recently_added](docs/sdks/hubs/README.md#get_recently_added) - Get Recently Added
* [get_library_hubs](docs/sdks/hubs/README.md#get_library_hubs) - Get library specific hubs

### [library](docs/sdks/library/README.md)

* [get_file_hash](docs/sdks/library/README.md#get_file_hash) - Get Hash Value
* [get_recently_added_library](docs/sdks/library/README.md#get_recently_added_library) - Get Recently Added
* [get_all_libraries](docs/sdks/library/README.md#get_all_libraries) - Get All Libraries
* [get_library_details](docs/sdks/library/README.md#get_library_details) - Get Library Details
* [delete_library](docs/sdks/library/README.md#delete_library) - Delete Library Section
* [get_library_items](docs/sdks/library/README.md#get_library_items) - Get Library Items
* [get_refresh_library_metadata](docs/sdks/library/README.md#get_refresh_library_metadata) - Refresh Metadata Of The Library
* [get_search_library](docs/sdks/library/README.md#get_search_library) - Search Library
* [get_search_all_libraries](docs/sdks/library/README.md#get_search_all_libraries) - Search All Libraries
* [get_meta_data_by_rating_key](docs/sdks/library/README.md#get_meta_data_by_rating_key) - Get Metadata by RatingKey
* [get_metadata_children](docs/sdks/library/README.md#get_metadata_children) - Get Items Children
* [get_top_watched_content](docs/sdks/library/README.md#get_top_watched_content) - Get Top Watched Content
* [get_on_deck](docs/sdks/library/README.md#get_on_deck) - Get On Deck

### [log](docs/sdks/log/README.md)

* [log_line](docs/sdks/log/README.md#log_line) - Logging a single line message.
* [log_multi_line](docs/sdks/log/README.md#log_multi_line) - Logging a multi-line message
* [enable_paper_trail](docs/sdks/log/README.md#enable_paper_trail) - Enabling Papertrail

### [media](docs/sdks/media/README.md)

* [mark_played](docs/sdks/media/README.md#mark_played) - Mark Media Played
* [mark_unplayed](docs/sdks/media/README.md#mark_unplayed) - Mark Media Unplayed
* [update_play_progress](docs/sdks/media/README.md#update_play_progress) - Update Media Play Progress
* [get_banner_image](docs/sdks/media/README.md#get_banner_image) - Get Banner Image
* [get_thumb_image](docs/sdks/media/README.md#get_thumb_image) - Get Thumb Image

### [playlists](docs/sdks/playlists/README.md)

* [create_playlist](docs/sdks/playlists/README.md#create_playlist) - Create a Playlist
* [get_playlists](docs/sdks/playlists/README.md#get_playlists) - Get All Playlists
* [get_playlist](docs/sdks/playlists/README.md#get_playlist) - Retrieve Playlist
* [delete_playlist](docs/sdks/playlists/README.md#delete_playlist) - Deletes a Playlist
* [update_playlist](docs/sdks/playlists/README.md#update_playlist) - Update a Playlist
* [get_playlist_contents](docs/sdks/playlists/README.md#get_playlist_contents) - Retrieve Playlist Contents
* [clear_playlist_contents](docs/sdks/playlists/README.md#clear_playlist_contents) - Delete Playlist Contents
* [add_playlist_contents](docs/sdks/playlists/README.md#add_playlist_contents) - Adding to a Playlist
* [upload_playlist](docs/sdks/playlists/README.md#upload_playlist) - Upload Playlist

### [plex](docs/sdks/plex/README.md)

* [get_companions_data](docs/sdks/plex/README.md#get_companions_data) - Get Companions Data
* [get_user_friends](docs/sdks/plex/README.md#get_user_friends) - Get list of friends of the user logged in
* [get_geo_data](docs/sdks/plex/README.md#get_geo_data) - Get Geo Data
* [get_home_data](docs/sdks/plex/README.md#get_home_data) - Get Plex Home Data
* [get_server_resources](docs/sdks/plex/README.md#get_server_resources) - Get Server Resources
* [get_pin](docs/sdks/plex/README.md#get_pin) - Get a Pin
* [get_token_by_pin_id](docs/sdks/plex/README.md#get_token_by_pin_id) - Get Access Token by PinId


### [search](docs/sdks/search/README.md)

* [perform_search](docs/sdks/search/README.md#perform_search) - Perform a search
* [perform_voice_search](docs/sdks/search/README.md#perform_voice_search) - Perform a voice search
* [get_search_results](docs/sdks/search/README.md#get_search_results) - Get Search Results

### [server](docs/sdks/server/README.md)

* [get_server_capabilities](docs/sdks/server/README.md#get_server_capabilities) - Get Server Capabilities
* [get_server_preferences](docs/sdks/server/README.md#get_server_preferences) - Get Server Preferences
* [get_available_clients](docs/sdks/server/README.md#get_available_clients) - Get Available Clients
* [get_devices](docs/sdks/server/README.md#get_devices) - Get Devices
* [get_server_identity](docs/sdks/server/README.md#get_server_identity) - Get Server Identity
* [get_my_plex_account](docs/sdks/server/README.md#get_my_plex_account) - Get MyPlex Account
* [get_resized_photo](docs/sdks/server/README.md#get_resized_photo) - Get a Resized Photo
* [get_media_providers](docs/sdks/server/README.md#get_media_providers) - Get Media Providers
* [get_server_list](docs/sdks/server/README.md#get_server_list) - Get Server List

### [sessions](docs/sdks/sessions/README.md)

* [get_sessions](docs/sdks/sessions/README.md#get_sessions) - Get Active Sessions
* [get_session_history](docs/sdks/sessions/README.md#get_session_history) - Get Session History
* [get_transcode_sessions](docs/sdks/sessions/README.md#get_transcode_sessions) - Get Transcode Sessions
* [stop_transcode_session](docs/sdks/sessions/README.md#stop_transcode_session) - Stop a Transcode Session

### [statistics](docs/sdks/statistics/README.md)

* [get_statistics](docs/sdks/statistics/README.md#get_statistics) - Get Media Statistics
* [get_resources_statistics](docs/sdks/statistics/README.md#get_resources_statistics) - Get Resources Statistics
* [get_bandwidth_statistics](docs/sdks/statistics/README.md#get_bandwidth_statistics) - Get Bandwidth Statistics

### [updater](docs/sdks/updater/README.md)

* [get_update_status](docs/sdks/updater/README.md#get_update_status) - Querying status of updates
* [check_for_updates](docs/sdks/updater/README.md#check_for_updates) - Checking for updates
* [apply_updates](docs/sdks/updater/README.md#apply_updates) - Apply Updates

### [video](docs/sdks/video/README.md)

* [get_timeline](docs/sdks/video/README.md#get_timeline) - Get the timeline for a media item
* [start_universal_transcode](docs/sdks/video/README.md#start_universal_transcode) - Start Universal Transcode

### [watchlist](docs/sdks/watchlist/README.md)

* [get_watch_list](docs/sdks/watchlist/README.md#get_watch_list) - Get User Watchlist

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from plex_api_client import PlexAPI
from plex_api_client.utils import BackoffStrategy, RetryConfig

with PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.server.get_server_capabilities(,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    assert res.object is not None

    # Handle response
    print(res.object)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from plex_api_client import PlexAPI
from plex_api_client.utils import BackoffStrategy, RetryConfig

with PlexAPI(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.server.get_server_capabilities()

    assert res.object is not None

    # Handle response
    print(res.object)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a errors.SDKError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `get_server_capabilities_async` method may raise the following exceptions:

| Error Type                               | Status Code | Content Type     |
| ---------------------------------------- | ----------- | ---------------- |
| errors.GetServerCapabilitiesBadRequest   | 400         | application/json |
| errors.GetServerCapabilitiesUnauthorized | 401         | application/json |
| errors.SDKError                          | 4XX, 5XX    | \*/\*            |

### Example

```python
from plex_api_client import PlexAPI
from plex_api_client.models import errors

with PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:
    res = None
    try:

        res = plex_api.server.get_server_capabilities()

        assert res.object is not None

        # Handle response
        print(res.object)

    except errors.GetServerCapabilitiesBadRequest as e:
        # handle e.data: errors.GetServerCapabilitiesBadRequestData
        raise(e)
    except errors.GetServerCapabilitiesUnauthorized as e:
        # handle e.data: errors.GetServerCapabilitiesUnauthorizedData
        raise(e)
    except errors.SDKError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Server Variables

The default server `{protocol}://{ip}:{port}` contains variables and is set to `https://10.10.10.47:32400` by default. To override default values, the following parameters are available when initializing the SDK client instance:
 * `protocol: models.ServerProtocol`
 * `ip: str`
 * `port: str`

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from plex_api_client import PlexAPI

with PlexAPI(
    server_url="https://10.10.10.47:32400",
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.server.get_server_capabilities()

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Override Server URL Per-Operation

The server URL can also be overridden on a per-operation basis, provided a server list was specified for the operation. For example:
```python
from plex_api_client import PlexAPI

with PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.plex.get_companions_data(server_url="https://plex.tv/api/v2")

    assert res.response_bodies is not None

    # Handle response
    print(res.response_bodies)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from plex_api_client import PlexAPI
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = PlexAPI(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from plex_api_client import PlexAPI
from plex_api_client.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = PlexAPI(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name           | Type   | Scheme  |
| -------------- | ------ | ------- |
| `access_token` | apiKey | API key |

To authenticate with the API the `access_token` parameter must be set when initializing the SDK client instance. For example:
```python
from plex_api_client import PlexAPI

with PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.server.get_server_capabilities()

    assert res.object is not None

    # Handle response
    print(res.object)

```
<!-- End Authentication [security] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from plex_api_client import PlexAPI
import logging

logging.basicConfig(level=logging.DEBUG)
s = PlexAPI(debug_logger=logging.getLogger("plex_api_client"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
