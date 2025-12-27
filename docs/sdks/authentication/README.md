# Authentication

## Overview

### Available Operations

* [get_token_details](#get_token_details) - Get Token Details
* [post_users_sign_in_data](#post_users_sign_in_data) - Get User Sign In Data

## get_token_details

Get the User data from the provided X-Plex-Token

### Example Usage

<!-- UsageSnippet language="python" operationID="getTokenDetails" method="get" path="/user" -->
```python
from plex_api_client import PlexAPI
from plex_api_client.models import components


with PlexAPI(
    accepts=components.Accepts.APPLICATION_XML,
    client_identifier="abc123",
    product="Plex for Roku",
    version="2.4.1",
    platform="Roku",
    platform_version="4.3 build 1057",
    device="Roku 3",
    model="4200X",
    device_vendor="Roku",
    device_name="Living Room TV",
    marketplace="googlePlay",
    token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.authentication.get_token_details(request={})

    assert res.user_plex_account is not None

    # Handle response
    print(res.user_plex_account)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetTokenDetailsRequest](../../models/operations/gettokendetailsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |
| `server_url`                                                                           | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | An optional server URL to use.                                                         |

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

<!-- UsageSnippet language="python" operationID="post-users-sign-in-data" method="post" path="/users/signin" -->
```python
from plex_api_client import PlexAPI
from plex_api_client.models import components


with PlexAPI(
    accepts=components.Accepts.APPLICATION_XML,
    client_identifier="3381b62b-9ab7-4e37-827b-203e9809eb58",
    product="Plex for Roku",
    version="2.4.1",
    platform="Roku",
    platform_version="4.3 build 1057",
    device="Roku 3",
    model="4200X",
    device_vendor="Roku",
    device_name="Living Room TV",
    marketplace="googlePlay",
) as plex_api:

    res = plex_api.authentication.post_users_sign_in_data(request={
        "request_body": {
            "login": "username@email.com",
            "password": "password123",
            "verification_code": "123456",
        },
    })

    assert res.user_plex_account is not None

    # Handle response
    print(res.user_plex_account)

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