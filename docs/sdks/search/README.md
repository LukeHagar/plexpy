# Search
(*search*)

## Overview

API Calls that perform search operations with Plex Media Server


### Available Operations

* [perform_search](#perform_search) - Perform a search
* [perform_voice_search](#perform_voice_search) - Perform a voice search
* [get_search_results](#get_search_results) - Get Search Results

## perform_search

This endpoint performs a search across all library sections, or a single section, and returns matches as hubs, split up by type. It performs spell checking, looks for partial matches, and orders the hubs based on quality of results. In addition, based on matches, it will return other related matches (e.g. for a genre match, it may return movies in that genre, or for an actor match, movies with that actor).

In the response's items, the following extra attributes are returned to further describe or disambiguate the result:

- `reason`: The reason for the result, if not because of a direct search term match; can be either:
  - `section`: There are multiple identical results from different sections.
  - `originalTitle`: There was a search term match from the original title field (sometimes those can be very different or in a foreign language).
  - `<hub identifier>`: If the reason for the result is due to a result in another hub, the source hub identifier is returned. For example, if the search is for "dylan" then Bob Dylan may be returned as an artist result, an a few of his albums returned as album results with a reason code of `artist` (the identifier of that particular hub). Or if the search is for "arnold", there might be movie results returned with a reason of `actor`
- `reasonTitle`: The string associated with the reason code. For a section reason, it'll be the section name; For a hub identifier, it'll be a string associated with the match (e.g. `Arnold Schwarzenegger` for movies which were returned because the search was for "arnold").
- `reasonID`: The ID of the item associated with the reason for the result. This might be a section ID, a tag ID, an artist ID, or a show ID.

This request is intended to be very fast, and called as the user types.


### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='<value>',
)


res = s.search.perform_search(query='dylan', section_id=1516.53, limit=5)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           | Example                                                                               |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `query`                                                                               | *str*                                                                                 | :heavy_check_mark:                                                                    | The query term                                                                        | arnold                                                                                |
| `section_id`                                                                          | *Optional[float]*                                                                     | :heavy_minus_sign:                                                                    | This gives context to the search, and can result in re-ordering of search result hubs |                                                                                       |
| `limit`                                                                               | *Optional[float]*                                                                     | :heavy_minus_sign:                                                                    | The number of items to return per hub                                                 | 5                                                                                     |


### Response

**[operations.PerformSearchResponse](../../models/operations/performsearchresponse.md)**
### Errors

| Error Object                     | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.PerformSearchResponseBody | 401                              | application/json                 |
| errors.SDKError                  | 4xx-5xx                          | */*                              |

## perform_voice_search

This endpoint performs a search specifically tailored towards voice or other imprecise input which may work badly with the substring and spell-checking heuristics used by the `/hubs/search` endpoint. 
It uses a [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) heuristic to search titles, and as such is much slower than the other search endpoint. 
Whenever possible, clients should limit the search to the appropriate type. 
Results, as well as their containing per-type hubs, contain a `distance` attribute which can be used to judge result quality.


### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='<value>',
)


res = s.search.perform_voice_search(query='dead+poop', section_id=4094.8, limit=5)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           | Example                                                                               |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `query`                                                                               | *str*                                                                                 | :heavy_check_mark:                                                                    | The query term                                                                        | dead+poop                                                                             |
| `section_id`                                                                          | *Optional[float]*                                                                     | :heavy_minus_sign:                                                                    | This gives context to the search, and can result in re-ordering of search result hubs |                                                                                       |
| `limit`                                                                               | *Optional[float]*                                                                     | :heavy_minus_sign:                                                                    | The number of items to return per hub                                                 | 5                                                                                     |


### Response

**[operations.PerformVoiceSearchResponse](../../models/operations/performvoicesearchresponse.md)**
### Errors

| Error Object                          | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| errors.PerformVoiceSearchResponseBody | 401                                   | application/json                      |
| errors.SDKError                       | 4xx-5xx                               | */*                                   |

## get_search_results

This will search the database for the string provided.

### Example Usage

```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='<value>',
)


res = s.search.get_search_results(query='110')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                      | Type                           | Required                       | Description                    | Example                        |
| ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ |
| `query`                        | *str*                          | :heavy_check_mark:             | The search query string to use | 110                            |


### Response

**[operations.GetSearchResultsResponse](../../models/operations/getsearchresultsresponse.md)**
### Errors

| Error Object                        | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| errors.GetSearchResultsResponseBody | 401                                 | application/json                    |
| errors.SDKError                     | 4xx-5xx                             | */*                                 |
