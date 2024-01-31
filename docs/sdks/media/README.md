# Media
(*media*)

## Overview

API Calls interacting with Plex Media Server Media


### Available Operations

* [mark_played](#mark_played) - Mark Media Played
* [mark_unplayed](#mark_unplayed) - Mark Media Unplayed
* [update_play_progress](#update_play_progress) - Update Media Play Progress

## mark_played

This will mark the provided media key as Played.

### Example Usage

```python
import plex_api
from plex_api.models import operations

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
)


res = s.media.mark_played(key=59398)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                       | Type                            | Required                        | Description                     | Example                         |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `key`                           | *float*                         | :heavy_check_mark:              | The media key to mark as played | 59398                           |


### Response

**[operations.MarkPlayedResponse](../../models/operations/markplayedresponse.md)**
### Errors

| Error Object                  | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.MarkPlayedResponseBody | 401                           | application/json              |
| errors.SDKError               | 4x-5xx                        | */*                           |

## mark_unplayed

This will mark the provided media key as Unplayed.

### Example Usage

```python
import plex_api
from plex_api.models import operations

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
)


res = s.media.mark_unplayed(key=59398)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                         | Type                              | Required                          | Description                       | Example                           |
| --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- |
| `key`                             | *float*                           | :heavy_check_mark:                | The media key to mark as Unplayed | 59398                             |


### Response

**[operations.MarkUnplayedResponse](../../models/operations/markunplayedresponse.md)**
### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.MarkUnplayedResponseBody | 401                             | application/json                |
| errors.SDKError                 | 4x-5xx                          | */*                             |

## update_play_progress

This API command can be used to update the play progress of a media item.


### Example Usage

```python
import plex_api
from plex_api.models import operations

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
)


res = s.media.update_play_progress(key='string', time=6900.91, state='string')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `key`                                                               | *str*                                                               | :heavy_check_mark:                                                  | the media key                                                       |
| `time`                                                              | *float*                                                             | :heavy_check_mark:                                                  | The time, in milliseconds, used to set the media playback progress. |
| `state`                                                             | *str*                                                               | :heavy_check_mark:                                                  | The playback state of the media item.                               |


### Response

**[operations.UpdatePlayProgressResponse](../../models/operations/updateplayprogressresponse.md)**
### Errors

| Error Object                          | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| errors.UpdatePlayProgressResponseBody | 401                                   | application/json                      |
| errors.SDKError                       | 4x-5xx                                | */*                                   |
