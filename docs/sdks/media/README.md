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

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.media.mark_played(key=59398)

if res is not None:
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
| errors.SDKError               | 4xx-5xx                       | */*                           |

## mark_unplayed

This will mark the provided media key as Unplayed.

### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.media.mark_unplayed(key=59398)

if res is not None:
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
| errors.SDKError                 | 4xx-5xx                         | */*                             |

## update_play_progress

This API command can be used to update the play progress of a media item.


### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.media.update_play_progress(key='<value>', time=90000, state='played')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `key`                                                               | *str*                                                               | :heavy_check_mark:                                                  | the media key                                                       |                                                                     |
| `time`                                                              | *float*                                                             | :heavy_check_mark:                                                  | The time, in milliseconds, used to set the media playback progress. | 90000                                                               |
| `state`                                                             | *str*                                                               | :heavy_check_mark:                                                  | The playback state of the media item.                               | played                                                              |


### Response

**[operations.UpdatePlayProgressResponse](../../models/operations/updateplayprogressresponse.md)**
### Errors

| Error Object                          | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| errors.UpdatePlayProgressResponseBody | 401                                   | application/json                      |
| errors.SDKError                       | 4xx-5xx                               | */*                                   |
