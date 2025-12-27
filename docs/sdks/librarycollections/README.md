# LibraryCollections

## Overview

Endpoints for manipulating collections.  In addition to these endpoints, `/library/collections/:collectionId/X` will be rerouted to `/library/metadata/:collectionId/X` and respond to those endpoints as well.

### Available Operations

* [add_collection_items](#add_collection_items) - Add items to a collection
* [delete_collection_item](#delete_collection_item) - Delete an item from a collection
* [move_collection_item](#move_collection_item) - Reorder an item in the collection

## add_collection_items

Add items to a collection by uri

### Example Usage

<!-- UsageSnippet language="python" operationID="addCollectionItems" method="put" path="/library/collections/{collectionId}/items" -->
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

    res = plex_api.library_collections.add_collection_items(request={
        "collection_id": 338144,
        "uri": "https://expensive-bakeware.com",
    })

    assert res.media_container_with_metadata is not None

    # Handle response
    print(res.media_container_with_metadata)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.AddCollectionItemsRequest](../../models/operations/addcollectionitemsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.AddCollectionItemsResponse](../../models/operations/addcollectionitemsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_collection_item

Delete an item from a collection

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteCollectionItem" method="put" path="/library/collections/{collectionId}/items/{itemId}" -->
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

    res = plex_api.library_collections.delete_collection_item(request={
        "collection_id": 320928,
        "item_id": 406983,
    })

    assert res.media_container_with_metadata is not None

    # Handle response
    print(res.media_container_with_metadata)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.DeleteCollectionItemRequest](../../models/operations/deletecollectionitemrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.DeleteCollectionItemResponse](../../models/operations/deletecollectionitemresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## move_collection_item

Reorder items in a collection with one item after another

### Example Usage

<!-- UsageSnippet language="python" operationID="moveCollectionItem" method="put" path="/library/collections/{collectionId}/items/{itemId}/move" -->
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

    res = plex_api.library_collections.move_collection_item(request={
        "collection_id": 239532,
        "item_id": 513864,
    })

    assert res.media_container_with_metadata is not None

    # Handle response
    print(res.media_container_with_metadata)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.MoveCollectionItemRequest](../../models/operations/movecollectionitemrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.MoveCollectionItemResponse](../../models/operations/movecollectionitemresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |