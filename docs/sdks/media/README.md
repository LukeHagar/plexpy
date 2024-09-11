# Media
(*media*)

## Overview

API Calls interacting with Plex Media Server Media


### Available Operations

* [mark_played](#mark_played) - Mark Media Played
* [mark_unplayed](#mark_unplayed) - Mark Media Unplayed
* [update_play_progress](#update_play_progress) - Update Media Play Progress
* [get_banner_image](#get_banner_image) - Get Banner Image
* [get_thumb_image](#get_thumb_image) - Get Thumb Image

## mark_played

This will mark the provided media key as Played.

### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier="gcgzw5rz2xovp84b4vha3a40",
)

res = s.media.mark_played(key=59398)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `key`                                                               | *float*                                                             | :heavy_check_mark:                                                  | The media key to mark as played                                     | 59398                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.MarkPlayedResponse](../../models/operations/markplayedresponse.md)**

### Errors

| Error Object                  | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.MarkPlayedBadRequest   | 400                           | application/json              |
| errors.MarkPlayedUnauthorized | 401                           | application/json              |
| errors.SDKError               | 4xx-5xx                       | */*                           |


## mark_unplayed

This will mark the provided media key as Unplayed.

### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier="gcgzw5rz2xovp84b4vha3a40",
)

res = s.media.mark_unplayed(key=59398)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `key`                                                               | *float*                                                             | :heavy_check_mark:                                                  | The media key to mark as Unplayed                                   | 59398                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.MarkUnplayedResponse](../../models/operations/markunplayedresponse.md)**

### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.MarkUnplayedBadRequest   | 400                             | application/json                |
| errors.MarkUnplayedUnauthorized | 401                             | application/json                |
| errors.SDKError                 | 4xx-5xx                         | */*                             |


## update_play_progress

This API command can be used to update the play progress of a media item.


### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier="gcgzw5rz2xovp84b4vha3a40",
)

res = s.media.update_play_progress(key="<key>", time=90000, state="played")

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
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.UpdatePlayProgressResponse](../../models/operations/updateplayprogressresponse.md)**

### Errors

| Error Object                          | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| errors.UpdatePlayProgressBadRequest   | 400                                   | application/json                      |
| errors.UpdatePlayProgressUnauthorized | 401                                   | application/json                      |
| errors.SDKError                       | 4xx-5xx                               | */*                                   |


## get_banner_image

Gets the banner image of the media item

### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier="gcgzw5rz2xovp84b4vha3a40",
)

res = s.media.get_banner_image(request={
    "rating_key": 9518,
    "width": 396,
    "height": 396,
    "min_size": 1,
    "upscale": 1,
    "x_plex_token": "CV5xoxjTpFKUzBTShsaf",
})

if res.response_stream is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetBannerImageRequest](../../models/operations/getbannerimagerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetBannerImageResponse](../../models/operations/getbannerimageresponse.md)**

### Errors

| Error Object                      | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.GetBannerImageBadRequest   | 400                               | application/json                  |
| errors.GetBannerImageUnauthorized | 401                               | application/json                  |
| errors.SDKError                   | 4xx-5xx                           | */*                               |


## get_thumb_image

Gets the thumbnail image of the media item

### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier="gcgzw5rz2xovp84b4vha3a40",
)

res = s.media.get_thumb_image(request={
    "rating_key": 9518,
    "width": 396,
    "height": 396,
    "min_size": 1,
    "upscale": 1,
    "x_plex_token": "CV5xoxjTpFKUzBTShsaf",
})

if res.response_stream is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetThumbImageRequest](../../models/operations/getthumbimagerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.GetThumbImageResponse](../../models/operations/getthumbimageresponse.md)**

### Errors

| Error Object                     | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.GetThumbImageBadRequest   | 400                              | application/json                 |
| errors.GetThumbImageUnauthorized | 401                              | application/json                 |
| errors.SDKError                  | 4xx-5xx                          | */*                              |
