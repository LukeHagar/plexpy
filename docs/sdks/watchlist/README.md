# Watchlist
(*watchlist*)

## Overview

API Calls that perform operations with Plex Media Server Watchlists


### Available Operations

* [get_watchlist](#get_watchlist) - Get User Watchlist

## get_watchlist

Get User Watchlist

### Example Usage

```python
import plex_api
from plex_api.models import operations

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.watchlist.get_watchlist(request=operations.GetWatchlistRequest(
    filter_=operations.Filter.RELEASED,
    x_plex_token='<value>',
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetWatchlistRequest](../../models/operations/getwatchlistrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `server_url`                                                                     | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | An optional server URL to use.                                                   |


### Response

**[operations.GetWatchlistResponse](../../models/operations/getwatchlistresponse.md)**
### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.GetWatchlistResponseBody | 401                             | application/json                |
| errors.SDKError                 | 4xx-5xx                         | */*                             |
