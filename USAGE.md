<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
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
        auto_adjust_quality=components.BoolInt.ONE,
        auto_adjust_subtitle=components.BoolInt.ONE,
        direct_play=components.BoolInt.ONE,
        direct_stream=components.BoolInt.ONE,
        direct_stream_audio=components.BoolInt.ONE,
        disable_resolution_rotation=components.BoolInt.ONE,
        has_mde=components.BoolInt.ONE,
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

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from plex_api_client import PlexAPI
from plex_api_client.models import components, operations

async def main():

    async with PlexAPI(
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

        res = await plex_api.transcoder.start_transcode_session_async(request=operations.StartTranscodeSessionRequest(
            transcode_type=components.TranscodeType.MUSIC,
            extension=operations.Extension.MPD,
            advanced_subtitles=components.AdvancedSubtitles.BURN,
            audio_boost=50,
            audio_channel_count=5,
            auto_adjust_quality=components.BoolInt.ONE,
            auto_adjust_subtitle=components.BoolInt.ONE,
            direct_play=components.BoolInt.ONE,
            direct_stream=components.BoolInt.ONE,
            direct_stream_audio=components.BoolInt.ONE,
            disable_resolution_rotation=components.BoolInt.ONE,
            has_mde=components.BoolInt.ONE,
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

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->