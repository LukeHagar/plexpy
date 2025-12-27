# DownloadQueue

## Overview

API Operations against the Download Queue

### Available Operations

* [create_download_queue](#create_download_queue) - Create download queue
* [get_download_queue](#get_download_queue) - Get a download queue
* [add_download_queue_items](#add_download_queue_items) - Add to download queue
* [list_download_queue_items](#list_download_queue_items) - Get download queue items
* [get_item_decision](#get_item_decision) - Grab download queue item decision
* [get_download_queue_media](#get_download_queue_media) - Grab download queue media
* [remove_download_queue_items](#remove_download_queue_items) - Delete download queue items
* [get_download_queue_items](#get_download_queue_items) - Get download queue items
* [restart_processing_download_queue_items](#restart_processing_download_queue_items) - Restart processing of items from the decision

## create_download_queue

Available: 0.2.0

Creates a download queue for this client if one doesn't exist, or returns the existing queue for this client and user.


### Example Usage

<!-- UsageSnippet language="python" operationID="createDownloadQueue" method="post" path="/downloadQueue" -->
```python
from plex_api_client import PlexAPI


with PlexAPI(
    token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.download_queue.create_download_queue()

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.CreateDownloadQueueResponse](../../models/operations/createdownloadqueueresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_download_queue

Available: 0.2.0

Get a download queue by its id


### Example Usage

<!-- UsageSnippet language="python" operationID="getDownloadQueue" method="get" path="/downloadQueue/{queueId}" -->
```python
from plex_api_client import PlexAPI
from plex_api_client.models import components


with PlexAPI(
    accepts=components.Accepts.APPLICATION_XML,
    client_identifier="abc123",
    product="Plex for Roku",
    version="2.4.1",
    platform="Roku",
    platform_version="4.3 build 1057",
    device="Roku 3",
    model="4200X",
    device_vendor="Roku",
    device_name="Living Room TV",
    marketplace="googlePlay",
    token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.download_queue.get_download_queue(request={
        "queue_id": 922802,
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetDownloadQueueRequest](../../models/operations/getdownloadqueuerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetDownloadQueueResponse](../../models/operations/getdownloadqueueresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## add_download_queue_items

Available: 0.2.0

Add items to the download queue


### Example Usage

<!-- UsageSnippet language="python" operationID="addDownloadQueueItems" method="post" path="/downloadQueue/{queueId}/add" -->
```python
from plex_api_client import PlexAPI
from plex_api_client.models import components, operations


with PlexAPI(
    accepts=components.Accepts.APPLICATION_XML,
    client_identifier="abc123",
    product="Plex for Roku",
    version="2.4.1",
    platform="Roku",
    platform_version="4.3 build 1057",
    device="Roku 3",
    model="4200X",
    device_vendor="Roku",
    device_name="Living Room TV",
    marketplace="googlePlay",
    token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.download_queue.add_download_queue_items(request=operations.AddDownloadQueueItemsRequest(
        queue_id=984925,
        keys=[
            "/library/metadata/3",
            "/library/metadata/6",
        ],
        advanced_subtitles=components.AdvancedSubtitles.BURN,
        audio_boost=50,
        audio_channel_count=5,
        auto_adjust_quality=components.BoolInt.TRUE,
        auto_adjust_subtitle=components.BoolInt.TRUE,
        direct_play=components.BoolInt.TRUE,
        direct_stream=components.BoolInt.TRUE,
        direct_stream_audio=components.BoolInt.TRUE,
        disable_resolution_rotation=components.BoolInt.TRUE,
        has_mde=components.BoolInt.TRUE,
        location=components.Location.WAN,
        media_buffer_size=102400,
        media_index=0,
        music_bitrate=5000,
        offset=90.5,
        part_index=0,
        path="/library/metadata/151671",
        peak_bitrate=12000,
        photo_resolution="1080x1080",
        protocol=components.Protocol.DASH,
        seconds_per_segment=5,
        subtitle_size=50,
        video_bitrate=12000,
        video_quality=50,
        video_resolution="1080x1080",
    ))

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.AddDownloadQueueItemsRequest](../../models/operations/adddownloadqueueitemsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.AddDownloadQueueItemsResponse](../../models/operations/adddownloadqueueitemsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_download_queue_items

Available: 0.2.0

Get items from a download queue


### Example Usage

<!-- UsageSnippet language="python" operationID="listDownloadQueueItems" method="get" path="/downloadQueue/{queueId}/items" -->
```python
from plex_api_client import PlexAPI
from plex_api_client.models import components


with PlexAPI(
    accepts=components.Accepts.APPLICATION_XML,
    client_identifier="abc123",
    product="Plex for Roku",
    version="2.4.1",
    platform="Roku",
    platform_version="4.3 build 1057",
    device="Roku 3",
    model="4200X",
    device_vendor="Roku",
    device_name="Living Room TV",
    marketplace="googlePlay",
    token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.download_queue.list_download_queue_items(request={
        "queue_id": 524138,
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListDownloadQueueItemsRequest](../../models/operations/listdownloadqueueitemsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListDownloadQueueItemsResponse](../../models/operations/listdownloadqueueitemsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_item_decision

Available: 0.2.0

Grab the decision for a download queue item


### Example Usage

<!-- UsageSnippet language="python" operationID="getItemDecision" method="get" path="/downloadQueue/{queueId}/item/{itemId}/decision" -->
```python
from plex_api_client import PlexAPI
from plex_api_client.models import components


with PlexAPI(
    accepts=components.Accepts.APPLICATION_XML,
    client_identifier="abc123",
    product="Plex for Roku",
    version="2.4.1",
    platform="Roku",
    platform_version="4.3 build 1057",
    device="Roku 3",
    model="4200X",
    device_vendor="Roku",
    device_name="Living Room TV",
    marketplace="googlePlay",
    token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.download_queue.get_item_decision(request={
        "queue_id": 231605,
        "item_id": 32,
    })

    assert res.media_container_with_decision is not None

    # Handle response
    print(res.media_container_with_decision)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetItemDecisionRequest](../../models/operations/getitemdecisionrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetItemDecisionResponse](../../models/operations/getitemdecisionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_download_queue_media

Available: 0.2.0

Grab the media for a download queue item


### Example Usage

<!-- UsageSnippet language="python" operationID="getDownloadQueueMedia" method="get" path="/downloadQueue/{queueId}/item/{itemId}/media" -->
```python
from plex_api_client import PlexAPI
from plex_api_client.models import components


with PlexAPI(
    accepts=components.Accepts.APPLICATION_XML,
    client_identifier="abc123",
    product="Plex for Roku",
    version="2.4.1",
    platform="Roku",
    platform_version="4.3 build 1057",
    device="Roku 3",
    model="4200X",
    device_vendor="Roku",
    device_name="Living Room TV",
    marketplace="googlePlay",
    token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.download_queue.get_download_queue_media(request={
        "queue_id": 663184,
        "item_id": 32,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetDownloadQueueMediaRequest](../../models/operations/getdownloadqueuemediarequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.GetDownloadQueueMediaResponse](../../models/operations/getdownloadqueuemediaresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_download_queue_items

delete items from a download queue

### Example Usage

<!-- UsageSnippet language="python" operationID="removeDownloadQueueItems" method="delete" path="/downloadQueue/{queueId}/items/{itemId}" -->
```python
from plex_api_client import PlexAPI
from plex_api_client.models import components


with PlexAPI(
    accepts=components.Accepts.APPLICATION_XML,
    client_identifier="abc123",
    product="Plex for Roku",
    version="2.4.1",
    platform="Roku",
    platform_version="4.3 build 1057",
    device="Roku 3",
    model="4200X",
    device_vendor="Roku",
    device_name="Living Room TV",
    marketplace="googlePlay",
    token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.download_queue.remove_download_queue_items(request={
        "queue_id": 946275,
        "item_id": [
            32,
            345,
            23,
        ],
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.RemoveDownloadQueueItemsRequest](../../models/operations/removedownloadqueueitemsrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.RemoveDownloadQueueItemsResponse](../../models/operations/removedownloadqueueitemsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_download_queue_items

Available: 0.2.0

Get items from a download queue


### Example Usage

<!-- UsageSnippet language="python" operationID="getDownloadQueueItems" method="get" path="/downloadQueue/{queueId}/items/{itemId}" -->
```python
from plex_api_client import PlexAPI
from plex_api_client.models import components


with PlexAPI(
    accepts=components.Accepts.APPLICATION_XML,
    client_identifier="abc123",
    product="Plex for Roku",
    version="2.4.1",
    platform="Roku",
    platform_version="4.3 build 1057",
    device="Roku 3",
    model="4200X",
    device_vendor="Roku",
    device_name="Living Room TV",
    marketplace="googlePlay",
    token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.download_queue.get_download_queue_items(request={
        "queue_id": 809886,
        "item_id": [
            32,
            345,
            23,
        ],
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetDownloadQueueItemsRequest](../../models/operations/getdownloadqueueitemsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.GetDownloadQueueItemsResponse](../../models/operations/getdownloadqueueitemsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## restart_processing_download_queue_items

Available: 0.2.0

Reprocess download queue items with previous decision parameters


### Example Usage

<!-- UsageSnippet language="python" operationID="restartProcessingDownloadQueueItems" method="post" path="/downloadQueue/{queueId}/items/{itemId}/restart" -->
```python
from plex_api_client import PlexAPI
from plex_api_client.models import components


with PlexAPI(
    accepts=components.Accepts.APPLICATION_XML,
    client_identifier="abc123",
    product="Plex for Roku",
    version="2.4.1",
    platform="Roku",
    platform_version="4.3 build 1057",
    device="Roku 3",
    model="4200X",
    device_vendor="Roku",
    device_name="Living Room TV",
    marketplace="googlePlay",
    token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.download_queue.restart_processing_download_queue_items(request={
        "queue_id": 713001,
        "item_id": [
            32,
            345,
            23,
        ],
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.RestartProcessingDownloadQueueItemsRequest](../../models/operations/restartprocessingdownloadqueueitemsrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |

### Response

**[operations.RestartProcessingDownloadQueueItemsResponse](../../models/operations/restartprocessingdownloadqueueitemsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |