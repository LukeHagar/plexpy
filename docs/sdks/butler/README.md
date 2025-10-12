# Butler
(*butler*)

## Overview

The butler is responsible for running periodic tasks.  Some tasks run daily, others every few days, and some weekly.  These includes database maintenance, metadata updating, thumbnail generation, media analysis, and other tasks.

### Available Operations

* [stop_tasks](#stop_tasks) - Stop all Butler tasks
* [get_tasks](#get_tasks) - Get all Butler tasks
* [start_tasks](#start_tasks) - Start all Butler tasks
* [stop_task](#stop_task) - Stop a single Butler task
* [start_task](#start_task) - Start a single Butler task

## stop_tasks

This endpoint will stop all currently running tasks and remove any scheduled tasks from the queue.

### Example Usage

<!-- UsageSnippet language="python" operationID="stopTasks" method="delete" path="/butler" -->
```python
from plex_api_client import PlexAPI


with PlexAPI(
    token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.butler.stop_tasks()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.StopTasksResponse](../../models/operations/stoptasksresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_tasks

Get the list of butler tasks and their scheduling


### Example Usage

<!-- UsageSnippet language="python" operationID="getTasks" method="get" path="/butler" -->
```python
from plex_api_client import PlexAPI


with PlexAPI(
    token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.butler.get_tasks()

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetTasksResponse](../../models/operations/gettasksresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## start_tasks

This endpoint will attempt to start all Butler tasks that are enabled in the settings. Butler tasks normally run automatically during a time window configured on the server's Settings page but can be manually started using this endpoint. Tasks will run with the following criteria:

  1. Any tasks not scheduled to run on the current day will be skipped.
  2. If a task is configured to run at a random time during the configured window and we are outside that window, the task will start immediately.
  3. If a task is configured to run at a random time during the configured window and we are within that window, the task will be scheduled at a random time within the window.
  4. If we are outside the configured window, the task will start immediately.


### Example Usage

<!-- UsageSnippet language="python" operationID="startTasks" method="post" path="/butler" -->
```python
from plex_api_client import PlexAPI


with PlexAPI(
    token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.butler.start_tasks()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.StartTasksResponse](../../models/operations/starttasksresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## stop_task

This endpoint will stop a currently running task by name, or remove it from the list of scheduled tasks if it exists


### Example Usage

<!-- UsageSnippet language="python" operationID="stopTask" method="delete" path="/butler/{task}" -->
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

    res = plex_api.butler.stop_task(request={
        "task": operations.Task.CLEAN_OLD_BUNDLES,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.StopTaskRequest](../../models/operations/stoptaskrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |
| `retries`                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)         | :heavy_minus_sign:                                                       | Configuration to override the default retry behavior of the client.      |

### Response

**[operations.StopTaskResponse](../../models/operations/stoptaskresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## start_task

This endpoint will attempt to start a specific Butler task by name.


### Example Usage

<!-- UsageSnippet language="python" operationID="startTask" method="post" path="/butler/{task}" -->
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

    res = plex_api.butler.start_task(request={
        "task": operations.PathParamTask.REFRESH_LOCAL_MEDIA,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.StartTaskRequest](../../models/operations/starttaskrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[operations.StartTaskResponse](../../models/operations/starttaskresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |