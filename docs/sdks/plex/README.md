# Plex
(*plex*)

## Overview

API Calls that perform operations directly against https://Plex.tv


### Available Operations

* [get_companions_data](#get_companions_data) - Get Companions Data
* [get_user_friends](#get_user_friends) - Get list of friends of the user logged in
* [get_geo_data](#get_geo_data) - Get Geo Data
* [get_home_data](#get_home_data) - Get Plex Home Data
* [get_server_resources](#get_server_resources) - Get Server Resources
* [get_pin](#get_pin) - Get a Pin
* [get_token_by_pin_id](#get_token_by_pin_id) - Get Access Token by PinId

## get_companions_data

Get Companions Data

### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier="gcgzw5rz2xovp84b4vha3a40",
)

res = s.plex.get_companions_data()

if res.response_bodies is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[operations.GetCompanionsDataResponse](../../models/operations/getcompanionsdataresponse.md)**

### Errors

| Error Object                             | Status Code                              | Content Type                             |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| errors.GetCompanionsDataResponseBody     | 400                                      | application/json                         |
| errors.GetCompanionsDataPlexResponseBody | 401                                      | application/json                         |
| errors.SDKError                          | 4xx-5xx                                  | */*                                      |


## get_user_friends

Get friends of provided auth token.

### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier="gcgzw5rz2xovp84b4vha3a40",
)

res = s.plex.get_user_friends()

if res.friends is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[operations.GetUserFriendsResponse](../../models/operations/getuserfriendsresponse.md)**

### Errors

| Error Object                          | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| errors.GetUserFriendsResponseBody     | 400                                   | application/json                      |
| errors.GetUserFriendsPlexResponseBody | 401                                   | application/json                      |
| errors.SDKError                       | 4xx-5xx                               | */*                                   |


## get_geo_data

Returns the geolocation and locale data of the caller

### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    x_plex_client_identifier="gcgzw5rz2xovp84b4vha3a40",
)

res = s.plex.get_geo_data()

if res.geo_data is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[operations.GetGeoDataResponse](../../models/operations/getgeodataresponse.md)**

### Errors

| Error Object                      | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.GetGeoDataResponseBody     | 400                               | application/json                  |
| errors.GetGeoDataPlexResponseBody | 401                               | application/json                  |
| errors.SDKError                   | 4xx-5xx                           | */*                               |


## get_home_data

Retrieves the home data for the authenticated user, including details like home ID, name, guest access information, and subscription status.

### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier="gcgzw5rz2xovp84b4vha3a40",
)

res = s.plex.get_home_data()

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetHomeDataResponse](../../models/operations/gethomedataresponse.md)**

### Errors

| Error Object                       | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.GetHomeDataResponseBody     | 400                                | application/json                   |
| errors.GetHomeDataPlexResponseBody | 401                                | application/json                   |
| errors.SDKError                    | 4xx-5xx                            | */*                                |


## get_server_resources

Get Plex server access tokens and server connections

### Example Usage

```python
from plex_api_client import PlexAPI
from plex_api_client.models import operations

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier="gcgzw5rz2xovp84b4vha3a40",
)

res = s.plex.get_server_resources(request={
    "x_plex_token": "CV5xoxjTpFKUzBTShsaf",
    "include_https": operations.IncludeHTTPS.ONE,
    "include_relay": operations.IncludeRelay.ONE,
    "include_i_pv6": operations.IncludeIPv6.ONE,
})

if res.plex_devices is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetServerResourcesRequest](../../models/operations/getserverresourcesrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |
| `server_url`                                                                                 | *Optional[str]*                                                                              | :heavy_minus_sign:                                                                           | An optional server URL to use.                                                               |

### Response

**[operations.GetServerResourcesResponse](../../models/operations/getserverresourcesresponse.md)**

### Errors

| Error Object                              | Status Code                               | Content Type                              |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| errors.GetServerResourcesResponseBody     | 400                                       | application/json                          |
| errors.GetServerResourcesPlexResponseBody | 401                                       | application/json                          |
| errors.SDKError                           | 4xx-5xx                                   | */*                                       |


## get_pin

Retrieve a Pin from Plex.tv for authentication flows

### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    x_plex_client_identifier="gcgzw5rz2xovp84b4vha3a40",
)

res = s.plex.get_pin(x_plex_client_identifier="gcgzw5rz2xovp84b4vha3a40", x_plex_product="Plex Web")

if res.auth_pin_container is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                             | Type                                                                                                                                                                  | Required                                                                                                                                                              | Description                                                                                                                                                           | Example                                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `strong`                                                                                                                                                              | *Optional[bool]*                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                    | Determines the kind of code returned by the API call<br/>Strong codes are used for Pin authentication flows<br/>Non-Strong codes are used for `Plex.tv/link`<br/>     |                                                                                                                                                                       |
| `x_plex_client_identifier`                                                                                                                                            | *Optional[str]*                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                    | The unique identifier for the client application<br/>This is used to track the client application and its usage<br/>(UUID, serial number, or other number unique per device)<br/> | gcgzw5rz2xovp84b4vha3a40                                                                                                                                              |
| `x_plex_product`                                                                                                                                                      | *Optional[str]*                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                    | N/A                                                                                                                                                                   | Plex Web                                                                                                                                                              |
| `retries`                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                      | :heavy_minus_sign:                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                   |                                                                                                                                                                       |
| `server_url`                                                                                                                                                          | *Optional[str]*                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                    | An optional server URL to use.                                                                                                                                        | http://localhost:8080                                                                                                                                                 |

### Response

**[operations.GetPinResponse](../../models/operations/getpinresponse.md)**

### Errors

| Error Object              | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.GetPinResponseBody | 400                       | application/json          |
| errors.SDKError           | 4xx-5xx                   | */*                       |


## get_token_by_pin_id

Retrieve an Access Token from Plex.tv after the Pin has been authenticated

### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    x_plex_client_identifier="gcgzw5rz2xovp84b4vha3a40",
)

res = s.plex.get_token_by_pin_id(pin_id=408895, x_plex_client_identifier="gcgzw5rz2xovp84b4vha3a40")

if res.auth_pin_container is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                             | Type                                                                                                                                                                  | Required                                                                                                                                                              | Description                                                                                                                                                           | Example                                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pin_id`                                                                                                                                                              | *int*                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                    | The PinID to retrieve an access token for                                                                                                                             |                                                                                                                                                                       |
| `x_plex_client_identifier`                                                                                                                                            | *Optional[str]*                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                    | The unique identifier for the client application<br/>This is used to track the client application and its usage<br/>(UUID, serial number, or other number unique per device)<br/> | gcgzw5rz2xovp84b4vha3a40                                                                                                                                              |
| `retries`                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                      | :heavy_minus_sign:                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                   |                                                                                                                                                                       |
| `server_url`                                                                                                                                                          | *Optional[str]*                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                    | An optional server URL to use.                                                                                                                                        | http://localhost:8080                                                                                                                                                 |

### Response

**[operations.GetTokenByPinIDResponse](../../models/operations/gettokenbypinidresponse.md)**

### Errors

| Error Object                           | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.GetTokenByPinIDResponseBody     | 400                                    | application/json                       |
| errors.GetTokenByPinIDPlexResponseBody | 404                                    | application/json                       |
| errors.SDKError                        | 4xx-5xx                                | */*                                    |
