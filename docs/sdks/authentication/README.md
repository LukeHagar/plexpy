# Authentication
(*authentication*)

## Overview

API Calls regarding authentication for Plex Media Server


### Available Operations

* [get_transient_token](#get_transient_token) - Get a Transient Token.
* [get_source_connection_information](#get_source_connection_information) - Get Source Connection Information
* [get_user_details](#get_user_details) - Get User Data By Token
* [post_users_sign_in_data](#post_users_sign_in_data) - Get User Sign In Data

## get_transient_token

This endpoint provides the caller with a temporary token with the same access level as the caller's token. These tokens are valid for up to 48 hours and are destroyed if the server instance is restarted.


### Example Usage

```python
from plex_api_client import PlexAPI
from plex_api_client.models import operations

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier="gcgzw5rz2xovp84b4vha3a40",
)

res = s.authentication.get_transient_token(type_=operations.GetTransientTokenQueryParamType.DELEGATION, scope=operations.Scope.ALL)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `type`                                                                                                   | [operations.GetTransientTokenQueryParamType](../../models/operations/gettransienttokenqueryparamtype.md) | :heavy_check_mark:                                                                                       | `delegation` - This is the only supported `type` parameter.                                              |
| `scope`                                                                                                  | [operations.Scope](../../models/operations/scope.md)                                                     | :heavy_check_mark:                                                                                       | `all` - This is the only supported `scope` parameter.                                                    |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.GetTransientTokenResponse](../../models/operations/gettransienttokenresponse.md)**

### Errors

| Error Object                                       | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| errors.GetTransientTokenResponseBody               | 400                                                | application/json                                   |
| errors.GetTransientTokenAuthenticationResponseBody | 401                                                | application/json                                   |
| errors.SDKError                                    | 4xx-5xx                                            | */*                                                |


## get_source_connection_information

If a caller requires connection details and a transient token for a source that is known to the server, for example a cloud media provider or shared PMS, then this endpoint can be called. This endpoint is only accessible with either an admin token or a valid transient token generated from an admin token.
Note: requires Plex Media Server >= 1.15.4.


### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier="gcgzw5rz2xovp84b4vha3a40",
)

res = s.authentication.get_source_connection_information(source="server://client-identifier")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `source`                                                            | *str*                                                               | :heavy_check_mark:                                                  | The source identifier with an included prefix.                      | server://client-identifier                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.GetSourceConnectionInformationResponse](../../models/operations/getsourceconnectioninformationresponse.md)**

### Errors

| Error Object                                                    | Status Code                                                     | Content Type                                                    |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| errors.GetSourceConnectionInformationResponseBody               | 400                                                             | application/json                                                |
| errors.GetSourceConnectionInformationAuthenticationResponseBody | 401                                                             | application/json                                                |
| errors.SDKError                                                 | 4xx-5xx                                                         | */*                                                             |


## get_user_details

Get the User data from the provided X-Plex-Token

### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier="gcgzw5rz2xovp84b4vha3a40",
)

res = s.authentication.get_user_details(x_plex_token="CV5xoxjTpFKUzBTShsaf")

if res.user_plex_account is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `x_plex_token`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Plex Authentication Token                                           | CV5xoxjTpFKUzBTShsaf                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[operations.GetUserDetailsResponse](../../models/operations/getuserdetailsresponse.md)**

### Errors

| Error Object                                    | Status Code                                     | Content Type                                    |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| errors.GetUserDetailsResponseBody               | 400                                             | application/json                                |
| errors.GetUserDetailsAuthenticationResponseBody | 401                                             | application/json                                |
| errors.SDKError                                 | 4xx-5xx                                         | */*                                             |


## post_users_sign_in_data

Sign in user with username and password and return user data with Plex authentication token

### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    x_plex_client_identifier="gcgzw5rz2xovp84b4vha3a40",
)

res = s.authentication.post_users_sign_in_data(x_plex_client_identifier="gcgzw5rz2xovp84b4vha3a40", request_body={
    "login": "username@email.com",
    "password": "password123",
    "verification_code": "123456",
})

if res.user_plex_account is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                             | Type                                                                                                                                                                  | Required                                                                                                                                                              | Description                                                                                                                                                           | Example                                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `x_plex_client_identifier`                                                                                                                                            | *Optional[str]*                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                    | The unique identifier for the client application<br/>This is used to track the client application and its usage<br/>(UUID, serial number, or other number unique per device)<br/> | gcgzw5rz2xovp84b4vha3a40                                                                                                                                              |
| `request_body`                                                                                                                                                        | [Optional[operations.PostUsersSignInDataRequestBody]](../../models/operations/postuserssignindatarequestbody.md)                                                      | :heavy_minus_sign:                                                                                                                                                    | Login credentials                                                                                                                                                     |                                                                                                                                                                       |
| `retries`                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                      | :heavy_minus_sign:                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                   |                                                                                                                                                                       |
| `server_url`                                                                                                                                                          | *Optional[str]*                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                    | An optional server URL to use.                                                                                                                                        | http://localhost:8080                                                                                                                                                 |

### Response

**[operations.PostUsersSignInDataResponse](../../models/operations/postuserssignindataresponse.md)**

### Errors

| Error Object                                         | Status Code                                          | Content Type                                         |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| errors.PostUsersSignInDataResponseBody               | 400                                                  | application/json                                     |
| errors.PostUsersSignInDataAuthenticationResponseBody | 401                                                  | application/json                                     |
| errors.SDKError                                      | 4xx-5xx                                              | */*                                                  |
