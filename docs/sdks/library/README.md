# Library
(*library*)

## Overview

API Calls interacting with Plex Media Server Libraries


### Available Operations

* [get_file_hash](#get_file_hash) - Get Hash Value
* [get_recently_added_library](#get_recently_added_library) - Get Recently Added
* [get_all_libraries](#get_all_libraries) - Get All Libraries
* [get_library_details](#get_library_details) - Get Library Details
* [delete_library](#delete_library) - Delete Library Section
* [get_library_items](#get_library_items) - Get Library Items
* [get_refresh_library_metadata](#get_refresh_library_metadata) - Refresh Metadata Of The Library
* [get_search_library](#get_search_library) - Search Library
* [get_search_all_libraries](#get_search_all_libraries) - Search All Libraries
* [get_meta_data_by_rating_key](#get_meta_data_by_rating_key) - Get Metadata by RatingKey
* [get_metadata_children](#get_metadata_children) - Get Items Children
* [get_top_watched_content](#get_top_watched_content) - Get Top Watched Content
* [get_on_deck](#get_on_deck) - Get On Deck

## get_file_hash

This resource returns hash values for local files

### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    client_id="3381b62b-9ab7-4e37-827b-203e9809eb58",
    client_name="Plex for Roku",
    client_version="2.4.1",
    platform="Roku",
    device_nickname="Roku 3",
)

res = s.library.get_file_hash(url="file://C:\Image.png&type=13")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `url`                                                               | *str*                                                               | :heavy_check_mark:                                                  | This is the path to the local file, must be prefixed by `file://`   | file://C:\Image.png&type=13                                         |
| `type`                                                              | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | Item type                                                           |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.GetFileHashResponse](../../models/operations/getfilehashresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| errors.GetFileHashBadRequest   | 400                            | application/json               |
| errors.GetFileHashUnauthorized | 401                            | application/json               |
| errors.SDKError                | 4XX, 5XX                       | \*/\*                          |

## get_recently_added_library

This endpoint will return the recently added content.


### Example Usage

```python
from plex_api_client import PlexAPI
from plex_api_client.models import operations

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    client_id="3381b62b-9ab7-4e37-827b-203e9809eb58",
    client_name="Plex for Roku",
    client_version="2.4.1",
    platform="Roku",
    device_nickname="Roku 3",
)

res = s.library.get_recently_added_library(request={
    "type": operations.QueryParamType.TV_SHOW,
    "content_directory_id": 2,
    "pinned_content_directory_id": [
        3,
        5,
        7,
        13,
        12,
        1,
        6,
        14,
        2,
        10,
        16,
        17,
    ],
    "section_id": 2,
    "include_meta": operations.QueryParamIncludeMeta.ENABLE,
    "x_plex_container_start": 0,
    "x_plex_container_size": 50,
})

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetRecentlyAddedLibraryRequest](../../models/operations/getrecentlyaddedlibraryrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.GetRecentlyAddedLibraryResponse](../../models/operations/getrecentlyaddedlibraryresponse.md)**

### Errors

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| errors.GetRecentlyAddedLibraryBadRequest   | 400                                        | application/json                           |
| errors.GetRecentlyAddedLibraryUnauthorized | 401                                        | application/json                           |
| errors.SDKError                            | 4XX, 5XX                                   | \*/\*                                      |

## get_all_libraries

A library section (commonly referred to as just a library) is a collection of media. 
Libraries are typed, and depending on their type provide either a flat or a hierarchical view of the media. 
For example, a music library has an artist > albums > tracks structure, whereas a movie library is flat.

Libraries have features beyond just being a collection of media; for starters, they include information about supported types, filters and sorts. 
This allows a client to provide a rich interface around the media (e.g. allow sorting movies by release year).


### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    client_id="3381b62b-9ab7-4e37-827b-203e9809eb58",
    client_name="Plex for Roku",
    client_version="2.4.1",
    platform="Roku",
    device_nickname="Roku 3",
)

res = s.library.get_all_libraries()

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetAllLibrariesResponse](../../models/operations/getalllibrariesresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.GetAllLibrariesBadRequest   | 400                                | application/json                   |
| errors.GetAllLibrariesUnauthorized | 401                                | application/json                   |
| errors.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## get_library_details

## Library Details Endpoint

This endpoint provides comprehensive details about the library, focusing on organizational aspects rather than the content itself.   

The details include:

### Directories
Organized into three categories:

- **Primary Directories**: 
  - Used in some clients for quick access to media subsets (e.g., "All", "On Deck").
  - Most can be replicated via media queries.
  - Customizable by users.

- **Secondary Directories**:
  - Marked with `secondary="1"`.
  - Used in older clients for structured navigation.

- **Special Directories**:
  - Includes a "By Folder" entry for filesystem-based browsing.
  - Contains an obsolete `search="1"` entry for on-the-fly search dialog creation.

### Types
Each type in the library comes with a set of filters and sorts, aiding in building dynamic media controls:

- **Type Object Attributes**:
  - `key`: Endpoint for the media list of this type.
  - `type`: Metadata type (if standard Plex type).
  - `title`: Title for this content type (e.g., "Movies").

- **Filter Objects**:
  - Subset of the media query language.
  - Attributes include `filter` (name), `filterType` (data type), `key` (endpoint for value range), and `title`.

- **Sort Objects**:
  - Description of sort fields.
  - Attributes include `defaultDirection` (asc/desc), `descKey` and `key` (sort parameters), and `title`.

> **Note**: Filters and sorts are optional; without them, no filtering controls are rendered.


### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    client_id="3381b62b-9ab7-4e37-827b-203e9809eb58",
    client_name="Plex for Roku",
    client_version="2.4.1",
    platform="Roku",
    device_nickname="Roku 3",
)

res = s.library.get_library_details(section_key=9518)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                  | Type                                                                                                                                                                                       | Required                                                                                                                                                                                   | Description                                                                                                                                                                                | Example                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `section_key`                                                                                                                                                                              | *int*                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                         | The unique key of the Plex library. <br/>Note: This is unique in the context of the Plex server.<br/>                                                                                      | 9518                                                                                                                                                                                       |
| `include_details`                                                                                                                                                                          | [Optional[operations.IncludeDetails]](../../models/operations/includedetails.md)                                                                                                           | :heavy_minus_sign:                                                                                                                                                                         | Whether or not to include details for a section (types, filters, and sorts). <br/>Only exists for backwards compatibility, media providers other than the server libraries have it on always.<br/> |                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                        |                                                                                                                                                                                            |

### Response

**[operations.GetLibraryDetailsResponse](../../models/operations/getlibrarydetailsresponse.md)**

### Errors

| Error Type                           | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| errors.GetLibraryDetailsBadRequest   | 400                                  | application/json                     |
| errors.GetLibraryDetailsUnauthorized | 401                                  | application/json                     |
| errors.SDKError                      | 4XX, 5XX                             | \*/\*                                |

## delete_library

Delete a library using a specific section id

### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    client_id="3381b62b-9ab7-4e37-827b-203e9809eb58",
    client_name="Plex for Roku",
    client_version="2.4.1",
    platform="Roku",
    device_nickname="Roku 3",
)

res = s.library.delete_library(section_key=9518)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   | Example                                                                                       |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `section_key`                                                                                 | *int*                                                                                         | :heavy_check_mark:                                                                            | The unique key of the Plex library. <br/>Note: This is unique in the context of the Plex server.<br/> | 9518                                                                                          |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |                                                                                               |

### Response

**[operations.DeleteLibraryResponse](../../models/operations/deletelibraryresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.DeleteLibraryBadRequest   | 400                              | application/json                 |
| errors.DeleteLibraryUnauthorized | 401                              | application/json                 |
| errors.SDKError                  | 4XX, 5XX                         | \*/\*                            |

## get_library_items

Fetches details from a specific section of the library identified by a section key and a tag. The tag parameter accepts the following values:
- `all`: All items in the section.
- `unwatched`: Items that have not been played.
- `newest`: Items that are recently released.
- `recentlyAdded`: Items that are recently added to the library.
- `recentlyViewed`: Items that were recently viewed.
- `onDeck`: Items to continue watching.
- `collection`: Items categorized by collection.
- `edition`: Items categorized by edition.
- `genre`: Items categorized by genre.
- `year`: Items categorized by year of release.
- `decade`: Items categorized by decade.
- `director`: Items categorized by director.
- `actor`: Items categorized by starring actor.
- `country`: Items categorized by country of origin.
- `contentRating`: Items categorized by content rating.
- `rating`: Items categorized by rating.
- `resolution`: Items categorized by resolution.
- `firstCharacter`: Items categorized by the first letter.
- `folder`: Items categorized by folder.


### Example Usage

```python
from plex_api_client import PlexAPI
from plex_api_client.models import operations

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    client_id="3381b62b-9ab7-4e37-827b-203e9809eb58",
    client_name="Plex for Roku",
    client_version="2.4.1",
    platform="Roku",
    device_nickname="Roku 3",
)

res = s.library.get_library_items(request={
    "tag": operations.Tag.EDITION,
    "section_key": 9518,
    "include_guids": operations.IncludeGuids.ENABLE,
    "type": operations.GetLibraryItemsQueryParamType.TV_SHOW,
    "include_meta": operations.GetLibraryItemsQueryParamIncludeMeta.ENABLE,
    "x_plex_container_start": 0,
    "x_plex_container_size": 50,
})

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetLibraryItemsRequest](../../models/operations/getlibraryitemsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetLibraryItemsResponse](../../models/operations/getlibraryitemsresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.GetLibraryItemsBadRequest   | 400                                | application/json                   |
| errors.GetLibraryItemsUnauthorized | 401                                | application/json                   |
| errors.SDKError                    | 4XX, 5XX                           | \*/\*                              |

## get_refresh_library_metadata

This endpoint Refreshes all the Metadata of the library.


### Example Usage

```python
from plex_api_client import PlexAPI
from plex_api_client.models import operations

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    client_id="3381b62b-9ab7-4e37-827b-203e9809eb58",
    client_name="Plex for Roku",
    client_version="2.4.1",
    platform="Roku",
    device_nickname="Roku 3",
)

res = s.library.get_refresh_library_metadata(section_key=9518, force=operations.Force.ONE)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   | Example                                                                                       |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `section_key`                                                                                 | *int*                                                                                         | :heavy_check_mark:                                                                            | The unique key of the Plex library. <br/>Note: This is unique in the context of the Plex server.<br/> | 9518                                                                                          |
| `force`                                                                                       | [Optional[operations.Force]](../../models/operations/force.md)                                | :heavy_minus_sign:                                                                            | Force the refresh even if the library is already being refreshed.                             | 0                                                                                             |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |                                                                                               |

### Response

**[operations.GetRefreshLibraryMetadataResponse](../../models/operations/getrefreshlibrarymetadataresponse.md)**

### Errors

| Error Type                                   | Status Code                                  | Content Type                                 |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| errors.GetRefreshLibraryMetadataBadRequest   | 400                                          | application/json                             |
| errors.GetRefreshLibraryMetadataUnauthorized | 401                                          | application/json                             |
| errors.SDKError                              | 4XX, 5XX                                     | \*/\*                                        |

## get_search_library

Search for content within a specific section of the library.

### Types
Each type in the library comes with a set of filters and sorts, aiding in building dynamic media controls:

- **Type Object Attributes**:
  - `type`: Metadata type (if standard Plex type).  
  - `title`: Title for this content type (e.g., "Movies").

- **Filter Objects**:
  - Subset of the media query language.
  - Attributes include `filter` (name), `filterType` (data type), `key` (endpoint for value range), and `title`.

- **Sort Objects**:
  - Description of sort fields.
  - Attributes include `defaultDirection` (asc/desc), `descKey` and `key` (sort parameters), and `title`.

> **Note**: Filters and sorts are optional; without them, no filtering controls are rendered.


### Example Usage

```python
from plex_api_client import PlexAPI
from plex_api_client.models import operations

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    client_id="3381b62b-9ab7-4e37-827b-203e9809eb58",
    client_name="Plex for Roku",
    client_version="2.4.1",
    platform="Roku",
    device_nickname="Roku 3",
)

res = s.library.get_search_library(section_key=9518, type_=operations.GetSearchLibraryQueryParamType.TV_SHOW)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                       | Type                                                                                                                                                                            | Required                                                                                                                                                                        | Description                                                                                                                                                                     | Example                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `section_key`                                                                                                                                                                   | *int*                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                              | The unique key of the Plex library. <br/>Note: This is unique in the context of the Plex server.<br/>                                                                           | 9518                                                                                                                                                                            |
| `type`                                                                                                                                                                          | [operations.GetSearchLibraryQueryParamType](../../models/operations/getsearchlibraryqueryparamtype.md)                                                                          | :heavy_check_mark:                                                                                                                                                              | The type of media to retrieve.<br/>1 = movie<br/>2 = show<br/>3 = season<br/>4 = episode<br/>E.g. A movie library will not return anything with type 3 as there are no seasons for movie libraries<br/> | 2                                                                                                                                                                               |
| `retries`                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                | :heavy_minus_sign:                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                             |                                                                                                                                                                                 |

### Response

**[operations.GetSearchLibraryResponse](../../models/operations/getsearchlibraryresponse.md)**

### Errors

| Error Type                          | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| errors.GetSearchLibraryBadRequest   | 400                                 | application/json                    |
| errors.GetSearchLibraryUnauthorized | 401                                 | application/json                    |
| errors.SDKError                     | 4XX, 5XX                            | \*/\*                               |

## get_search_all_libraries

Search the provided query across all library sections, or a single section, and return matches as hubs, split up by type.


### Example Usage

```python
from plex_api_client import PlexAPI
from plex_api_client.models import operations

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    client_id="3381b62b-9ab7-4e37-827b-203e9809eb58",
    client_name="Plex for Roku",
    client_version="2.4.1",
    platform="Roku",
    device_nickname="Roku 3",
)

res = s.library.get_search_all_libraries(request={
    "query": "<value>",
    "search_types": [
        operations.SearchTypes.PEOPLE,
    ],
    "include_collections": operations.QueryParamIncludeCollections.ENABLE,
    "include_external_media": operations.QueryParamIncludeExternalMedia.ENABLE,
})

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetSearchAllLibrariesRequest](../../models/operations/getsearchalllibrariesrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.GetSearchAllLibrariesResponse](../../models/operations/getsearchalllibrariesresponse.md)**

### Errors

| Error Type                               | Status Code                              | Content Type                             |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| errors.GetSearchAllLibrariesBadRequest   | 400                                      | application/json                         |
| errors.GetSearchAllLibrariesUnauthorized | 401                                      | application/json                         |
| errors.SDKError                          | 4XX, 5XX                                 | \*/\*                                    |

## get_meta_data_by_rating_key

This endpoint will return the metadata of a library item specified with the ratingKey.


### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    client_id="3381b62b-9ab7-4e37-827b-203e9809eb58",
    client_name="Plex for Roku",
    client_version="2.4.1",
    platform="Roku",
    device_nickname="Roku 3",
)

res = s.library.get_meta_data_by_rating_key(rating_key=9518)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `rating_key`                                                        | *int*                                                               | :heavy_check_mark:                                                  | the id of the library item to return the children of.               | 9518                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.GetMetaDataByRatingKeyResponse](../../models/operations/getmetadatabyratingkeyresponse.md)**

### Errors

| Error Type                                | Status Code                               | Content Type                              |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| errors.GetMetaDataByRatingKeyBadRequest   | 400                                       | application/json                          |
| errors.GetMetaDataByRatingKeyUnauthorized | 401                                       | application/json                          |
| errors.SDKError                           | 4XX, 5XX                                  | \*/\*                                     |

## get_metadata_children

This endpoint will return the children of of a library item specified with the ratingKey.


### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    client_id="3381b62b-9ab7-4e37-827b-203e9809eb58",
    client_name="Plex for Roku",
    client_version="2.4.1",
    platform="Roku",
    device_nickname="Roku 3",
)

res = s.library.get_metadata_children(rating_key=1539.14, include_elements="Stream")

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `rating_key`                                                            | *float*                                                                 | :heavy_check_mark:                                                      | the id of the library item to return the children of.                   |
| `include_elements`                                                      | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Adds additional elements to the response. Supported types are (Stream)<br/> |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[operations.GetMetadataChildrenResponse](../../models/operations/getmetadatachildrenresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.GetMetadataChildrenBadRequest   | 400                                    | application/json                       |
| errors.GetMetadataChildrenUnauthorized | 401                                    | application/json                       |
| errors.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

## get_top_watched_content

This endpoint will return the top watched content from libraries of a certain type


### Example Usage

```python
from plex_api_client import PlexAPI
from plex_api_client.models import operations

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    client_id="3381b62b-9ab7-4e37-827b-203e9809eb58",
    client_name="Plex for Roku",
    client_version="2.4.1",
    platform="Roku",
    device_nickname="Roku 3",
)

res = s.library.get_top_watched_content(type_=operations.GetTopWatchedContentQueryParamType.TV_SHOW, include_guids=1)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                       | Type                                                                                                                                                                            | Required                                                                                                                                                                        | Description                                                                                                                                                                     | Example                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`                                                                                                                                                                          | [operations.GetTopWatchedContentQueryParamType](../../models/operations/gettopwatchedcontentqueryparamtype.md)                                                                  | :heavy_check_mark:                                                                                                                                                              | The type of media to retrieve.<br/>1 = movie<br/>2 = show<br/>3 = season<br/>4 = episode<br/>E.g. A movie library will not return anything with type 3 as there are no seasons for movie libraries<br/> | 2                                                                                                                                                                               |
| `include_guids`                                                                                                                                                                 | *Optional[int]*                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                              | Adds the Guids object to the response<br/>                                                                                                                                      | 1                                                                                                                                                                               |
| `retries`                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                | :heavy_minus_sign:                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                             |                                                                                                                                                                                 |

### Response

**[operations.GetTopWatchedContentResponse](../../models/operations/gettopwatchedcontentresponse.md)**

### Errors

| Error Type                              | Status Code                             | Content Type                            |
| --------------------------------------- | --------------------------------------- | --------------------------------------- |
| errors.GetTopWatchedContentBadRequest   | 400                                     | application/json                        |
| errors.GetTopWatchedContentUnauthorized | 401                                     | application/json                        |
| errors.SDKError                         | 4XX, 5XX                                | \*/\*                                   |

## get_on_deck

This endpoint will return the on deck content.


### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    client_id="3381b62b-9ab7-4e37-827b-203e9809eb58",
    client_name="Plex for Roku",
    client_version="2.4.1",
    platform="Roku",
    device_nickname="Roku 3",
)

res = s.library.get_on_deck()

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetOnDeckResponse](../../models/operations/getondeckresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.GetOnDeckBadRequest   | 400                          | application/json             |
| errors.GetOnDeckUnauthorized | 401                          | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |