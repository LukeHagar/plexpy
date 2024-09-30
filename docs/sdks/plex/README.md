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
    client_id="gcgzw5rz2xovp84b4vha3a40",
    client_name="Plex Web",
    client_version="4.133.0",
    client_platform="Chrome",
    device_name="Linux",
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

| Error Type                           | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| errors.GetCompanionsDataBadRequest   | 400                                  | application/json                     |
| errors.GetCompanionsDataUnauthorized | 401                                  | application/json                     |
| errors.SDKError                      | 4XX, 5XX                             | \*/\*                                |

## get_user_friends

Get friends of provided auth token.

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

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.GetUserFriendsBadRequest   | 400                               | application/json                  |
| errors.GetUserFriendsUnauthorized | 401                               | application/json                  |
| errors.SDKError                   | 4XX, 5XX                          | \*/\*                             |

## get_geo_data

Returns the geolocation and locale data of the caller

### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    client_id="gcgzw5rz2xovp84b4vha3a40",
    client_name="Plex Web",
    client_version="4.133.0",
    client_platform="Chrome",
    device_name="Linux",
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

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.GetGeoDataBadRequest   | 400                           | application/json              |
| errors.GetGeoDataUnauthorized | 401                           | application/json              |
| errors.SDKError               | 4XX, 5XX                      | \*/\*                         |

## get_home_data

Retrieves the home data for the authenticated user, including details like home ID, name, guest access information, and subscription status.

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

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| errors.GetHomeDataBadRequest   | 400                            | application/json               |
| errors.GetHomeDataUnauthorized | 401                            | application/json               |
| errors.SDKError                | 4XX, 5XX                       | \*/\*                          |

## get_server_resources

Get Plex server access tokens and server connections

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

res = s.plex.get_server_resources(include_https=operations.IncludeHTTPS.ENABLE, include_relay=operations.IncludeRelay.ENABLE, include_i_pv6=operations.IncludeIPv6.ENABLE, client_id="gcgzw5rz2xovp84b4vha3a40")

if res.plex_devices is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                             | Type                                                                                                                                                                  | Required                                                                                                                                                              | Description                                                                                                                                                           | Example                                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `include_https`                                                                                                                                                       | [Optional[operations.IncludeHTTPS]](../../models/operations/includehttps.md)                                                                                          | :heavy_minus_sign:                                                                                                                                                    | Include Https entries in the results                                                                                                                                  | 1                                                                                                                                                                     |
| `include_relay`                                                                                                                                                       | [Optional[operations.IncludeRelay]](../../models/operations/includerelay.md)                                                                                          | :heavy_minus_sign:                                                                                                                                                    | Include Relay addresses in the results <br/>E.g: https://10-0-0-25.bbf8e10c7fa20447cacee74cd9914cde.plex.direct:32400<br/>                                            | 1                                                                                                                                                                     |
| `include_i_pv6`                                                                                                                                                       | [Optional[operations.IncludeIPv6]](../../models/operations/includeipv6.md)                                                                                            | :heavy_minus_sign:                                                                                                                                                    | Include IPv6 entries in the results                                                                                                                                   | 1                                                                                                                                                                     |
| `client_id`                                                                                                                                                           | *Optional[str]*                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                    | The unique identifier for the client application<br/>This is used to track the client application and its usage<br/>(UUID, serial number, or other number unique per device)<br/> | gcgzw5rz2xovp84b4vha3a40                                                                                                                                              |
| `retries`                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                      | :heavy_minus_sign:                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                   |                                                                                                                                                                       |
| `server_url`                                                                                                                                                          | *Optional[str]*                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                    | An optional server URL to use.                                                                                                                                        | http://localhost:8080                                                                                                                                                 |

### Response

**[operations.GetServerResourcesResponse](../../models/operations/getserverresourcesresponse.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| errors.GetServerResourcesBadRequest   | 400                                   | application/json                      |
| errors.GetServerResourcesUnauthorized | 401                                   | application/json                      |
| errors.SDKError                       | 4XX, 5XX                              | \*/\*                                 |

## get_pin

Retrieve a Pin ID from Plex.tv to use for authentication flows

### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    client_id="gcgzw5rz2xovp84b4vha3a40",
    client_name="Plex Web",
    client_version="4.133.0",
    client_platform="Chrome",
    device_name="Linux",
)

res = s.plex.get_pin(request={})

if res.auth_pin_container is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [operations.GetPinRequest](../../models/operations/getpinrequest.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |
| `server_url`                                                         | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | An optional server URL to use.                                       |

### Response

**[operations.GetPinResponse](../../models/operations/getpinresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.GetPinBadRequest | 400                     | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_token_by_pin_id

Retrieve an Access Token from Plex.tv after the Pin has been authenticated

### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    client_id="gcgzw5rz2xovp84b4vha3a40",
    client_name="Plex Web",
    client_version="4.133.0",
    client_platform="Chrome",
    device_name="Linux",
)

res = s.plex.get_token_by_pin_id(request={
    "pin_id": 408895,
})

if res.auth_pin_container is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetTokenByPinIDRequest](../../models/operations/gettokenbypinidrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |
| `server_url`                                                                           | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | An optional server URL to use.                                                         |

### Response

**[operations.GetTokenByPinIDResponse](../../models/operations/gettokenbypinidresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.GetTokenByPinIDBadRequest   | 400                                | application/json                   |
| errors.GetTokenByPinIDResponseBody | 404                                | application/json                   |
| errors.SDKError                    | 4XX, 5XX                           | \*/\*                              |