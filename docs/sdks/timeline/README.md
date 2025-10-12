# Timeline
(*timeline*)

## Overview

The actions feature within a media provider

### Available Operations

* [mark_played](#mark_played) - Mark an item as played
* [report](#report) - Report media timeline
* [unscrobble](#unscrobble) - Mark an item as unplayed

## mark_played

Mark an item as played.  Note, this does not create any view history of this item but rather just sets the state as played. The client must provide either the `key` or `uri` query parameter
This API does respond to the GET verb but applications should use PUT

### Example Usage

<!-- UsageSnippet language="python" operationID="markPlayed" method="put" path="/:/scrobble" -->
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

    res = plex_api.timeline.mark_played(request={
        "identifier": "<value>",
        "key": "59398",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.MarkPlayedRequest](../../models/operations/markplayedrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.MarkPlayedResponse](../../models/operations/markplayedresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## report

This endpoint is hit during media playback for an item. It must be hit whenever the play state changes, or in the absence of a play state change, in a regular fashion (generally this means every 10 seconds on a LAN/WAN, and every 20 seconds over cellular).


### Example Usage

<!-- UsageSnippet language="python" operationID="report" method="post" path="/:/timeline" -->
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

    res = plex_api.timeline.report(request=operations.ReportRequest(
        key="/foo",
        rating_key="xyz",
        state=operations.State.PLAYING,
        play_queue_item_id="123",
        time=0,
        duration=10000,
        continuing=components.BoolInt.ONE,
        updated=14200000,
        offline=components.BoolInt.ONE,
        time_to_first_frame=1000,
        time_stalled=1000,
        bandwidth=100,
        buffered_time=100,
        buffered_size=1024,
    ))

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [operations.ReportRequest](../../models/operations/reportrequest.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[operations.ReportResponse](../../models/operations/reportresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## unscrobble

Mark an item as unplayed. The client must provide either the `key` or `uri` query parameter
This API does respond to the GET verb but applications should use PUT

### Example Usage

<!-- UsageSnippet language="python" operationID="unscrobble" method="put" path="/:/unscrobble" -->
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

    res = plex_api.timeline.unscrobble(request={
        "identifier": "<value>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.UnscrobbleRequest](../../models/operations/unscrobblerequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.UnscrobbleResponse](../../models/operations/unscrobbleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |