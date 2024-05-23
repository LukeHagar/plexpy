# Library
(*library*)

## Overview

API Calls interacting with Plex Media Server Libraries


### Available Operations

* [get_file_hash](#get_file_hash) - Get Hash Value
* [get_recently_added](#get_recently_added) - Get Recently Added
* [get_libraries](#get_libraries) - Get All Libraries
* [get_library](#get_library) - Get Library Details
* [delete_library](#delete_library) - Delete Library Section
* [get_library_items](#get_library_items) - Get Library Items
* [refresh_library](#refresh_library) - Refresh Library
* [search_library](#search_library) - Search Library
* [get_metadata](#get_metadata) - Get Items Metadata
* [get_metadata_children](#get_metadata_children) - Get Items Children
* [get_on_deck](#get_on_deck) - Get On Deck

## get_file_hash

This resource returns hash values for local files

### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.library.get_file_hash(url='file://C:\Image.png&type=13', type=4462.17)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                         | Type                                                              | Required                                                          | Description                                                       | Example                                                           |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `url`                                                             | *str*                                                             | :heavy_check_mark:                                                | This is the path to the local file, must be prefixed by `file://` | file://C:\Image.png&type=13                                       |
| `type`                                                            | *Optional[float]*                                                 | :heavy_minus_sign:                                                | Item type                                                         |                                                                   |


### Response

**[operations.GetFileHashResponse](../../models/operations/getfilehashresponse.md)**
### Errors

| Error Object                   | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| errors.GetFileHashResponseBody | 401                            | application/json               |
| errors.SDKError                | 4xx-5xx                        | */*                            |

## get_recently_added

This endpoint will return the recently added content.


### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.library.get_recently_added()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.GetRecentlyAddedResponse](../../models/operations/getrecentlyaddedresponse.md)**
### Errors

| Error Object                        | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| errors.GetRecentlyAddedResponseBody | 401                                 | application/json                    |
| errors.SDKError                     | 4xx-5xx                             | */*                                 |

## get_libraries

A library section (commonly referred to as just a library) is a collection of media. 
Libraries are typed, and depending on their type provide either a flat or a hierarchical view of the media. 
For example, a music library has an artist > albums > tracks structure, whereas a movie library is flat.

Libraries have features beyond just being a collection of media; for starters, they include information about supported types, filters and sorts. 
This allows a client to provide a rich interface around the media (e.g. allow sorting movies by release year).


### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.library.get_libraries()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.GetLibrariesResponse](../../models/operations/getlibrariesresponse.md)**
### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.GetLibrariesResponseBody | 401                             | application/json                |
| errors.SDKError                 | 4xx-5xx                         | */*                             |

## get_library

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
import plex_api
from plex_api.models import operations

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.library.get_library(section_id=1000, include_details=operations.IncludeDetails.ZERO)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                  | Type                                                                                                                                                                                       | Required                                                                                                                                                                                   | Description                                                                                                                                                                                | Example                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `section_id`                                                                                                                                                                               | *float*                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                         | the Id of the library to query                                                                                                                                                             | 1000                                                                                                                                                                                       |
| `include_details`                                                                                                                                                                          | [Optional[operations.IncludeDetails]](../../models/operations/includedetails.md)                                                                                                           | :heavy_minus_sign:                                                                                                                                                                         | Whether or not to include details for a section (types, filters, and sorts). <br/>Only exists for backwards compatibility, media providers other than the server libraries have it on always.<br/> |                                                                                                                                                                                            |


### Response

**[operations.GetLibraryResponse](../../models/operations/getlibraryresponse.md)**
### Errors

| Error Object                  | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.GetLibraryResponseBody | 401                           | application/json              |
| errors.SDKError               | 4xx-5xx                       | */*                           |

## delete_library

Delate a library using a specific section

### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.library.delete_library(section_id=1000)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                      | Type                           | Required                       | Description                    | Example                        |
| ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ |
| `section_id`                   | *float*                        | :heavy_check_mark:             | the Id of the library to query | 1000                           |


### Response

**[operations.DeleteLibraryResponse](../../models/operations/deletelibraryresponse.md)**
### Errors

| Error Object                     | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.DeleteLibraryResponseBody | 401                              | application/json                 |
| errors.SDKError                  | 4xx-5xx                          | */*                              |

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
import plex_api
from plex_api.models import operations

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.library.get_library_items(section_id=1, tag=operations.Tag.GENRE)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                             | Type                                                  | Required                                              | Description                                           | Example                                               |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `section_id`                                          | *int*                                                 | :heavy_check_mark:                                    | the Id of the library to query                        | 1                                                     |
| `tag`                                                 | [operations.Tag](../../models/operations/tag.md)      | :heavy_check_mark:                                    | A key representing a specific tag within the section. |                                                       |


### Response

**[operations.GetLibraryItemsResponse](../../models/operations/getlibraryitemsresponse.md)**
### Errors

| Error Object                       | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.GetLibraryItemsResponseBody | 401                                | application/json                   |
| errors.SDKError                    | 4xx-5xx                            | */*                                |

## refresh_library

This endpoint Refreshes the library.


### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.library.refresh_library(section_id=934.16)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                        | Type                             | Required                         | Description                      |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `section_id`                     | *float*                          | :heavy_check_mark:               | the Id of the library to refresh |


### Response

**[operations.RefreshLibraryResponse](../../models/operations/refreshlibraryresponse.md)**
### Errors

| Error Object                      | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.RefreshLibraryResponseBody | 401                               | application/json                  |
| errors.SDKError                   | 4xx-5xx                           | */*                               |

## search_library

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
import plex_api
from plex_api.models import operations

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.library.search_library(section_id=933505, type=operations.Type.FOUR)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                          | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `section_id`                                       | *int*                                              | :heavy_check_mark:                                 | the Id of the library to query                     |
| `type`                                             | [operations.Type](../../models/operations/type.md) | :heavy_check_mark:                                 | Plex content type to search for                    |


### Response

**[operations.SearchLibraryResponse](../../models/operations/searchlibraryresponse.md)**
### Errors

| Error Object                     | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.SearchLibraryResponseBody | 401                              | application/json                 |
| errors.SDKError                  | 4xx-5xx                          | */*                              |

## get_metadata

This endpoint will return the metadata of a library item specified with the ratingKey.


### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.library.get_metadata(rating_key=8382.31)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                             | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `rating_key`                                          | *float*                                               | :heavy_check_mark:                                    | the id of the library item to return the children of. |


### Response

**[operations.GetMetadataResponse](../../models/operations/getmetadataresponse.md)**
### Errors

| Error Object                   | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| errors.GetMetadataResponseBody | 401                            | application/json               |
| errors.SDKError                | 4xx-5xx                        | */*                            |

## get_metadata_children

This endpoint will return the children of of a library item specified with the ratingKey.


### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.library.get_metadata_children(rating_key=1539.14)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                             | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `rating_key`                                          | *float*                                               | :heavy_check_mark:                                    | the id of the library item to return the children of. |


### Response

**[operations.GetMetadataChildrenResponse](../../models/operations/getmetadatachildrenresponse.md)**
### Errors

| Error Object                           | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.GetMetadataChildrenResponseBody | 401                                    | application/json                       |
| errors.SDKError                        | 4xx-5xx                                | */*                                    |

## get_on_deck

This endpoint will return the on deck content.


### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='Postman',
)


res = s.library.get_on_deck()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.GetOnDeckResponse](../../models/operations/getondeckresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.GetOnDeckResponseBody | 401                          | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |
