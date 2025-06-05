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
* [get_library_sections_all](#get_library_sections_all) - Get Library section media by tag ALL
* [get_refresh_library_metadata](#get_refresh_library_metadata) - Refresh Metadata Of The Library
* [get_search_library](#get_search_library) - Search Library
* [get_genres_library](#get_genres_library) - Get Genres of library media
* [get_countries_library](#get_countries_library) - Get Countries of library media
* [get_actors_library](#get_actors_library) - Get Actors of library media
* [get_search_all_libraries](#get_search_all_libraries) - Search All Libraries
* [get_media_meta_data](#get_media_meta_data) - Get Media Metadata
* [get_media_arts](#get_media_arts) - Get Media Background Artwork
* [post_media_arts](#post_media_arts) - Upload Media Background Artwork
* [get_media_posters](#get_media_posters) - Get Media Posters
* [post_media_poster](#post_media_poster) - Upload Media Poster
* [get_metadata_children](#get_metadata_children) - Get Items Children
* [get_top_watched_content](#get_top_watched_content) - Get Top Watched Content

## get_file_hash

This resource returns hash values for local files

### Example Usage

```python
from plex_api_client import PlexAPI


with PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.library.get_file_hash(url="file://C:\Image.png&type=13")

    assert res is not None

    # Handle response
    print(res)

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


with PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.library.get_recently_added_library(request={
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
        "type": operations.QueryParamType.TV_SHOW,
        "include_meta": operations.QueryParamIncludeMeta.ENABLE,
    })

    assert res.object is not None

    # Handle response
    print(res.object)

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


with PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.library.get_all_libraries()

    assert res.object is not None

    # Handle response
    print(res.object)

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
from plex_api_client.models import operations


with PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.library.get_library_details(section_key=9518, include_details=operations.IncludeDetails.ZERO)

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                                                                                                                 | Type                                                                                                                                                                                      | Required                                                                                                                                                                                  | Description                                                                                                                                                                               | Example                                                                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `section_key`                                                                                                                                                                             | *int*                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                        | The unique key of the Plex library. <br/>Note: This is unique in the context of the Plex server.<br/>                                                                                     | 9518                                                                                                                                                                                      |
| `include_details`                                                                                                                                                                         | [Optional[operations.IncludeDetails]](../../models/operations/includedetails.md)                                                                                                          | :heavy_minus_sign:                                                                                                                                                                        | Whether or not to include details for a section (types, filters, and sorts).<br/>Only exists for backwards compatibility, media providers other than the server libraries have it on always.<br/> |                                                                                                                                                                                           |
| `retries`                                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                                       |                                                                                                                                                                                           |

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


with PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.library.delete_library(section_key=9518)

    assert res is not None

    # Handle response
    print(res)

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
- `albums`: Items categorized by album.


### Example Usage

```python
from plex_api_client import PlexAPI
from plex_api_client.models import operations


with PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.library.get_library_items(request={
        "tag": operations.Tag.NEWEST,
        "include_guids": operations.IncludeGuids.ENABLE,
        "type": operations.GetLibraryItemsQueryParamType.TV_SHOW,
        "section_key": 9518,
        "include_meta": operations.GetLibraryItemsQueryParamIncludeMeta.ENABLE,
    })

    assert res.object is not None

    # Handle response
    print(res.object)

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

## get_library_sections_all

Retrieves a list of all general media data for this library.


### Example Usage

```python
from plex_api_client import PlexAPI
from plex_api_client.models import operations


with PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.library.get_library_sections_all(request={
        "section_key": 9518,
        "type": operations.GetLibrarySectionsAllQueryParamType.TV_SHOW,
        "include_meta": operations.GetLibrarySectionsAllQueryParamIncludeMeta.ENABLE,
        "include_guids": operations.QueryParamIncludeGuids.ENABLE,
        "include_advanced": operations.IncludeAdvanced.ENABLE,
        "include_collections": operations.QueryParamIncludeCollections.ENABLE,
        "include_external_media": operations.QueryParamIncludeExternalMedia.ENABLE,
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetLibrarySectionsAllRequest](../../models/operations/getlibrarysectionsallrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.GetLibrarySectionsAllResponse](../../models/operations/getlibrarysectionsallresponse.md)**

### Errors

| Error Type                               | Status Code                              | Content Type                             |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| errors.GetLibrarySectionsAllBadRequest   | 400                                      | application/json                         |
| errors.GetLibrarySectionsAllUnauthorized | 401                                      | application/json                         |
| errors.SDKError                          | 4XX, 5XX                                 | \*/\*                                    |

## get_refresh_library_metadata

This endpoint Refreshes all the Metadata of the library.


### Example Usage

```python
from plex_api_client import PlexAPI
from plex_api_client.models import operations


with PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.library.get_refresh_library_metadata(section_key=9518, force=operations.Force.ZERO)

    assert res is not None

    # Handle response
    print(res)

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


with PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.library.get_search_library(section_key=9518, type_=operations.GetSearchLibraryQueryParamType.TV_SHOW)

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                                                                                                                    | Type                                                                                                                                                                                         | Required                                                                                                                                                                                     | Description                                                                                                                                                                                  | Example                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `section_key`                                                                                                                                                                                | *int*                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                           | The unique key of the Plex library. <br/>Note: This is unique in the context of the Plex server.<br/>                                                                                        | 9518                                                                                                                                                                                         |
| `type`                                                                                                                                                                                       | [operations.GetSearchLibraryQueryParamType](../../models/operations/getsearchlibraryqueryparamtype.md)                                                                                       | :heavy_check_mark:                                                                                                                                                                           | The type of media to retrieve or filter by.<br/>1 = movie<br/>2 = show<br/>3 = season<br/>4 = episode<br/>E.g. A movie library will not return anything with type 3 as there are no seasons for movie libraries<br/> | 2                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                          |                                                                                                                                                                                              |

### Response

**[operations.GetSearchLibraryResponse](../../models/operations/getsearchlibraryresponse.md)**

### Errors

| Error Type                          | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| errors.GetSearchLibraryBadRequest   | 400                                 | application/json                    |
| errors.GetSearchLibraryUnauthorized | 401                                 | application/json                    |
| errors.SDKError                     | 4XX, 5XX                            | \*/\*                               |

## get_genres_library

Retrieves a list of all the genres that are found for the media in this library.


### Example Usage

```python
from plex_api_client import PlexAPI
from plex_api_client.models import operations


with PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.library.get_genres_library(section_key=9518, type_=operations.GetGenresLibraryQueryParamType.TV_SHOW)

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                                                                                                                    | Type                                                                                                                                                                                         | Required                                                                                                                                                                                     | Description                                                                                                                                                                                  | Example                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `section_key`                                                                                                                                                                                | *int*                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                           | The unique key of the Plex library. <br/>Note: This is unique in the context of the Plex server.<br/>                                                                                        | 9518                                                                                                                                                                                         |
| `type`                                                                                                                                                                                       | [operations.GetGenresLibraryQueryParamType](../../models/operations/getgenreslibraryqueryparamtype.md)                                                                                       | :heavy_check_mark:                                                                                                                                                                           | The type of media to retrieve or filter by.<br/>1 = movie<br/>2 = show<br/>3 = season<br/>4 = episode<br/>E.g. A movie library will not return anything with type 3 as there are no seasons for movie libraries<br/> | 2                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                          |                                                                                                                                                                                              |

### Response

**[operations.GetGenresLibraryResponse](../../models/operations/getgenreslibraryresponse.md)**

### Errors

| Error Type                          | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| errors.GetGenresLibraryBadRequest   | 400                                 | application/json                    |
| errors.GetGenresLibraryUnauthorized | 401                                 | application/json                    |
| errors.SDKError                     | 4XX, 5XX                            | \*/\*                               |

## get_countries_library

Retrieves a list of all the countries that are found for the media in this library.


### Example Usage

```python
from plex_api_client import PlexAPI
from plex_api_client.models import operations


with PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.library.get_countries_library(section_key=9518, type_=operations.GetCountriesLibraryQueryParamType.TV_SHOW)

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                                                                                                                    | Type                                                                                                                                                                                         | Required                                                                                                                                                                                     | Description                                                                                                                                                                                  | Example                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `section_key`                                                                                                                                                                                | *int*                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                           | The unique key of the Plex library. <br/>Note: This is unique in the context of the Plex server.<br/>                                                                                        | 9518                                                                                                                                                                                         |
| `type`                                                                                                                                                                                       | [operations.GetCountriesLibraryQueryParamType](../../models/operations/getcountrieslibraryqueryparamtype.md)                                                                                 | :heavy_check_mark:                                                                                                                                                                           | The type of media to retrieve or filter by.<br/>1 = movie<br/>2 = show<br/>3 = season<br/>4 = episode<br/>E.g. A movie library will not return anything with type 3 as there are no seasons for movie libraries<br/> | 2                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                          |                                                                                                                                                                                              |

### Response

**[operations.GetCountriesLibraryResponse](../../models/operations/getcountrieslibraryresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.GetCountriesLibraryBadRequest   | 400                                    | application/json                       |
| errors.GetCountriesLibraryUnauthorized | 401                                    | application/json                       |
| errors.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

## get_actors_library

Retrieves a list of all the actors that are found for the media in this library.


### Example Usage

```python
from plex_api_client import PlexAPI
from plex_api_client.models import operations


with PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.library.get_actors_library(section_key=9518, type_=operations.GetActorsLibraryQueryParamType.TV_SHOW)

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                                                                                                                    | Type                                                                                                                                                                                         | Required                                                                                                                                                                                     | Description                                                                                                                                                                                  | Example                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `section_key`                                                                                                                                                                                | *int*                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                           | The unique key of the Plex library. <br/>Note: This is unique in the context of the Plex server.<br/>                                                                                        | 9518                                                                                                                                                                                         |
| `type`                                                                                                                                                                                       | [operations.GetActorsLibraryQueryParamType](../../models/operations/getactorslibraryqueryparamtype.md)                                                                                       | :heavy_check_mark:                                                                                                                                                                           | The type of media to retrieve or filter by.<br/>1 = movie<br/>2 = show<br/>3 = season<br/>4 = episode<br/>E.g. A movie library will not return anything with type 3 as there are no seasons for movie libraries<br/> | 2                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                          |                                                                                                                                                                                              |

### Response

**[operations.GetActorsLibraryResponse](../../models/operations/getactorslibraryresponse.md)**

### Errors

| Error Type                          | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| errors.GetActorsLibraryBadRequest   | 400                                 | application/json                    |
| errors.GetActorsLibraryUnauthorized | 401                                 | application/json                    |
| errors.SDKError                     | 4XX, 5XX                            | \*/\*                               |

## get_search_all_libraries

Search the provided query across all library sections, or a single section, and return matches as hubs, split up by type.


### Example Usage

```python
from plex_api_client import PlexAPI
from plex_api_client.models import operations


with PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.library.get_search_all_libraries(request={
        "query": "<value>",
        "client_id": "3381b62b-9ab7-4e37-827b-203e9809eb58",
        "search_types": [
            operations.SearchTypes.PEOPLE,
        ],
        "include_collections": operations.GetSearchAllLibrariesQueryParamIncludeCollections.ENABLE,
        "include_external_media": operations.GetSearchAllLibrariesQueryParamIncludeExternalMedia.ENABLE,
    })

    assert res.object is not None

    # Handle response
    print(res.object)

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

## get_media_meta_data

This endpoint will return all the (meta)data of one or more library items specified by the ratingKey.
Multiple rating keys can be provided as a comma-separated list (e.g., "21119,21617").


### Example Usage

```python
from plex_api_client import PlexAPI


with PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.library.get_media_meta_data(request={
        "rating_key": "21119,21617",
        "include_concerts": True,
        "include_extras": True,
        "include_on_deck": True,
        "include_popular_leaves": True,
        "include_preferences": True,
        "include_reviews": True,
        "include_chapters": True,
        "include_stations": True,
        "include_external_media": True,
        "async_augment_metadata": True,
        "async_check_files": True,
        "async_refresh_analysis": True,
        "async_refresh_local_media_agent": True,
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetMediaMetaDataRequest](../../models/operations/getmediametadatarequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetMediaMetaDataResponse](../../models/operations/getmediametadataresponse.md)**

### Errors

| Error Type                          | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| errors.GetMediaMetaDataBadRequest   | 400                                 | application/json                    |
| errors.GetMediaMetaDataUnauthorized | 401                                 | application/json                    |
| errors.SDKError                     | 4XX, 5XX                            | \*/\*                               |

## get_media_arts

Returns the background artwork for a library item.

### Example Usage

```python
from plex_api_client import PlexAPI


with PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.library.get_media_arts(rating_key=16099)

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `rating_key`                                                        | *int*                                                               | :heavy_check_mark:                                                  | the id of the library item to return the artwork of.                | 16099                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.GetMediaArtsResponse](../../models/operations/getmediaartsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## post_media_arts

Uploads an image to use as the background artwork for a library item, either from a local file or a remote URL

### Example Usage

```python
from plex_api_client import PlexAPI


with PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.library.post_media_arts(rating_key=2268, url="https://api.mediux.pro/assets/fcfdc487-dd07-4993-a0c1-0a3015362e5b")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `rating_key`                                                        | *int*                                                               | :heavy_check_mark:                                                  | the id of the library item to return the posters of.                | 2268                                                                |
| `url`                                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The URL of the image, if uploading a remote image                   | https://api.mediux.pro/assets/fcfdc487-dd07-4993-a0c1-0a3015362e5b  |
| `request_body`                                                      | *Optional[Union[bytes, IO[bytes], io.BufferedReader]]*              | :heavy_minus_sign:                                                  | The contents of the image, if uploading a local file                |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.PostMediaArtsResponse](../../models/operations/postmediaartsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_media_posters

Returns the available posters for a library item.

### Example Usage

```python
from plex_api_client import PlexAPI


with PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.library.get_media_posters(rating_key=16099)

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `rating_key`                                                        | *int*                                                               | :heavy_check_mark:                                                  | the id of the library item to return the posters of.                | 16099                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.GetMediaPostersResponse](../../models/operations/getmediapostersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## post_media_poster

Uploads a poster to a library item, either from a local file or a remote URL

### Example Usage

```python
from plex_api_client import PlexAPI


with PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.library.post_media_poster(rating_key=2268, url="https://api.mediux.pro/assets/fcfdc487-dd07-4993-a0c1-0a3015362e5b")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `rating_key`                                                        | *int*                                                               | :heavy_check_mark:                                                  | the id of the library item to return the posters of.                | 2268                                                                |
| `url`                                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The URL of the image, if uploading a remote image                   | https://api.mediux.pro/assets/fcfdc487-dd07-4993-a0c1-0a3015362e5b  |
| `request_body`                                                      | *Optional[Union[bytes, IO[bytes], io.BufferedReader]]*              | :heavy_minus_sign:                                                  | The contents of the image, if uploading a local file                |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.PostMediaPosterResponse](../../models/operations/postmediaposterresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_metadata_children

This endpoint will return the children of of a library item specified with the ratingKey.


### Example Usage

```python
from plex_api_client import PlexAPI


with PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.library.get_metadata_children(rating_key=2403.67, include_elements="Stream")

    assert res.object is not None

    # Handle response
    print(res.object)

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


with PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.library.get_top_watched_content(type_=operations.GetTopWatchedContentQueryParamType.TV_SHOW, include_guids=operations.GetTopWatchedContentQueryParamIncludeGuids.ENABLE)

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                                                                                                                    | Type                                                                                                                                                                                         | Required                                                                                                                                                                                     | Description                                                                                                                                                                                  | Example                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`                                                                                                                                                                                       | [operations.GetTopWatchedContentQueryParamType](../../models/operations/gettopwatchedcontentqueryparamtype.md)                                                                               | :heavy_check_mark:                                                                                                                                                                           | The type of media to retrieve or filter by.<br/>1 = movie<br/>2 = show<br/>3 = season<br/>4 = episode<br/>E.g. A movie library will not return anything with type 3 as there are no seasons for movie libraries<br/> | 2                                                                                                                                                                                            |
| `include_guids`                                                                                                                                                                              | [Optional[operations.GetTopWatchedContentQueryParamIncludeGuids]](../../models/operations/gettopwatchedcontentqueryparamincludeguids.md)                                                     | :heavy_minus_sign:                                                                                                                                                                           | Adds the Guid object to the response<br/>                                                                                                                                                    | 1                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                          |                                                                                                                                                                                              |

### Response

**[operations.GetTopWatchedContentResponse](../../models/operations/gettopwatchedcontentresponse.md)**

### Errors

| Error Type                              | Status Code                             | Content Type                            |
| --------------------------------------- | --------------------------------------- | --------------------------------------- |
| errors.GetTopWatchedContentBadRequest   | 400                                     | application/json                        |
| errors.GetTopWatchedContentUnauthorized | 401                                     | application/json                        |
| errors.SDKError                         | 4XX, 5XX                                | \*/\*                                   |