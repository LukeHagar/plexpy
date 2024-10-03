# Statistics
(*statistics*)

## Overview

API Calls that perform operations with Plex Media Server Statistics


### Available Operations

* [get_statistics](#get_statistics) - Get Media Statistics
* [get_resources_statistics](#get_resources_statistics) - Get Resources Statistics
* [get_bandwidth_statistics](#get_bandwidth_statistics) - Get Bandwidth Statistics

## get_statistics

This will return the media statistics for the server

### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    client_id="3381b62b-9ab7-4e37-827b-203e9809eb58",
    client_name="Plex for Roku",
    client_version="2.4.1",
    platform="Roku",
    device_nickname="Roku 3",
)

res = s.statistics.get_statistics(timespan=4)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               | Example                                                                                   |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `timespan`                                                                                | *Optional[int]*                                                                           | :heavy_minus_sign:                                                                        | The timespan to retrieve statistics for<br/>the exact meaning of this parameter is not known<br/> | 4                                                                                         |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |                                                                                           |

### Response

**[operations.GetStatisticsResponse](../../models/operations/getstatisticsresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.GetStatisticsBadRequest   | 400                              | application/json                 |
| errors.GetStatisticsUnauthorized | 401                              | application/json                 |
| errors.SDKError                  | 4XX, 5XX                         | \*/\*                            |

## get_resources_statistics

This will return the resources for the server

### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    client_id="3381b62b-9ab7-4e37-827b-203e9809eb58",
    client_name="Plex for Roku",
    client_version="2.4.1",
    platform="Roku",
    device_nickname="Roku 3",
)

res = s.statistics.get_resources_statistics(timespan=4)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               | Example                                                                                   |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `timespan`                                                                                | *Optional[int]*                                                                           | :heavy_minus_sign:                                                                        | The timespan to retrieve statistics for<br/>the exact meaning of this parameter is not known<br/> | 4                                                                                         |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |                                                                                           |

### Response

**[operations.GetResourcesStatisticsResponse](../../models/operations/getresourcesstatisticsresponse.md)**

### Errors

| Error Type                                | Status Code                               | Content Type                              |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| errors.GetResourcesStatisticsBadRequest   | 400                                       | application/json                          |
| errors.GetResourcesStatisticsUnauthorized | 401                                       | application/json                          |
| errors.SDKError                           | 4XX, 5XX                                  | \*/\*                                     |

## get_bandwidth_statistics

This will return the bandwidth statistics for the server

### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    client_id="3381b62b-9ab7-4e37-827b-203e9809eb58",
    client_name="Plex for Roku",
    client_version="2.4.1",
    platform="Roku",
    device_nickname="Roku 3",
)

res = s.statistics.get_bandwidth_statistics(timespan=4)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               | Example                                                                                   |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `timespan`                                                                                | *Optional[int]*                                                                           | :heavy_minus_sign:                                                                        | The timespan to retrieve statistics for<br/>the exact meaning of this parameter is not known<br/> | 4                                                                                         |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |                                                                                           |

### Response

**[operations.GetBandwidthStatisticsResponse](../../models/operations/getbandwidthstatisticsresponse.md)**

### Errors

| Error Type                                | Status Code                               | Content Type                              |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| errors.GetBandwidthStatisticsBadRequest   | 400                                       | application/json                          |
| errors.GetBandwidthStatisticsUnauthorized | 401                                       | application/json                          |
| errors.SDKError                           | 4XX, 5XX                                  | \*/\*                                     |