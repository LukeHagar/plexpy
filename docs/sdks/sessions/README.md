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
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.sessions.get_sessions()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.GetSessionsResponse](../../models/operations/getsessionsresponse.md)**
### Errors

| Error Object                   | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| errors.GetSessionsResponseBody | 401                            | application/json               |
| errors.SDKError                | 4xx-5xx                        | */*                            |

## get_session_history

This will Retrieve a listing of all history views.

### Example Usage

```python
import plex_api
from plex_api.models import operations

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.sessions.get_session_history(sort='<value>', account_id=1, filter_=operations.Filter(), library_section_id=12)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                     | Type                                                                                                                                                                                          | Required                                                                                                                                                                                      | Description                                                                                                                                                                                   | Example                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sort`                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                            | Sorts the results by the specified field followed by the direction (asc, desc)<br/>                                                                                                           |                                                                                                                                                                                               |
| `account_id`                                                                                                                                                                                  | *Optional[int]*                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                            | Filter results by those that are related to a specific users id<br/>                                                                                                                          | 1                                                                                                                                                                                             |
| `filter_`                                                                                                                                                                                     | [Optional[operations.Filter]](../../models/operations/filter_.md)                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                            | Filters content by field and direction/equality<br/>(Unknown if viewedAt is the only supported column)<br/>                                                                                   | {<br/>"viewed-at-greater-than": {<br/>"value": "viewedAt\u003e"<br/>},<br/>"viewed-at-greater-than-or-equal-to": {<br/>"value": "viewedAt\u003e=\u003e"<br/>},<br/>"viewed-at-less-than": {<br/>"value": "viewedAt\u003c"<br/>}<br/>} |
| `library_section_id`                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                            | Filters the results based on the id of a valid library section<br/>                                                                                                                           | 12                                                                                                                                                                                            |


### Response

**[operations.GetSessionHistoryResponse](../../models/operations/getsessionhistoryresponse.md)**
### Errors

| Error Object                         | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| errors.GetSessionHistoryResponseBody | 401                                  | application/json                     |
| errors.SDKError                      | 4xx-5xx                              | */*                                  |

## get_transcode_sessions

Get Transcode Sessions

### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.sessions.get_transcode_sessions()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.GetTranscodeSessionsResponse](../../models/operations/gettranscodesessionsresponse.md)**
### Errors

| Error Object                            | Status Code                             | Content Type                            |
| --------------------------------------- | --------------------------------------- | --------------------------------------- |
| errors.GetTranscodeSessionsResponseBody | 401                                     | application/json                        |
| errors.SDKError                         | 4xx-5xx                                 | */*                                     |

## stop_transcode_session

Stop a Transcode Session

### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.sessions.stop_transcode_session(session_key='zz7llzqlx8w9vnrsbnwhbmep')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                | Type                                     | Required                                 | Description                              | Example                                  |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `session_key`                            | *str*                                    | :heavy_check_mark:                       | the Key of the transcode session to stop | zz7llzqlx8w9vnrsbnwhbmep                 |


### Response

**[operations.StopTranscodeSessionResponse](../../models/operations/stoptranscodesessionresponse.md)**
### Errors

| Error Object                            | Status Code                             | Content Type                            |
| --------------------------------------- | --------------------------------------- | --------------------------------------- |
| errors.StopTranscodeSessionResponseBody | 401                                     | application/json                        |
| errors.SDKError                         | 4xx-5xx                                 | */*                                     |
