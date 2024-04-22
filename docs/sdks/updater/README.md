# Updater
(*updater*)

## Overview

This describes the API for searching and applying updates to the Plex Media Server.
Updates to the status can be observed via the Event API.


### Available Operations

* [get_update_status](#get_update_status) - Querying status of updates
* [check_for_updates](#check_for_updates) - Checking for updates
* [apply_updates](#apply_updates) - Apply Updates

## get_update_status

Querying status of updates

### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.updater.get_update_status()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.GetUpdateStatusResponse](../../models/operations/getupdatestatusresponse.md)**
### Errors

| Error Object                       | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.GetUpdateStatusResponseBody | 401                                | application/json                   |
| errors.SDKError                    | 4xx-5xx                            | */*                                |

## check_for_updates

Checking for updates

### Example Usage

```python
import plex_api
from plex_api.models import operations

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.updater.check_for_updates(download=operations.Download.ONE)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `download`                                                           | [Optional[operations.Download]](../../models/operations/download.md) | :heavy_minus_sign:                                                   | Indicate that you want to start download any updates found.          |


### Response

**[operations.CheckForUpdatesResponse](../../models/operations/checkforupdatesresponse.md)**
### Errors

| Error Object                       | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.CheckForUpdatesResponseBody | 401                                | application/json                   |
| errors.SDKError                    | 4xx-5xx                            | */*                                |

## apply_updates

Note that these two parameters are effectively mutually exclusive. The `tonight` parameter takes precedence and `skip` will be ignored if `tonight` is also passed


### Example Usage

```python
import plex_api
from plex_api.models import operations

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.updater.apply_updates(tonight=operations.Tonight.ONE, skip=operations.Skip.ZERO)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                | Type                                                                                                                                                     | Required                                                                                                                                                 | Description                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tonight`                                                                                                                                                | [Optional[operations.Tonight]](../../models/operations/tonight.md)                                                                                       | :heavy_minus_sign:                                                                                                                                       | Indicate that you want the update to run during the next Butler execution. Omitting this or setting it to false indicates that the update should install |
| `skip`                                                                                                                                                   | [Optional[operations.Skip]](../../models/operations/skip.md)                                                                                             | :heavy_minus_sign:                                                                                                                                       | Indicate that the latest version should be marked as skipped. The <Release> entry for this version will have the `state` set to `skipped`.               |


### Response

**[operations.ApplyUpdatesResponse](../../models/operations/applyupdatesresponse.md)**
### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ApplyUpdatesResponseBody | 401                             | application/json                |
| errors.SDKError                 | 4xx-5xx                         | */*                             |
