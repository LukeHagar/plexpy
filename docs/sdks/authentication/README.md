# Authentication
(*authentication*)

## Overview

API Calls regarding authentication for Plex Media Server


### Available Operations

* [get_transient_token](#get_transient_token) - Get a Transient Token.
* [get_source_connection_information](#get_source_connection_information) - Get Source Connection Information

## get_transient_token

This endpoint provides the caller with a temporary token with the same access level as the caller's token. These tokens are valid for up to 48 hours and are destroyed if the server instance is restarted.


### Example Usage

```python
import plex_api
from plex_api.models import operations

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='<value>',
)


res = s.authentication.get_transient_token(type=operations.GetTransientTokenQueryParamType.DELEGATION, scope=operations.Scope.ALL)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `type`                                                                                                   | [operations.GetTransientTokenQueryParamType](../../models/operations/gettransienttokenqueryparamtype.md) | :heavy_check_mark:                                                                                       | `delegation` - This is the only supported `type` parameter.                                              |
| `scope`                                                                                                  | [operations.Scope](../../models/operations/scope.md)                                                     | :heavy_check_mark:                                                                                       | `all` - This is the only supported `scope` parameter.                                                    |


### Response

**[operations.GetTransientTokenResponse](../../models/operations/gettransienttokenresponse.md)**
### Errors

| Error Object                         | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| errors.GetTransientTokenResponseBody | 401                                  | application/json                     |
| errors.SDKError                      | 4xx-5xx                              | */*                                  |

## get_source_connection_information

If a caller requires connection details and a transient token for a source that is known to the server, for example a cloud media provider or shared PMS, then this endpoint can be called. This endpoint is only accessible with either an admin token or a valid transient token generated from an admin token.
Note: requires Plex Media Server >= 1.15.4.


### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='<value>',
)


res = s.authentication.get_source_connection_information(source='server://client-identifier')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                      | Type                                           | Required                                       | Description                                    | Example                                        |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `source`                                       | *str*                                          | :heavy_check_mark:                             | The source identifier with an included prefix. | server://client-identifier                     |


### Response

**[operations.GetSourceConnectionInformationResponse](../../models/operations/getsourceconnectioninformationresponse.md)**
### Errors

| Error Object                                      | Status Code                                       | Content Type                                      |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| errors.GetSourceConnectionInformationResponseBody | 401                                               | application/json                                  |
| errors.SDKError                                   | 4xx-5xx                                           | */*                                               |
