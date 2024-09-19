# Hubs
(*hubs*)

## Overview

Hubs are a structured two-dimensional container for media, generally represented by multiple horizontal rows.


### Available Operations

* [get_global_hubs](#get_global_hubs) - Get Global Hubs
* [get_library_hubs](#get_library_hubs) - Get library specific hubs

## get_global_hubs

Get Global Hubs filtered by the parameters provided.

### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    client_id="gcgzw5rz2xovp84b4vha3a40",
    client_name="Plex Web",
    client_version="4.133.0",
    client_platform="Chrome",
    device_name="Linux",
)

res = s.hubs.get_global_hubs()

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                             | Type                                                                                                                                                  | Required                                                                                                                                              | Description                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `count`                                                                                                                                               | *Optional[float]*                                                                                                                                     | :heavy_minus_sign:                                                                                                                                    | The number of items to return with each hub.                                                                                                          |
| `only_transient`                                                                                                                                      | [Optional[operations.OnlyTransient]](../../models/operations/onlytransient.md)                                                                        | :heavy_minus_sign:                                                                                                                                    | Only return hubs which are "transient", meaning those which are prone to changing after media playback or addition (e.g. On Deck, or Recently Added). |
| `retries`                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                      | :heavy_minus_sign:                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                   |

### Response

**[operations.GetGlobalHubsResponse](../../models/operations/getglobalhubsresponse.md)**

### Errors

| Error Object                     | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.GetGlobalHubsBadRequest   | 400                              | application/json                 |
| errors.GetGlobalHubsUnauthorized | 401                              | application/json                 |
| errors.SDKError                  | 4xx-5xx                          | */*                              |


## get_library_hubs

This endpoint will return a list of library specific hubs


### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    client_id="gcgzw5rz2xovp84b4vha3a40",
    client_name="Plex Web",
    client_version="4.133.0",
    client_platform="Chrome",
    device_name="Linux",
)

res = s.hubs.get_library_hubs(section_id=6728.76)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                             | Type                                                                                                                                                  | Required                                                                                                                                              | Description                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `section_id`                                                                                                                                          | *float*                                                                                                                                               | :heavy_check_mark:                                                                                                                                    | the Id of the library to query                                                                                                                        |
| `count`                                                                                                                                               | *Optional[float]*                                                                                                                                     | :heavy_minus_sign:                                                                                                                                    | The number of items to return with each hub.                                                                                                          |
| `only_transient`                                                                                                                                      | [Optional[operations.QueryParamOnlyTransient]](../../models/operations/queryparamonlytransient.md)                                                    | :heavy_minus_sign:                                                                                                                                    | Only return hubs which are "transient", meaning those which are prone to changing after media playback or addition (e.g. On Deck, or Recently Added). |
| `retries`                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                      | :heavy_minus_sign:                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                   |

### Response

**[operations.GetLibraryHubsResponse](../../models/operations/getlibraryhubsresponse.md)**

### Errors

| Error Object                      | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.GetLibraryHubsBadRequest   | 400                               | application/json                  |
| errors.GetLibraryHubsUnauthorized | 401                               | application/json                  |
| errors.SDKError                   | 4xx-5xx                           | */*                               |
