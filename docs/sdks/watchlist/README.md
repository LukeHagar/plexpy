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


with PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.watchlist.get_watch_list(request={
        "filter_": operations.Filter.AVAILABLE,
        "x_plex_token": "CV5xoxjTpFKUzBTShsaf",
    })

    assert res.object is not None

    # Handle response
    print(res.object)

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

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.GetWatchListBadRequest   | 400                             | application/json                |
| errors.GetWatchListUnauthorized | 401                             | application/json                |
| errors.SDKError                 | 4XX, 5XX                        | \*/\*                           |