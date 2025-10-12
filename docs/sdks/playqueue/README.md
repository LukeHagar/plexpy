# PlayQueue
(*play_queue*)

## Overview

The playqueue feature within a media provider
A play queue represents the current list of media for playback. Although queues are persisted by the server, they should be regarded by the user as a fairly lightweight, an ephemeral list of items queued up for playback in a session.  There is generally one active queue for each type of media (music, video, photos) that can be added to or destroyed and replaced with a fresh queue.
Play Queues has a region, which we refer to in this doc (partially for historical reasons) as "Up Next". This region is defined by `playQueueLastAddedItemID` existing on the media container. This follows iTunes' terminology. It is a special region after the currently playing item but before the originally-played items. This enables "Party Mode" listening/viewing, where items can be added on-the-fly, and normal queue playback resumed when completed. 
You can visualize the play queue as a sliding window in the complete list of media queued for playback. This model is important when scaling to larger play queues (e.g. shuffling 40,000 audio tracks). The client only needs visibility into small areas of the queue at any given time, and the server can optimize access in this fashion.
All created play queues will have an empty "Up Next" area - unless the item is an album and no `key` is provided. In this case the "Up Next" area will be populated by the contents of the album. This is to allow queueing of multiple albums - since the 'Add to Up Next' will insert after all the tracks. This means that If you're creating a PQ from an album, you can only shuffle it if you set `key`. This is due to the above implicit queueing of albums when no `key` is provided as well as the current limitation that you cannot shuffle a PQ with an "Up Next" area.
The play queue window advances as the server receives timeline requests. The client needs to retrieve the play queue as the “now playing” item changes. There is no play queue API to update the playing item.

### Available Operations

