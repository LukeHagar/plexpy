# Authentication
(*authentication*)

## Overview

API Calls regarding authentication for Plex Media Server


### Available Operations

* [get_transient_token](#get_transient_token) - Get a Transient Token
* [get_source_connection_information](#get_source_connection_information) - Get Source Connection Information
* [get_token_details](#get_token_details) - Get Token Details
* [post_users_sign_in_data](#post_users_sign_in_data) - Get User Sign In Data

## get_transient_token

This endpoint provides the caller with a temporary token with the same access level as the caller's token. These tokens are valid for up to 48 hours and are destroyed if the server instance is restarted.


### Example Usage

```python
from plex_api_client import PlexAPI
from plex_api_client.models import operations

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    client_id="3381b62b-9ab7-4e37-827b-203e9809eb58",
    client_name="Plex for Roku",
    client_version="2.4.1",
    platform="Roku",
    device_nickname="Roku 3",
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

| Error Type                           | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| errors.GetTransientTokenBadRequest   | 400                                  | application/json                     |
| errors.GetTransientTokenUnauthorized | 401                                  | application/json                     |
| errors.SDKError                      | 4XX, 5XX                             | \*/\*                                |

## get_source_connection_information

If a caller requires connection details and a transient token for a source that is known to the server, for example a cloud media provider or shared PMS, then this endpoint can be called. This endpoint is only accessible with either an admin token or a valid transient token generated from an admin token.
Note: requires Plex Media Server >= 1.15.4.


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

res = s.authentication.get_source_connection_information(source="provider://provider-identifier")

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

| Error Type                                        | Status Code                                       | Content Type                                      |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| errors.GetSourceConnectionInformationBadRequest   | 400                                               | application/json                                  |
| errors.GetSourceConnectionInformationUnauthorized | 401                                               | application/json                                  |
| errors.SDKError                                   | 4XX, 5XX                                          | \*/\*                                             |

## get_token_details

Get the User data from the provided X-Plex-Token

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

res = s.authentication.get_token_details()

if res.user_plex_account is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[operations.GetTokenDetailsResponse](../../models/operations/gettokendetailsresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.GetTokenDetailsBadRequest   | 400                                | application/json                   |
| errors.GetTokenDetailsUnauthorized | 401                                | application/json                   |
| errors.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## post_users_sign_in_data

Sign in user with username and password and return user data with Plex authentication token

### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    client_id="3381b62b-9ab7-4e37-827b-203e9809eb58",
    client_name="Plex for Roku",
    client_version="2.4.1",
    platform="Roku",
    device_nickname="Roku 3",
)

res = s.authentication.post_users_sign_in_data(request={
    "request_body": {
        "login": "username@email.com",
        "password": "password123",
        "verification_code": "123456",
    },
})

if res.user_plex_account is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PostUsersSignInDataRequest](../../models/operations/postuserssignindatarequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |
| `server_url`                                                                                   | *Optional[str]*                                                                                | :heavy_minus_sign:                                                                             | An optional server URL to use.                                                                 |

### Response

**[operations.PostUsersSignInDataResponse](../../models/operations/postuserssignindataresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.PostUsersSignInDataBadRequest   | 400                                    | application/json                       |
| errors.PostUsersSignInDataUnauthorized | 401                                    | application/json                       |
| errors.SDKError                        | 4XX, 5XX                               | \*/\*                                  |