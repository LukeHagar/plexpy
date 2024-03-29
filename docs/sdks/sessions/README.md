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
    x_plex_client_identifier='<value>',
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
| errors.SDKError                | 4x-5xx                         | */*                            |

## get_session_history

This will Retrieve a listing of all history views.

### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='<value>',
)


res = s.sessions.get_session_history()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.GetSessionHistoryResponse](../../models/operations/getsessionhistoryresponse.md)**
### Errors

| Error Object                         | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| errors.GetSessionHistoryResponseBody | 401                                  | application/json                     |
| errors.SDKError                      | 4x-5xx                               | */*                                  |

## get_transcode_sessions

Get Transcode Sessions

### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='<value>',
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
| errors.SDKError                         | 4x-5xx                                  | */*                                     |

## stop_transcode_session

Stop a Transcode Session

### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='<value>',
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
| errors.SDKError                         | 4x-5xx                                  | */*                                     |