* [create_play_queue](#create_play_queue) - Create a play queue
* [get_play_queue](#get_play_queue) - Retrieve a play queue
* [add_to_play_queue](#add_to_play_queue) - Add a generator or playlist to a play queue
* [clear_play_queue](#clear_play_queue) - Clear a play queue
* [reset_play_queue](#reset_play_queue) - Reset a play queue
* [shuffle](#shuffle) - Shuffle a play queue
* [unshuffle](#unshuffle) - Unshuffle a play queue
* [delete_play_queue_item](#delete_play_queue_item) - Delete an item from a play queue
* [move_play_queue_item](#move_play_queue_item) - Move an item in a play queue

## create_play_queue

Makes a new play queue for a device. The source of the playqueue can either be a URI, or a playlist. The response is a media container with the initial items in the queue. Each item in the queue will be a regular item but with `playQueueItemID` - a unique ID since the queue could have repeated items with the same `ratingKey`.
Note: Either `uri` or `playlistID` must be specified

### Example Usage

<!-- UsageSnippet language="python" operationID="createPlayQueue" method="post" path="/playQueues" -->
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

    res = plex_api.play_queue.create_play_queue(request=operations.CreatePlayQueueRequest(
        type=operations.Type.AUDIO,
        shuffle=components.BoolInt.ONE,
        repeat=components.BoolInt.ONE,
        continuous=components.BoolInt.ONE,
        recursive=components.BoolInt.ONE,
        on_deck=components.BoolInt.ONE,
    ))

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreatePlayQueueRequest](../../models/operations/createplayqueuerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.CreatePlayQueueResponse](../../models/operations/createplayqueueresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_play_queue

Retrieves the play queue, centered at current item. This can be treated as a regular container by play queue-oblivious clients, but they may wish to request a large window onto the queue since they won't know to refresh.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPlayQueue" method="get" path="/playQueues/{playQueueId}" -->
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

    res = plex_api.play_queue.get_play_queue(request=operations.GetPlayQueueRequest(
        play_queue_id=210646,
        own=components.BoolInt.ONE,
        include_before=components.BoolInt.ONE,
        include_after=components.BoolInt.ONE,
    ))

    assert res.media_container_with_playlist_metadata is not None

    # Handle response
    print(res.media_container_with_playlist_metadata)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetPlayQueueRequest](../../models/operations/getplayqueuerequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.GetPlayQueueResponse](../../models/operations/getplayqueueresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## add_to_play_queue

Adds an item to a play queue (e.g. party mode). Increments the version of the play queue. Takes the following parameters (`uri` and `playlistID` are mutually exclusive). Returns the modified play queue.

### Example Usage

<!-- UsageSnippet language="python" operationID="addToPlayQueue" method="put" path="/playQueues/{playQueueId}" -->
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

    res = plex_api.play_queue.add_to_play_queue(request={
        "play_queue_id": 919248,
        "next": components.BoolInt.ONE,
    })

    assert res.media_container_with_playlist_metadata is not None

    # Handle response
    print(res.media_container_with_playlist_metadata)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.AddToPlayQueueRequest](../../models/operations/addtoplayqueuerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.AddToPlayQueueResponse](../../models/operations/addtoplayqueueresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## clear_play_queue

Deletes all items in the play queue, and increases the version of the play queue.

### Example Usage

<!-- UsageSnippet language="python" operationID="clearPlayQueue" method="delete" path="/playQueues/{playQueueId}/items" -->
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

    res = plex_api.play_queue.clear_play_queue(request={
        "play_queue_id": 86357,
    })

    assert res.media_container_with_playlist_metadata is not None

    # Handle response
    print(res.media_container_with_playlist_metadata)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ClearPlayQueueRequest](../../models/operations/clearplayqueuerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.ClearPlayQueueResponse](../../models/operations/clearplayqueueresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## reset_play_queue

Reset a play queue to the first item being the current item

### Example Usage

<!-- UsageSnippet language="python" operationID="resetPlayQueue" method="put" path="/playQueues/{playQueueId}/reset" -->
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

    res = plex_api.play_queue.reset_play_queue(request={
        "play_queue_id": 581891,
    })

    assert res.media_container_with_playlist_metadata is not None

    # Handle response
    print(res.media_container_with_playlist_metadata)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ResetPlayQueueRequest](../../models/operations/resetplayqueuerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.ResetPlayQueueResponse](../../models/operations/resetplayqueueresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## shuffle

Shuffle a play queue (or reshuffles if already shuffled). The currently selected item is maintained. Note that this is currently only supported for play queues *without* an Up Next area. Returns the modified play queue.

### Example Usage

<!-- UsageSnippet language="python" operationID="shuffle" method="put" path="/playQueues/{playQueueId}/shuffle" -->
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

    res = plex_api.play_queue.shuffle(request={
        "play_queue_id": 316150,
    })

    assert res.media_container_with_playlist_metadata is not None

    # Handle response
    print(res.media_container_with_playlist_metadata)

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.ShuffleRequest](../../models/operations/shufflerequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |

### Response

**[operations.ShuffleResponse](../../models/operations/shuffleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## unshuffle

Unshuffles a play queue and restores "natural order". Note that this is currently only supported for play queues *without* an Up Next area. Returns the modified play queue.

### Example Usage

<!-- UsageSnippet language="python" operationID="unshuffle" method="put" path="/playQueues/{playQueueId}/unshuffle" -->
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

    res = plex_api.play_queue.unshuffle(request={
        "play_queue_id": 484388,
    })

    assert res.media_container_with_playlist_metadata is not None

    # Handle response
    print(res.media_container_with_playlist_metadata)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.UnshuffleRequest](../../models/operations/unshufflerequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[operations.UnshuffleResponse](../../models/operations/unshuffleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_play_queue_item

Deletes an item in a play queue. Increments the version of the play queue. Returns the modified play queue.

### Example Usage

<!-- UsageSnippet language="python" operationID="deletePlayQueueItem" method="delete" path="/playQueues/{playQueueId}/items/{playQueueItemId}" -->
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

    res = plex_api.play_queue.delete_play_queue_item(request={
        "play_queue_id": 285738,
        "play_queue_item_id": 464354,
    })

    assert res.media_container_with_playlist_metadata is not None

    # Handle response
    print(res.media_container_with_playlist_metadata)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.DeletePlayQueueItemRequest](../../models/operations/deleteplayqueueitemrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.DeletePlayQueueItemResponse](../../models/operations/deleteplayqueueitemresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## move_play_queue_item

Moves an item in a play queue, and increases the version of the play queue. Returns the modified play queue.

### Example Usage

<!-- UsageSnippet language="python" operationID="movePlayQueueItem" method="put" path="/playQueues/{playQueueId}/items/{playQueueItemId}/move" -->
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

    res = plex_api.play_queue.move_play_queue_item(request={
        "play_queue_id": 31341,
        "play_queue_item_id": 495865,
    })

    assert res.media_container_with_playlist_metadata is not None

    # Handle response
    print(res.media_container_with_playlist_metadata)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.MovePlayQueueItemRequest](../../models/operations/moveplayqueueitemrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.MovePlayQueueItemResponse](../../models/operations/moveplayqueueitemresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |