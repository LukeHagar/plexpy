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
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    client_id="gcgzw5rz2xovp84b4vha3a40",
    client_name="Plex Web",
    client_version="4.133.0",
    client_platform="Chrome",
    device_name="Linux",
)

res = s.updater.get_update_status()

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetUpdateStatusResponse](../../models/operations/getupdatestatusresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.GetUpdateStatusBadRequest   | 400                                | application/json                   |
| errors.GetUpdateStatusUnauthorized | 401                                | application/json                   |
| errors.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## check_for_updates

Checking for updates

### Example Usage

```python
from plex_api_client import PlexAPI
from plex_api_client.models import operations

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    client_id="gcgzw5rz2xovp84b4vha3a40",
    client_name="Plex Web",
    client_version="4.133.0",
    client_platform="Chrome",
    device_name="Linux",
)

res = s.updater.check_for_updates(download=operations.Download.ONE)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `download`                                                           | [Optional[operations.Download]](../../models/operations/download.md) | :heavy_minus_sign:                                                   | Indicate that you want to start download any updates found.          | 1                                                                    |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |                                                                      |

### Response

**[operations.CheckForUpdatesResponse](../../models/operations/checkforupdatesresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.CheckForUpdatesBadRequest   | 400                                | application/json                   |
| errors.CheckForUpdatesUnauthorized | 401                                | application/json                   |
| errors.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## apply_updates

Note that these two parameters are effectively mutually exclusive. The `tonight` parameter takes precedence and `skip` will be ignored if `tonight` is also passed


### Example Usage

```python
from plex_api_client import PlexAPI
from plex_api_client.models import operations

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    client_id="gcgzw5rz2xovp84b4vha3a40",
    client_name="Plex Web",
    client_version="4.133.0",
    client_platform="Chrome",
    device_name="Linux",
)

res = s.updater.apply_updates(tonight=operations.Tonight.ONE, skip=operations.Skip.ONE)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                | Type                                                                                                                                                     | Required                                                                                                                                                 | Description                                                                                                                                              | Example                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tonight`                                                                                                                                                | [Optional[operations.Tonight]](../../models/operations/tonight.md)                                                                                       | :heavy_minus_sign:                                                                                                                                       | Indicate that you want the update to run during the next Butler execution. Omitting this or setting it to false indicates that the update should install | 1                                                                                                                                                        |
| `skip`                                                                                                                                                   | [Optional[operations.Skip]](../../models/operations/skip.md)                                                                                             | :heavy_minus_sign:                                                                                                                                       | Indicate that the latest version should be marked as skipped. The [Release] entry for this version will have the `state` set to `skipped`.               | 1                                                                                                                                                        |
| `retries`                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                         | :heavy_minus_sign:                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                      |                                                                                                                                                          |

### Response

**[operations.ApplyUpdatesResponse](../../models/operations/applyupdatesresponse.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ApplyUpdatesBadRequest   | 400                             | application/json                |
| errors.ApplyUpdatesUnauthorized | 401                             | application/json                |
| errors.SDKError                 | 4XX, 5XX                        | \*/\*                           |