# Butler
(*butler*)

## Overview

Butler is the task manager of the Plex Media Server Ecosystem.


### Available Operations

* [get_butler_tasks](#get_butler_tasks) - Get Butler tasks
* [start_all_tasks](#start_all_tasks) - Start all Butler tasks
* [stop_all_tasks](#stop_all_tasks) - Stop all Butler tasks
* [start_task](#start_task) - Start a single Butler task
* [stop_task](#stop_task) - Stop a single Butler task

## get_butler_tasks

Returns a list of butler tasks

### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    client_id="gcgzw5rz2xovp84b4vha3a40",
    client_name="Plex Web",
    client_version="4.133.0",
    client_platform="Chrome",
    device_name="Linux",
)

res = s.butler.get_butler_tasks()

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetButlerTasksResponse](../../models/operations/getbutlertasksresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.GetButlerTasksBadRequest   | 400                               | application/json                  |
| errors.GetButlerTasksUnauthorized | 401                               | application/json                  |
| errors.SDKError                   | 4XX, 5XX                          | \*/\*                             |

## start_all_tasks

This endpoint will attempt to start all Butler tasks that are enabled in the settings. Butler tasks normally run automatically during a time window configured on the server's Settings page but can be manually started using this endpoint. Tasks will run with the following criteria:
1. Any tasks not scheduled to run on the current day will be skipped.
2. If a task is configured to run at a random time during the configured window and we are outside that window, the task will start immediately.
3. If a task is configured to run at a random time during the configured window and we are within that window, the task will be scheduled at a random time within the window.
4. If we are outside the configured window, the task will start immediately.


### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    client_id="gcgzw5rz2xovp84b4vha3a40",
    client_name="Plex Web",
    client_version="4.133.0",
    client_platform="Chrome",
    device_name="Linux",
)

res = s.butler.start_all_tasks()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.StartAllTasksResponse](../../models/operations/startalltasksresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.StartAllTasksBadRequest   | 400                              | application/json                 |
| errors.StartAllTasksUnauthorized | 401                              | application/json                 |
| errors.SDKError                  | 4XX, 5XX                         | \*/\*                            |

## stop_all_tasks

This endpoint will stop all currently running tasks and remove any scheduled tasks from the queue.


### Example Usage

```python
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    client_id="gcgzw5rz2xovp84b4vha3a40",
    client_name="Plex Web",
    client_version="4.133.0",
    client_platform="Chrome",
    device_name="Linux",
)

res = s.butler.stop_all_tasks()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.StopAllTasksResponse](../../models/operations/stopalltasksresponse.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.StopAllTasksBadRequest   | 400                             | application/json                |
| errors.StopAllTasksUnauthorized | 401                             | application/json                |
| errors.SDKError                 | 4XX, 5XX                        | \*/\*                           |

## start_task

This endpoint will attempt to start a single Butler task that is enabled in the settings. Butler tasks normally run automatically during a time window configured on the server's Settings page but can be manually started using this endpoint. Tasks will run with the following criteria:
1. Any tasks not scheduled to run on the current day will be skipped.
2. If a task is configured to run at a random time during the configured window and we are outside that window, the task will start immediately.
3. If a task is configured to run at a random time during the configured window and we are within that window, the task will be scheduled at a random time within the window.
4. If we are outside the configured window, the task will start immediately.


### Example Usage

```python
from plex_api_client import PlexAPI
from plex_api_client.models import operations

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    client_id="gcgzw5rz2xovp84b4vha3a40",
    client_name="Plex Web",
    client_version="4.133.0",
    client_platform="Chrome",
    device_name="Linux",
)

res = s.butler.start_task(task_name=operations.TaskName.CLEAN_OLD_BUNDLES)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `task_name`                                                         | [operations.TaskName](../../models/operations/taskname.md)          | :heavy_check_mark:                                                  | the name of the task to be started.                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.StartTaskResponse](../../models/operations/starttaskresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.StartTaskBadRequest   | 400                          | application/json             |
| errors.StartTaskUnauthorized | 401                          | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## stop_task

This endpoint will stop a currently running task by name, or remove it from the list of scheduled tasks if it exists. See the section above for a list of task names for this endpoint.


### Example Usage

```python
from plex_api_client import PlexAPI
from plex_api_client.models import operations

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    client_id="gcgzw5rz2xovp84b4vha3a40",
    client_name="Plex Web",
    client_version="4.133.0",
    client_platform="Chrome",
    device_name="Linux",
)

res = s.butler.stop_task(task_name=operations.PathParamTaskName.BACKUP_DATABASE)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `task_name`                                                                  | [operations.PathParamTaskName](../../models/operations/pathparamtaskname.md) | :heavy_check_mark:                                                           | The name of the task to be started.                                          |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.StopTaskResponse](../../models/operations/stoptaskresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.StopTaskBadRequest   | 400                         | application/json            |
| errors.StopTaskUnauthorized | 401                         | application/json            |
| errors.SDKError             | 4XX, 5XX                    | \*/\*                       |