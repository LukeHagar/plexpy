# Video
(*video*)

## Overview

API Calls that perform operations with Plex Media Server Videos


### Available Operations

* [get_timeline](#get_timeline) - Get the timeline for a media item
* [start_universal_transcode](#start_universal_transcode) - Start Universal Transcode

## get_timeline

Get the timeline for a media item

### Example Usage

```python
import plex_api
from plex_api.models import operations

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.video.get_timeline(request=operations.GetTimelineRequest(
    rating_key=23409,
    key='/library/metadata/23409',
    state=operations.State.PLAYING,
    has_mde=1,
    time=2000,
    duration=10000,
    context='home:hub.continueWatching',
    play_queue_item_id=1,
    play_back_time=2000,
    row=1,
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetTimelineRequest](../../models/operations/gettimelinerequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetTimelineResponse](../../models/operations/gettimelineresponse.md)**
### Errors

| Error Object                   | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| errors.GetTimelineResponseBody | 401                            | application/json               |
| errors.SDKError                | 4xx-5xx                        | */*                            |

## start_universal_transcode

Begin a Universal Transcode Session

### Example Usage

```python
import plex_api
from plex_api.models import operations

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.video.start_universal_transcode(request=operations.StartUniversalTranscodeRequest(
    has_mde=1,
    path='/library/metadata/23409',
    media_index=0,
    part_index=0,
    protocol='hls',
    fast_seek=0,
    direct_play=0,
    direct_stream=0,
    subtitle_size=100,
    subtites='burn',
    audio_boost=100,
    location='lan',
    media_buffer_size=102400,
    session='zvcage8b7rkioqcm8f4uns4c',
    add_debug_overlay=0,
    auto_adjust_quality=0,
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.StartUniversalTranscodeRequest](../../models/operations/startuniversaltranscoderequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.StartUniversalTranscodeResponse](../../models/operations/startuniversaltranscoderesponse.md)**
### Errors

| Error Object                               | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| errors.StartUniversalTranscodeResponseBody | 401                                        | application/json                           |
| errors.SDKError                            | 4xx-5xx                                    | */*                                        |
