# Watchlist
(*watchlist*)

## Overview

API Calls that perform operations with Plex Media Server Watchlists


### Available Operations

* [get_watch_list](#get_watch_list) - Get User Watchlist

## get_watch_list

Get User Watchlist

### Example Usage

```python
from plex_api_client import PlexAPI
from plex_api_client.models import operations

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier="gcgzw5rz2xovp84b4vha3a40",
)

res = s.watchlist.get_watch_list(request={
    "filter_": operations.Filter.AVAILABLE,
    "x_plex_token": "CV5xoxjTpFKUzBTShsaf",
    "x_plex_container_start": 0,
    "x_plex_container_size": 50,
})

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetWatchListRequest](../../models/operations/getwatchlistrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |
| `server_url`                                                                     | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | An optional server URL to use.                                                   |

### Response

**[operations.GetWatchListResponse](../../models/operations/getwatchlistresponse.md)**

### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.GetWatchListBadRequest   | 400                             | application/json                |
| errors.GetWatchListUnauthorized | 401                             | application/json                |
| errors.SDKError                 | 4xx-5xx                         | */*                             |
