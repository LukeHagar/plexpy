# UltraBlur

## Overview

Service provided to compute UltraBlur colors and images.

### Available Operations

* [get_colors](#get_colors) - Get UltraBlur Colors
* [get_image](#get_image) - Get UltraBlur Image

## get_colors

Retrieves the four colors extracted from an image for clients to use to generate an ultrablur image.

### Example Usage

<!-- UsageSnippet language="python" operationID="getColors" method="get" path="/services/ultrablur/colors" -->
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

    res = plex_api.ultra_blur.get_colors(request={
        "url": "/library/metadata/217745/art/1718931408",
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetColorsRequest](../../models/operations/getcolorsrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[operations.GetColorsResponse](../../models/operations/getcolorsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_image

Retrieves a server-side generated UltraBlur image based on the provided color inputs. Clients should always call this via the photo transcoder endpoint.

### Example Usage

<!-- UsageSnippet language="python" operationID="getImage" method="get" path="/services/ultrablur/image" -->
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

    res = plex_api.ultra_blur.get_image(request={
        "top_left": "3f280a",
        "top_right": "6b4713",
        "bottom_right": "0f2a43",
        "bottom_left": "1c425d",
        "width": 1920,
        "height": 1080,
        "noise": components.BoolInt.TRUE,
    })

    assert res.response_stream is not None

    # Handle response
    print(res.response_stream)

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.GetImageRequest](../../models/operations/getimagerequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |
| `retries`                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)         | :heavy_minus_sign:                                                       | Configuration to override the default retry behavior of the client.      |

### Response

**[operations.GetImageResponse](../../models/operations/getimageresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |