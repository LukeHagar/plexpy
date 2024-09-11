# Sessions
(*sessions*)

## Overview

API Calls that perform search operations with Plex Media Server Sessions


### Available Operations

* [get_sessions](#get_sessions) - Get Active Sessions
* [get_session_history](#get_session_history) - Get Session History
* [get_transcode_sessions](#get_transcode_sessions) - Get Transcode Sessions
* [stop_transcode_session](#stop_transcode_session) - Stop a Transcode Session

## get_sessions

This will retrieve the "Now Playing" Information of the PMS.

### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier="gcgzw5rz2xovp84b4vha3a40",
)

res = s.sessions.get_sessions()

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetSessionsResponse](../../models/operations/getsessionsresponse.md)**

### Errors

| Error Object                   | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| errors.GetSessionsBadRequest   | 400                            | application/json               |
| errors.GetSessionsUnauthorized | 401                            | application/json               |
| errors.SDKError                | 4xx-5xx                        | */*                            |


## get_session_history

This will Retrieve a listing of all history views.

### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier="gcgzw5rz2xovp84b4vha3a40",
)

res = s.sessions.get_session_history(sort="viewedAt:desc", account_id=1, filter_={}, library_section_id=12)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                     | Type                                                                                                                                                                                          | Required                                                                                                                                                                                      | Description                                                                                                                                                                                   | Example                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sort`                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                            | Sorts the results by the specified field followed by the direction (asc, desc)<br/>                                                                                                           |                                                                                                                                                                                               |
| `account_id`                                                                                                                                                                                  | *Optional[int]*                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                            | Filter results by those that are related to a specific users id<br/>                                                                                                                          | 1                                                                                                                                                                                             |
| `filter_`                                                                                                                                                                                     | [Optional[operations.QueryParamFilter]](../../models/operations/queryparamfilter.md)                                                                                                          | :heavy_minus_sign:                                                                                                                                                                            | Filters content by field and direction/equality<br/>(Unknown if viewedAt is the only supported column)<br/>                                                                                   | {<br/>"viewed-at-greater-than": {<br/>"value": "viewedAt\u003e"<br/>},<br/>"viewed-at-greater-than-or-equal-to": {<br/>"value": "viewedAt\u003e=\u003e"<br/>},<br/>"viewed-at-less-than": {<br/>"value": "viewedAt\u003c"<br/>}<br/>} |
| `library_section_id`                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                            | Filters the results based on the id of a valid library section<br/>                                                                                                                           | 12                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                           |                                                                                                                                                                                               |

### Response

**[operations.GetSessionHistoryResponse](../../models/operations/getsessionhistoryresponse.md)**

### Errors

| Error Object                         | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| errors.GetSessionHistoryBadRequest   | 400                                  | application/json                     |
| errors.GetSessionHistoryUnauthorized | 401                                  | application/json                     |
| errors.SDKError                      | 4xx-5xx                              | */*                                  |


## get_transcode_sessions

Get Transcode Sessions

### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier="gcgzw5rz2xovp84b4vha3a40",
)

res = s.sessions.get_transcode_sessions()

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetTranscodeSessionsResponse](../../models/operations/gettranscodesessionsresponse.md)**

### Errors

| Error Object                            | Status Code                             | Content Type                            |
| --------------------------------------- | --------------------------------------- | --------------------------------------- |
| errors.GetTranscodeSessionsBadRequest   | 400                                     | application/json                        |
| errors.GetTranscodeSessionsUnauthorized | 401                                     | application/json                        |
| errors.SDKError                         | 4xx-5xx                                 | */*                                     |


## stop_transcode_session

Stop a Transcode Session

### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier="gcgzw5rz2xovp84b4vha3a40",
)

res = s.sessions.stop_transcode_session(session_key="zz7llzqlx8w9vnrsbnwhbmep")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `session_key`                                                       | *str*                                                               | :heavy_check_mark:                                                  | the Key of the transcode session to stop                            | zz7llzqlx8w9vnrsbnwhbmep                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.StopTranscodeSessionResponse](../../models/operations/stoptranscodesessionresponse.md)**

### Errors

| Error Object                            | Status Code                             | Content Type                            |
| --------------------------------------- | --------------------------------------- | --------------------------------------- |
| errors.StopTranscodeSessionBadRequest   | 400                                     | application/json                        |
| errors.StopTranscodeSessionUnauthorized | 401                                     | application/json                        |
| errors.SDKError                         | 4xx-5xx                                 | */*                                     |
