# Transcoder
(*transcoder*)

## Overview

API Operations against the Transcoder

### Available Operations

* [transcode_image](#transcode_image) - Transcode an image
* [make_decision](#make_decision) - Make a decision on media playback
* [trigger_fallback](#trigger_fallback) - Manually trigger a transcoder fallback
* [transcode_subtitles](#transcode_subtitles) - Transcode subtitles
* [start_transcode_session](#start_transcode_session) - Start A Transcoding Session

## transcode_image

Transcode an image, possibly changing format or size

### Example Usage

<!-- UsageSnippet language="python" operationID="transcodeImage" method="get" path="/photo/:/transcode" -->
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

    res = plex_api.transcoder.transcode_image(request=operations.TranscodeImageRequest(
        url="/library/metadata/265/thumb/1715112705",
        background="#ff5522",
        upscale=components.BoolInt.TRUE,
        min_size=components.BoolInt.TRUE,
        rotate=components.BoolInt.TRUE,
        blend_color="#ff5522",
    ))

    assert res.two_hundred_image_jpeg_response_stream is not None

    # Handle response
    print(res.two_hundred_image_jpeg_response_stream)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.TranscodeImageRequest](../../models/operations/transcodeimagerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.TranscodeImageResponse](../../models/operations/transcodeimageresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## make_decision

Make a decision on media playback based on client profile, and requested settings such as bandwidth and resolution.

### Example Usage

<!-- UsageSnippet language="python" operationID="makeDecision" method="get" path="/{transcodeType}/:/transcode/universal/decision" -->
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

    res = plex_api.transcoder.make_decision(request=operations.MakeDecisionRequest(
        transcode_type=components.TranscodeType.MUSIC,
        advanced_subtitles=components.AdvancedSubtitles.BURN,
        audio_boost=50,
        audio_channel_count=5,
        auto_adjust_quality=components.BoolInt.TRUE,
        auto_adjust_subtitle=components.BoolInt.TRUE,
        direct_play=components.BoolInt.TRUE,
        direct_stream=components.BoolInt.TRUE,
        direct_stream_audio=components.BoolInt.TRUE,
        disable_resolution_rotation=components.BoolInt.TRUE,
        has_mde=components.BoolInt.TRUE,
        location=operations.Location.WAN,
        media_buffer_size=102400,
        media_index=0,
        music_bitrate=5000,
        offset=90.5,
        part_index=0,
        path="/library/metadata/151671",
        peak_bitrate=12000,
        photo_resolution="1080x1080",
        protocol=operations.Protocol.DASH,
        seconds_per_segment=5,
        subtitle_size=50,
        video_bitrate=12000,
        video_quality=50,
        video_resolution="1080x1080",
        x_plex_client_profile_extra="add-limitation(scope=videoCodec&scopeName=*&type=upperBound&name=video.frameRate&value=60&replace=true)+append-transcode-target-codec(type=videoProfile&context=streaming&videoCodec=h264%2Chevc&audioCodec=aac&protocol=dash)",
        x_plex_client_profile_name="generic",
    ))

    assert res.media_container_with_decision is not None

    # Handle response
    print(res.media_container_with_decision)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.MakeDecisionRequest](../../models/operations/makedecisionrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.MakeDecisionResponse](../../models/operations/makedecisionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## trigger_fallback

Manually trigger a transcoder fallback ex: HEVC to h.264 or hw to sw

### Example Usage

<!-- UsageSnippet language="python" operationID="triggerFallback" method="post" path="/{transcodeType}/:/transcode/universal/fallback" -->
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

    res = plex_api.transcoder.trigger_fallback(request={
        "transcode_type": components.TranscodeType.AUDIO,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.TriggerFallbackRequest](../../models/operations/triggerfallbackrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.TriggerFallbackResponse](../../models/operations/triggerfallbackresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## transcode_subtitles

Only transcode subtitle streams.

### Example Usage

<!-- UsageSnippet language="python" operationID="transcodeSubtitles" method="get" path="/{transcodeType}/:/transcode/universal/subtitles" -->
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

    res = plex_api.transcoder.transcode_subtitles(request=operations.TranscodeSubtitlesRequest(
        transcode_type=components.TranscodeType.AUDIO,
        advanced_subtitles=components.AdvancedSubtitles.BURN,
        audio_boost=50,
        audio_channel_count=5,
        auto_adjust_quality=components.BoolInt.TRUE,
        auto_adjust_subtitle=components.BoolInt.TRUE,
        direct_play=components.BoolInt.TRUE,
        direct_stream=components.BoolInt.TRUE,
        direct_stream_audio=components.BoolInt.TRUE,
        disable_resolution_rotation=components.BoolInt.TRUE,
        has_mde=components.BoolInt.TRUE,
        location=operations.QueryParamLocation.WAN,
        media_buffer_size=102400,
        media_index=0,
        music_bitrate=5000,
        offset=90.5,
        part_index=0,
        path="/library/metadata/151671",
        peak_bitrate=12000,
        photo_resolution="1080x1080",
        protocol=operations.QueryParamProtocol.DASH,
        seconds_per_segment=5,
        subtitle_size=50,
        video_bitrate=12000,
        video_quality=50,
        video_resolution="1080x1080",
        x_plex_client_profile_extra="add-limitation(scope=videoCodec&scopeName=*&type=upperBound&name=video.frameRate&value=60&replace=true)+append-transcode-target-codec(type=videoProfile&context=streaming&videoCodec=h264%2Chevc&audioCodec=aac&protocol=dash)",
        x_plex_client_profile_name="generic",
    ))

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.TranscodeSubtitlesRequest](../../models/operations/transcodesubtitlesrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.TranscodeSubtitlesResponse](../../models/operations/transcodesubtitlesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## start_transcode_session

Starts the transcoder and returns the corresponding streaming resource document.

### Example Usage

<!-- UsageSnippet language="python" operationID="startTranscodeSession" method="get" path="/{transcodeType}/:/transcode/universal/start.{extension}" -->
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

    res = plex_api.transcoder.start_transcode_session(request=operations.StartTranscodeSessionRequest(
        transcode_type=components.TranscodeType.MUSIC,
        extension=operations.Extension.MPD,
        advanced_subtitles=components.AdvancedSubtitles.BURN,
        audio_boost=50,
        audio_channel_count=5,
        auto_adjust_quality=components.BoolInt.TRUE,
        auto_adjust_subtitle=components.BoolInt.TRUE,
        direct_play=components.BoolInt.TRUE,
        direct_stream=components.BoolInt.TRUE,
        direct_stream_audio=components.BoolInt.TRUE,
        disable_resolution_rotation=components.BoolInt.TRUE,
        has_mde=components.BoolInt.TRUE,
        location=operations.StartTranscodeSessionQueryParamLocation.WAN,
        media_buffer_size=102400,
        media_index=0,
        music_bitrate=5000,
        offset=90.5,
        part_index=0,
        path="/library/metadata/151671",
        peak_bitrate=12000,
        photo_resolution="1080x1080",
        protocol=operations.StartTranscodeSessionQueryParamProtocol.DASH,
        seconds_per_segment=5,
        subtitle_size=50,
        video_bitrate=12000,
        video_quality=50,
        video_resolution="1080x1080",
        x_plex_client_profile_extra="add-limitation(scope=videoCodec&scopeName=*&type=upperBound&name=video.frameRate&value=60&replace=true)+append-transcode-target-codec(type=videoProfile&context=streaming&videoCodec=h264%2Chevc&audioCodec=aac&protocol=dash)",
        x_plex_client_profile_name="generic",
    ))

    assert res.response_stream is not None

    # Handle response
    print(res.response_stream)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.StartTranscodeSessionRequest](../../models/operations/starttranscodesessionrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.StartTranscodeSessionResponse](../../models/operations/starttranscodesessionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |