# Plex
(*plex*)

## Overview

API Calls that perform operations directly against https://Plex.tv


### Available Operations

* [get_home_data](#get_home_data) - Get Plex Home Data
* [get_pin](#get_pin) - Get a Pin
* [get_token](#get_token) - Get Access Token

## get_home_data

Retrieves the home data for the authenticated user, including details like home ID, name, guest access information, and subscription status.

### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.plex.get_home_data()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.GetHomeDataResponse](../../models/operations/gethomedataresponse.md)**
### Errors

| Error Object                   | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| errors.GetHomeDataResponseBody | 401                            | application/json               |
| errors.SDKError                | 4xx-5xx                        | */*                            |

## get_pin

Retrieve a Pin from Plex.tv for authentication flows

### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    x_plex_client_identifier='Postman',
)


res = s.plex.get_pin(x_plex_product='Postman', strong=False, x_plex_client_identifier='Postman')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                             | Type                                                                                                                                                                  | Required                                                                                                                                                              | Description                                                                                                                                                           | Example                                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `x_plex_product`                                                                                                                                                      | *str*                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                    | Product name of the application shown in the list of devices<br/>                                                                                                     | Postman                                                                                                                                                               |
| `strong`                                                                                                                                                              | *Optional[bool]*                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                    | Determines the kind of code returned by the API call<br/>Strong codes are used for Pin authentication flows<br/>Non-Strong codes are used for `Plex.tv/link`<br/>     |                                                                                                                                                                       |
| `x_plex_client_identifier`                                                                                                                                            | *Optional[str]*                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                    | The unique identifier for the client application<br/>This is used to track the client application and its usage<br/>(UUID, serial number, or other number unique per device)<br/> | Postman                                                                                                                                                               |
| `server_url`                                                                                                                                                          | *Optional[str]*                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                    | An optional server URL to use.                                                                                                                                        | http://localhost:8080                                                                                                                                                 |


### Response

**[operations.GetPinResponse](../../models/operations/getpinresponse.md)**
### Errors

| Error Object              | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.GetPinResponseBody | 400                       | application/json          |
| errors.SDKError           | 4xx-5xx                   | */*                       |

## get_token

Retrieve an Access Token from Plex.tv after the Pin has already been authenticated

### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    x_plex_client_identifier='Postman',
)


res = s.plex.get_token(pin_id='<value>', x_plex_client_identifier='Postman')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                             | Type                                                                                                                                                                  | Required                                                                                                                                                              | Description                                                                                                                                                           | Example                                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pin_id`                                                                                                                                                              | *str*                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                    | The PinID to retrieve an access token for                                                                                                                             |                                                                                                                                                                       |
| `x_plex_client_identifier`                                                                                                                                            | *Optional[str]*                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                    | The unique identifier for the client application<br/>This is used to track the client application and its usage<br/>(UUID, serial number, or other number unique per device)<br/> | Postman                                                                                                                                                               |
| `server_url`                                                                                                                                                          | *Optional[str]*                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                    | An optional server URL to use.                                                                                                                                        | http://localhost:8080                                                                                                                                                 |


### Response

**[operations.GetTokenResponse](../../models/operations/gettokenresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.GetTokenResponseBody | 400                         | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |
