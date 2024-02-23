# Activities
(*activities*)

## Overview

Activities are awesome. They provide a way to monitor and control asynchronous operations on the server. In order to receive real-time updates for activities, a client would normally subscribe via either EventSource or Websocket endpoints.
Activities are associated with HTTP replies via a special `X-Plex-Activity` header which contains the UUID of the activity.
Activities are optional cancellable. If cancellable, they may be cancelled via the `DELETE` endpoint. Other details:
- They can contain a `progress` (from 0 to 100) marking the percent completion of the activity.
- They must contain an `type` which is used by clients to distinguish the specific activity.
- They may contain a `Context` object with attributes which associate the activity with various specific entities (items, libraries, etc.)
- The may contain a `Response` object which attributes which represent the result of the asynchronous operation.


### Available Operations

* [get_server_activities](#get_server_activities) - Get Server Activities
* [cancel_server_activities](#cancel_server_activities) - Cancel Server Activities

## get_server_activities

Get Server Activities

### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
)


res = s.activities.get_server_activities()

if res.object is not None:
    # handle response
    pass
```


### Response

**[operations.GetServerActivitiesResponse](../../models/operations/getserveractivitiesresponse.md)**
### Errors

| Error Object                           | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.GetServerActivitiesResponseBody | 401                                    | application/json                       |
| errors.SDKError                        | 4x-5xx                                 | */*                                    |

## cancel_server_activities

Cancel Server Activities

### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
)


res = s.activities.cancel_server_activities(activity_uuid='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                           | Type                                | Required                            | Description                         |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- |
| `activity_uuid`                     | *str*                               | :heavy_check_mark:                  | The UUID of the activity to cancel. |


### Response

**[operations.CancelServerActivitiesResponse](../../models/operations/cancelserveractivitiesresponse.md)**
### Errors

| Error Object                              | Status Code                               | Content Type                              |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| errors.CancelServerActivitiesResponseBody | 401                                       | application/json                          |
| errors.SDKError                           | 4x-5xx                                    | */*                                       |
