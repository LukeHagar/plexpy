# Server
(*server*)

## Overview

Operations against the Plex Media Server System.


### Available Operations

* [get_server_capabilities](#get_server_capabilities) - Get Server Capabilities
* [get_server_preferences](#get_server_preferences) - Get Server Preferences
* [get_available_clients](#get_available_clients) - Get Available Clients
* [get_devices](#get_devices) - Get Devices
* [get_server_identity](#get_server_identity) - Get Server Identity
* [get_my_plex_account](#get_my_plex_account) - Get MyPlex Account
* [get_resized_photo](#get_resized_photo) - Get a Resized Photo
* [get_media_providers](#get_media_providers) - Get Media Providers
* [get_server_list](#get_server_list) - Get Server List

## get_server_capabilities

Get Server Capabilities

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

res = s.server.get_server_capabilities()

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetServerCapabilitiesResponse](../../models/operations/getservercapabilitiesresponse.md)**

### Errors

| Error Object                             | Status Code                              | Content Type                             |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| errors.GetServerCapabilitiesBadRequest   | 400                                      | application/json                         |
| errors.GetServerCapabilitiesUnauthorized | 401                                      | application/json                         |
| errors.SDKError                          | 4xx-5xx                                  | */*                                      |


## get_server_preferences

Get Server Preferences

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

res = s.server.get_server_preferences()

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetServerPreferencesResponse](../../models/operations/getserverpreferencesresponse.md)**

### Errors

| Error Object                            | Status Code                             | Content Type                            |
| --------------------------------------- | --------------------------------------- | --------------------------------------- |
| errors.GetServerPreferencesBadRequest   | 400                                     | application/json                        |
| errors.GetServerPreferencesUnauthorized | 401                                     | application/json                        |
| errors.SDKError                         | 4xx-5xx                                 | */*                                     |


## get_available_clients

Get Available Clients

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

res = s.server.get_available_clients()

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetAvailableClientsResponse](../../models/operations/getavailableclientsresponse.md)**

### Errors

| Error Object                           | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.GetAvailableClientsBadRequest   | 400                                    | application/json                       |
| errors.GetAvailableClientsUnauthorized | 401                                    | application/json                       |
| errors.SDKError                        | 4xx-5xx                                | */*                                    |


## get_devices

Get Devices

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

res = s.server.get_devices()

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetDevicesResponse](../../models/operations/getdevicesresponse.md)**

### Errors

| Error Object                  | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.GetDevicesBadRequest   | 400                           | application/json              |
| errors.GetDevicesUnauthorized | 401                           | application/json              |
| errors.SDKError               | 4xx-5xx                       | */*                           |


## get_server_identity

This request is useful to determine if the server is online or offline

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

res = s.server.get_server_identity()

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetServerIdentityResponse](../../models/operations/getserveridentityresponse.md)**

### Errors

| Error Object                           | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.GetServerIdentityRequestTimeout | 408                                    | application/json                       |
| errors.SDKError                        | 4xx-5xx                                | */*                                    |


## get_my_plex_account

Returns MyPlex Account Information

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

res = s.server.get_my_plex_account()

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetMyPlexAccountResponse](../../models/operations/getmyplexaccountresponse.md)**

### Errors

| Error Object                        | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| errors.GetMyPlexAccountBadRequest   | 400                                 | application/json                    |
| errors.GetMyPlexAccountUnauthorized | 401                                 | application/json                    |
| errors.SDKError                     | 4xx-5xx                             | */*                                 |


## get_resized_photo

Plex's Photo transcoder is used throughout the service to serve images at specified sizes.


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

res = s.server.get_resized_photo(request={
    "width": 110,
    "height": 165,
    "blur": 20,
    "min_size": operations.MinSize.ONE,
    "upscale": operations.Upscale.ONE,
    "url": "/library/metadata/49564/thumb/1654258204",
    "opacity": 100,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetResizedPhotoRequest](../../models/operations/getresizedphotorequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetResizedPhotoResponse](../../models/operations/getresizedphotoresponse.md)**

### Errors

| Error Object                       | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.GetResizedPhotoBadRequest   | 400                                | application/json                   |
| errors.GetResizedPhotoUnauthorized | 401                                | application/json                   |
| errors.SDKError                    | 4xx-5xx                            | */*                                |


## get_media_providers

Retrieves media providers and their features from the Plex server.

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

res = s.server.get_media_providers(x_plex_token="CV5xoxjTpFKUzBTShsaf")

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `x_plex_token`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Plex Authentication Token                                           | CV5xoxjTpFKUzBTShsaf                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.GetMediaProvidersResponse](../../models/operations/getmediaprovidersresponse.md)**

### Errors

| Error Object                         | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| errors.GetMediaProvidersBadRequest   | 400                                  | application/json                     |
| errors.GetMediaProvidersUnauthorized | 401                                  | application/json                     |
| errors.SDKError                      | 4xx-5xx                              | */*                                  |


## get_server_list

Get Server List

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

res = s.server.get_server_list()

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetServerListResponse](../../models/operations/getserverlistresponse.md)**

### Errors

| Error Object                     | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.GetServerListBadRequest   | 400                              | application/json                 |
| errors.GetServerListUnauthorized | 401                              | application/json                 |
| errors.SDKError                  | 4xx-5xx                          | */*                              |
