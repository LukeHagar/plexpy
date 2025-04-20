# Log
(*log*)

## Overview

Submit logs to the Log Handler for Plex Media Server


### Available Operations

* [log_line](#log_line) - Logging a single line message.
* [log_multi_line](#log_multi_line) - Logging a multi-line message
* [enable_paper_trail](#enable_paper_trail) - Enabling Papertrail

## log_line

This endpoint will write a single-line log message, including a level and source to the main Plex Media Server log.


### Example Usage

```python
from plex_api_client import PlexAPI
from plex_api_client.models import operations


with PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.log.log_line(level=operations.Level.THREE, message="Test log message", source="Postman")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         | Example                                                                                             |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `level`                                                                                             | [operations.Level](../../models/operations/level.md)                                                | :heavy_check_mark:                                                                                  | An integer log level to write to the PMS log with.<br/>0: Error<br/>1: Warning<br/>2: Info<br/>3: Debug<br/>4: Verbose<br/> |                                                                                                     |
| `message`                                                                                           | *str*                                                                                               | :heavy_check_mark:                                                                                  | The text of the message to write to the log.                                                        | Test log message                                                                                    |
| `source`                                                                                            | *str*                                                                                               | :heavy_check_mark:                                                                                  | a string indicating the source of the message.                                                      | Postman                                                                                             |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |                                                                                                     |

### Response

**[operations.LogLineResponse](../../models/operations/loglineresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.LogLineBadRequest   | 400                        | application/json           |
| errors.LogLineUnauthorized | 401                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |

## log_multi_line

This endpoint allows for the batch addition of log entries to the main Plex Media Server log.
It accepts a text/plain request body, where each line represents a distinct log entry.
Each log entry consists of URL-encoded key-value pairs, specifying log attributes such as 'level', 'message', and 'source'.

Log entries are separated by a newline character (`\n`).
Each entry's parameters should be URL-encoded to ensure accurate parsing and handling of special characters.
This method is efficient for logging multiple entries in a single API call, reducing the overhead of multiple individual requests.

The 'level' parameter specifies the log entry's severity or importance, with the following integer values:
- `0`: Error - Critical issues that require immediate attention.
- `1`: Warning - Important events that are not critical but may indicate potential issues.
- `2`: Info - General informational messages about system operation.
- `3`: Debug - Detailed information useful for debugging purposes.
- `4`: Verbose - Highly detailed diagnostic information for in-depth analysis.

The 'message' parameter contains the log text, and 'source' identifies the log message's origin (e.g., an application name or module).

Example of a single log entry format:
`level=4&message=Sample%20log%20entry&source=applicationName`

Ensure each parameter is properly URL-encoded to avoid interpretation issues.


### Example Usage

```python
from plex_api_client import PlexAPI


with PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.log.log_multi_line(request=("level=4&message=Test%20message%201&source=postman\n"
    "level=3&message=Test%20message%202&source=postman\n"
    "level=1&message=Test%20message%203&source=postman"))

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [str](../../models/.md)                                             | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.LogMultiLineResponse](../../models/operations/logmultilineresponse.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.LogMultiLineBadRequest   | 400                             | application/json                |
| errors.LogMultiLineUnauthorized | 401                             | application/json                |
| errors.SDKError                 | 4XX, 5XX                        | \*/\*                           |

## enable_paper_trail

This endpoint will enable all Plex Media Serverlogs to be sent to the Papertrail networked logging site for a period of time.


### Example Usage

```python
from plex_api_client import PlexAPI


with PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.log.enable_paper_trail()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.EnablePaperTrailResponse](../../models/operations/enablepapertrailresponse.md)**

### Errors

| Error Type                          | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| errors.EnablePaperTrailBadRequest   | 400                                 | application/json                    |
| errors.EnablePaperTrailUnauthorized | 401                                 | application/json                    |
| errors.SDKError                     | 4XX, 5XX                            | \*/\*                               |