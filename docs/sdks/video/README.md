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

req = operations.GetTimelineRequest(
    rating_key=716.56,
    key='<key>',
    state=operations.State.PAUSED,
    has_mde=7574.33,
    time=3327.51,
    duration=7585.39,
    context='<value>',
    play_queue_item_id=1406.21,
    play_back_time=2699.34,
    row=3536.42,
)

res = s.video.get_timeline(req)

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

req = operations.StartUniversalTranscodeRequest(
    has_mde=8924.99,
    path='/etc/mail',
    media_index=9962.95,
    part_index=1232.82,
    protocol='<value>',
)

res = s.video.start_universal_transcode(req)

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
