# Users

## Overview

### Available Operations

* [get_users](#get_users) - Get list of all connected users

## get_users

Get list of all users that are friends and have library access with the provided Plex authentication token

### Example Usage

<!-- UsageSnippet language="python" operationID="get-users" method="get" path="/users" -->
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
    device_name="Chrome",
    marketplace="googlePlay",
    token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.users.get_users(request={})

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.GetUsersRequest](../../models/operations/getusersrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |
| `retries`                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)         | :heavy_minus_sign:                                                       | Configuration to override the default retry behavior of the client.      |
| `server_url`                                                             | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | An optional server URL to use.                                           |

### Response

**[operations.GetUsersResponse](../../models/operations/getusersresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.GetUsersBadRequest   | 400                         | application/json            |
| errors.GetUsersUnauthorized | 401                         | application/json            |
| errors.SDKError             | 4XX, 5XX                    | \*/\*                       |