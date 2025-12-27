# DVRs

## Overview

The DVR provides means to watch and record live TV.  This section of endpoints describes how to setup the DVR itself


### Available Operations

* [list_dv_rs](#list_dv_rs) - Get DVRs
* [create_dvr](#create_dvr) - Create a DVR
* [delete_dvr](#delete_dvr) - Delete a single DVR
* [get_dvr](#get_dvr) - Get a single DVR
* [delete_lineup](#delete_lineup) - Delete a DVR Lineup
* [add_lineup](#add_lineup) - Add a DVR Lineup
* [set_dvr_preferences](#set_dvr_preferences) - Set DVR preferences
* [stop_dvr_reload](#stop_dvr_reload) - Tell a DVR to stop reloading program guide
* [reload_guide](#reload_guide) - Tell a DVR to reload program guide
* [tune_channel](#tune_channel) - Tune a channel on a DVR
* [remove_device_from_dvr](#remove_device_from_dvr) - Remove a device from an existing DVR
* [add_device_to_dvr](#add_device_to_dvr) - Add a device to an existing DVR

## list_dv_rs

Get the list of all available DVRs

### Example Usage

<!-- UsageSnippet language="python" operationID="listDVRs" method="get" path="/livetv/dvrs" -->
```python
from plex_api_client import PlexAPI


with PlexAPI(
    token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.dv_rs.list_dv_rs()

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.ListDVRsResponse](../../models/operations/listdvrsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_dvr

Creation of a DVR, after creation of a devcie and a lineup is selected

### Example Usage

<!-- UsageSnippet language="python" operationID="createDVR" method="post" path="/livetv/dvrs" -->
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

    res = plex_api.dv_rs.create_dvr(request={
        "lineup": "lineup://tv.plex.providers.epg.onconnect/USA-HI51418-DEFAULT",
        "device_query_parameter": [
            "d",
            "e",
            "v",
            "i",
            "c",
            "e",
            "[",
            "]",
            "=",
            "d",
            "e",
            "v",
            "i",
            "c",
            "e",
            ":",
            "/",
            "/",
            "t",
            "v",
            ".",
            "p",
            "l",
            "e",
            "x",
            ".",
            "g",
            "r",
            "a",
            "b",
            "b",
            "e",
            "r",
            "s",
            ".",
            "h",
            "d",
            "h",
            "o",
            "m",
            "e",
            "r",
            "u",
            "n",
            "/",
            "1",
            "0",
            "5",
            "3",
            "C",
            "0",
            "C",
            "A",
        ],
        "language": "eng",
    })

    assert res.dvr_request_handler_slash_get_responses_200 is not None

    # Handle response
    print(res.dvr_request_handler_slash_get_responses_200)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.CreateDVRRequest](../../models/operations/createdvrrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[operations.CreateDVRResponse](../../models/operations/createdvrresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_dvr

Delete a single DVR by its id (key)

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteDVR" method="delete" path="/livetv/dvrs/{dvrId}" -->
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

    res = plex_api.dv_rs.delete_dvr(request={
        "dvr_id": 855088,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.DeleteDVRRequest](../../models/operations/deletedvrrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[operations.DeleteDVRResponse](../../models/operations/deletedvrresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dvr

Get a single DVR by its id (key)

### Example Usage

<!-- UsageSnippet language="python" operationID="getDVR" method="get" path="/livetv/dvrs/{dvrId}" -->
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

    res = plex_api.dv_rs.get_dvr(request={
        "dvr_id": 973518,
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [operations.GetDVRRequest](../../models/operations/getdvrrequest.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[operations.GetDVRResponse](../../models/operations/getdvrresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_lineup

Deletes a DVR device's lineup.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteLineup" method="delete" path="/livetv/dvrs/{dvrId}/lineups" -->
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

    res = plex_api.dv_rs.delete_lineup(request={
        "dvr_id": 454470,
        "lineup": "<value>",
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.DeleteLineupRequest](../../models/operations/deletelineuprequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.DeleteLineupResponse](../../models/operations/deletelineupresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## add_lineup

Add a lineup to a DVR device's set of lineups.

### Example Usage

<!-- UsageSnippet language="python" operationID="addLineup" method="put" path="/livetv/dvrs/{dvrId}/lineups" -->
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

    res = plex_api.dv_rs.add_lineup(request={
        "dvr_id": 945235,
        "lineup": "<value>",
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.AddLineupRequest](../../models/operations/addlineuprequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[operations.AddLineupResponse](../../models/operations/addlineupresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## set_dvr_preferences

Set DVR preferences by name avd value

### Example Usage

<!-- UsageSnippet language="python" operationID="setDVRPreferences" method="put" path="/livetv/dvrs/{dvrId}/prefs" -->
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

    res = plex_api.dv_rs.set_dvr_preferences(request={
        "dvr_id": 116357,
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.SetDVRPreferencesRequest](../../models/operations/setdvrpreferencesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.SetDVRPreferencesResponse](../../models/operations/setdvrpreferencesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## stop_dvr_reload

Tell a DVR to stop reloading program guide

### Example Usage

<!-- UsageSnippet language="python" operationID="stopDVRReload" method="delete" path="/livetv/dvrs/{dvrId}/reloadGuide" -->
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

    res = plex_api.dv_rs.stop_dvr_reload(request={
        "dvr_id": 348053,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.StopDVRReloadRequest](../../models/operations/stopdvrreloadrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.StopDVRReloadResponse](../../models/operations/stopdvrreloadresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## reload_guide

Tell a DVR to reload program guide

### Example Usage

<!-- UsageSnippet language="python" operationID="reloadGuide" method="post" path="/livetv/dvrs/{dvrId}/reloadGuide" -->
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

    res = plex_api.dv_rs.reload_guide(request={
        "dvr_id": 140753,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.ReloadGuideRequest](../../models/operations/reloadguiderequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.ReloadGuideResponse](../../models/operations/reloadguideresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## tune_channel

Tune a channel on a DVR to the provided channel

### Example Usage

<!-- UsageSnippet language="python" operationID="tuneChannel" method="post" path="/livetv/dvrs/{dvrId}/channels/{channel}/tune" -->
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

    res = plex_api.dv_rs.tune_channel(request={
        "dvr_id": 834281,
        "channel": "2.1",
    })

    assert res.media_container_with_metadata is not None

    # Handle response
    print(res.media_container_with_metadata)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.TuneChannelRequest](../../models/operations/tunechannelrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.TuneChannelResponse](../../models/operations/tunechannelresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_device_from_dvr

Remove a device from an existing DVR

### Example Usage

<!-- UsageSnippet language="python" operationID="removeDeviceFromDVR" method="delete" path="/livetv/dvrs/{dvrId}/devices/{deviceId}" -->
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

    res = plex_api.dv_rs.remove_device_from_dvr(request={
        "dvr_id": 945416,
        "device_id": 260761,
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.RemoveDeviceFromDVRRequest](../../models/operations/removedevicefromdvrrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.RemoveDeviceFromDVRResponse](../../models/operations/removedevicefromdvrresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## add_device_to_dvr

Add a device to an existing DVR

### Example Usage

<!-- UsageSnippet language="python" operationID="addDeviceToDVR" method="put" path="/livetv/dvrs/{dvrId}/devices/{deviceId}" -->
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

    res = plex_api.dv_rs.add_device_to_dvr(request={
        "dvr_id": 334755,
        "device_id": 852930,
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.AddDeviceToDVRRequest](../../models/operations/adddevicetodvrrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.AddDeviceToDVRResponse](../../models/operations/adddevicetodvrresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |