# Provider

## Overview

Media providers are the starting points for the entire Plex Media Server media library API.  It defines the paths for the groups of endpoints.  The `/media/providers` should be the only hard-coded path in clients when accessing the media library.  Non-media library endpoints are outside the scope of the media provider.  See the description in See [the section in API Info](#section/API-Info/Media-Providers) for more information on how to use media providers.

### Available Operations

* [list_providers](#list_providers) - Get the list of available media providers
* [add_provider](#add_provider) - Add a media provider
* [refresh_providers](#refresh_providers) - Refresh media providers
* [delete_media_provider](#delete_media_provider) - Delete a media provider

## list_providers

Get the list of all available media providers for this PMS.  This will generally include the library provider and possibly EPG if DVR is set up.

### Example Usage

<!-- UsageSnippet language="python" operationID="listProviders" method="get" path="/media/providers" -->
```python
from plex_api_client import PlexAPI


with PlexAPI(
    token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.provider.list_providers()

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.ListProvidersResponse](../../models/operations/listprovidersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## add_provider

This endpoint registers a media provider with the server. Once registered, the media server acts as a reverse proxy to the provider, allowing both local and remote providers to work.

### Example Usage

<!-- UsageSnippet language="python" operationID="addProvider" method="post" path="/media/providers" -->
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

    res = plex_api.provider.add_provider(request={
        "url": "https://steep-obedience.name/",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.AddProviderRequest](../../models/operations/addproviderrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.AddProviderResponse](../../models/operations/addproviderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## refresh_providers

Refresh all known media providers. This is useful in case a provider has updated features.

### Example Usage

<!-- UsageSnippet language="python" operationID="refreshProviders" method="post" path="/media/providers/refresh" -->
```python
from plex_api_client import PlexAPI


with PlexAPI(
    token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.provider.refresh_providers()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.RefreshProvidersResponse](../../models/operations/refreshprovidersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_media_provider

Deletes a media provider with the given id

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteMediaProvider" method="delete" path="/media/providers/{provider}" -->
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

    res = plex_api.provider.delete_media_provider(request={
        "provider": "<value>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.DeleteMediaProviderRequest](../../models/operations/deletemediaproviderrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.DeleteMediaProviderResponse](../../models/operations/deletemediaproviderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |