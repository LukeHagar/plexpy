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
* [get_server_list](#get_server_list) - Get Server List

## get_server_capabilities

Get Server Capabilities

### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.server.get_server_capabilities()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.GetServerCapabilitiesResponse](../../models/operations/getservercapabilitiesresponse.md)**
### Errors

| Error Object                             | Status Code                              | Content Type                             |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| errors.GetServerCapabilitiesResponseBody | 401                                      | application/json                         |
| errors.SDKError                          | 4xx-5xx                                  | */*                                      |

## get_server_preferences

Get Server Preferences

### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.server.get_server_preferences()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.GetServerPreferencesResponse](../../models/operations/getserverpreferencesresponse.md)**
### Errors

| Error Object                            | Status Code                             | Content Type                            |
| --------------------------------------- | --------------------------------------- | --------------------------------------- |
| errors.GetServerPreferencesResponseBody | 401                                     | application/json                        |
| errors.SDKError                         | 4xx-5xx                                 | */*                                     |

## get_available_clients

Get Available Clients

### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.server.get_available_clients()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.GetAvailableClientsResponse](../../models/operations/getavailableclientsresponse.md)**
### Errors

| Error Object                           | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.GetAvailableClientsResponseBody | 401                                    | application/json                       |
| errors.SDKError                        | 4xx-5xx                                | */*                                    |

## get_devices

Get Devices

### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.server.get_devices()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.GetDevicesResponse](../../models/operations/getdevicesresponse.md)**
### Errors

| Error Object                  | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.GetDevicesResponseBody | 401                           | application/json              |
| errors.SDKError               | 4xx-5xx                       | */*                           |

## get_server_identity

Get Server Identity

### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.server.get_server_identity()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.GetServerIdentityResponse](../../models/operations/getserveridentityresponse.md)**
### Errors

| Error Object                         | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| errors.GetServerIdentityResponseBody | 401                                  | application/json                     |
| errors.SDKError                      | 4xx-5xx                              | */*                                  |

## get_my_plex_account

Returns MyPlex Account Information

### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.server.get_my_plex_account()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.GetMyPlexAccountResponse](../../models/operations/getmyplexaccountresponse.md)**
### Errors

| Error Object                        | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| errors.GetMyPlexAccountResponseBody | 401                                 | application/json                    |
| errors.SDKError                     | 4xx-5xx                             | */*                                 |

## get_resized_photo

Plex's Photo transcoder is used throughout the service to serve images at specified sizes.


### Example Usage

```python
import plex_api
from plex_api.models import operations

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.server.get_resized_photo(request=operations.GetResizedPhotoRequest(
    width=110,
    height=165,
    blur=20,
    min_size=operations.MinSize.ONE,
    upscale=operations.Upscale.ZERO,
    url='/library/metadata/49564/thumb/1654258204',
    opacity=100,
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetResizedPhotoRequest](../../models/operations/getresizedphotorequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetResizedPhotoResponse](../../models/operations/getresizedphotoresponse.md)**
### Errors

| Error Object                       | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.GetResizedPhotoResponseBody | 401                                | application/json                   |
| errors.SDKError                    | 4xx-5xx                            | */*                                |

## get_server_list

Get Server List

### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.server.get_server_list()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.GetServerListResponse](../../models/operations/getserverlistresponse.md)**
### Errors

| Error Object                     | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.GetServerListResponseBody | 401                              | application/json                 |
| errors.SDKError                  | 4xx-5xx                          | */*                              |
