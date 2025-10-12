# plexpy

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>

<!-- Start Summary [summary] -->
## Summary


<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [plexpy](#plexpy)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [File uploads](#file-uploads)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Authentication](#authentication)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add plex-api-client
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install plex-api-client
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add plex-api-client
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from plex-api-client python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "plex-api-client",
# ]
# ///

from plex_api_client import PlexAPI

sdk = PlexAPI(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

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

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [activities](docs/sdks/activities/README.md)

* [list_activities](docs/sdks/activities/README.md#list_activities) - Get all activities
* [cancel_activity](docs/sdks/activities/README.md#cancel_activity) - Cancel a running activity

### [butler](docs/sdks/butler/README.md)

* [stop_tasks](docs/sdks/butler/README.md#stop_tasks) - Stop all Butler tasks
* [get_tasks](docs/sdks/butler/README.md#get_tasks) - Get all Butler tasks
* [start_tasks](docs/sdks/butler/README.md#start_tasks) - Start all Butler tasks
* [stop_task](docs/sdks/butler/README.md#stop_task) - Stop a single Butler task
* [start_task](docs/sdks/butler/README.md#start_task) - Start a single Butler task

### [collections](docs/sdks/collections/README.md)

* [create_collection](docs/sdks/collections/README.md#create_collection) - Create collection

### [content](docs/sdks/content/README.md)

* [get_collection_items](docs/sdks/content/README.md#get_collection_items) - Get items in a collection
* [get_metadata_item](docs/sdks/content/README.md#get_metadata_item) - Get a metadata item
* [get_albums](docs/sdks/content/README.md#get_albums) - Set section albums
* [list_content](docs/sdks/content/README.md#list_content) - Get items in the section
* [get_all_leaves](docs/sdks/content/README.md#get_all_leaves) - Set section leaves
* [get_arts](docs/sdks/content/README.md#get_arts) - Set section artwork
* [get_categories](docs/sdks/content/README.md#get_categories) - Set section categories
* [get_cluster](docs/sdks/content/README.md#get_cluster) - Set section clusters
* [get_sonic_path](docs/sdks/content/README.md#get_sonic_path) - Similar tracks to transition from one to another
* [get_folders](docs/sdks/content/README.md#get_folders) - Get all folder locations
* [list_moments](docs/sdks/content/README.md#list_moments) - Set section moments
* [get_sonically_similar](docs/sdks/content/README.md#get_sonically_similar) - The nearest audio tracks
* [get_collection_image](docs/sdks/content/README.md#get_collection_image) - Get a collection's image

### [devices](docs/sdks/devices/README.md)

* [get_available_grabbers](docs/sdks/devices/README.md#get_available_grabbers) - Get available grabbers
* [list_devices](docs/sdks/devices/README.md#list_devices) - Get all devices
* [add_device](docs/sdks/devices/README.md#add_device) - Add a device
* [discover_devices](docs/sdks/devices/README.md#discover_devices) - Tell grabbers to discover devices
* [remove_device](docs/sdks/devices/README.md#remove_device) - Remove a device
* [get_device_details](docs/sdks/devices/README.md#get_device_details) - Get device details
* [modify_device](docs/sdks/devices/README.md#modify_device) - Enable or disable a device
* [set_channelmap](docs/sdks/devices/README.md#set_channelmap) - Set a device's channel mapping
* [get_devices_channels](docs/sdks/devices/README.md#get_devices_channels) - Get a device's channels
* [set_device_preferences](docs/sdks/devices/README.md#set_device_preferences) - Set device preferences
* [stop_scan](docs/sdks/devices/README.md#stop_scan) - Tell a device to stop scanning for channels
* [scan](docs/sdks/devices/README.md#scan) - Tell a device to scan for channels
* [get_thumb](docs/sdks/devices/README.md#get_thumb) - Get device thumb

### [download_queue](docs/sdks/downloadqueue/README.md)

* [create_download_queue](docs/sdks/downloadqueue/README.md#create_download_queue) - Create download queue
* [get_download_queue](docs/sdks/downloadqueue/README.md#get_download_queue) - Get a download queue
* [add_download_queue_items](docs/sdks/downloadqueue/README.md#add_download_queue_items) - Add to download queue
* [list_download_queue_items](docs/sdks/downloadqueue/README.md#list_download_queue_items) - Get download queue items
* [get_item_decision](docs/sdks/downloadqueue/README.md#get_item_decision) - Grab download queue item decision
* [get_download_queue_media](docs/sdks/downloadqueue/README.md#get_download_queue_media) - Grab download queue media
* [remove_download_queue_items](docs/sdks/downloadqueue/README.md#remove_download_queue_items) - Delete download queue items
* [get_download_queue_items](docs/sdks/downloadqueue/README.md#get_download_queue_items) - Get download queue items
* [restart_processing_download_queue_items](docs/sdks/downloadqueue/README.md#restart_processing_download_queue_items) - Restart processing of items from the decision

### [dv_rs](docs/sdks/dvrs/README.md)

* [list_dv_rs](docs/sdks/dvrs/README.md#list_dv_rs) - Get DVRs
* [create_dvr](docs/sdks/dvrs/README.md#create_dvr) - Create a DVR
* [delete_dvr](docs/sdks/dvrs/README.md#delete_dvr) - Delete a single DVR
* [get_dvr](docs/sdks/dvrs/README.md#get_dvr) - Get a single DVR
* [delete_lineup](docs/sdks/dvrs/README.md#delete_lineup) - Delete a DVR Lineup
* [add_lineup](docs/sdks/dvrs/README.md#add_lineup) - Add a DVR Lineup
* [set_dvr_preferences](docs/sdks/dvrs/README.md#set_dvr_preferences) - Set DVR preferences
* [stop_dvr_reload](docs/sdks/dvrs/README.md#stop_dvr_reload) - Tell a DVR to stop reloading program guide
* [reload_guide](docs/sdks/dvrs/README.md#reload_guide) - Tell a DVR to reload program guide
* [tune_channel](docs/sdks/dvrs/README.md#tune_channel) - Tune a channel on a DVR
* [remove_device_from_dvr](docs/sdks/dvrs/README.md#remove_device_from_dvr) - Remove a device from an existing DVR
* [add_device_to_dvr](docs/sdks/dvrs/README.md#add_device_to_dvr) - Add a device to an existing DVR

### [epg](docs/sdks/epg/README.md)

* [compute_channel_map](docs/sdks/epg/README.md#compute_channel_map) - Compute the best channel map
* [get_channels](docs/sdks/epg/README.md#get_channels) - Get channels for a lineup
* [get_countries](docs/sdks/epg/README.md#get_countries) - Get all countries
* [get_all_languages](docs/sdks/epg/README.md#get_all_languages) - Get all languages
* [get_lineup](docs/sdks/epg/README.md#get_lineup) - Compute the best lineup
* [get_lineup_channels](docs/sdks/epg/README.md#get_lineup_channels) - Get the channels for mulitple lineups
* [get_countries_lineups](docs/sdks/epg/README.md#get_countries_lineups) - Get lineups for a country via postal code
* [get_country_regions](docs/sdks/epg/README.md#get_country_regions) - Get regions for a country
* [list_lineups](docs/sdks/epg/README.md#list_lineups) - Get lineups for a region

### [events](docs/sdks/events/README.md)

* [get_notifications](docs/sdks/events/README.md#get_notifications) - Connect to Eventsource
* [connect_web_socket](docs/sdks/events/README.md#connect_web_socket) - Connect to WebSocket

### [general](docs/sdks/general/README.md)

* [get_server_info](docs/sdks/general/README.md#get_server_info) - Get PMS info
* [get_identity](docs/sdks/general/README.md#get_identity) - Get PMS identity
* [get_source_connection_information](docs/sdks/general/README.md#get_source_connection_information) - Get Source Connection Information
* [get_transient_token](docs/sdks/general/README.md#get_transient_token) - Get Transient Tokens

### [hubs](docs/sdks/hubs/README.md)

* [get_all_hubs](docs/sdks/hubs/README.md#get_all_hubs) - Get global hubs
* [get_continue_watching](docs/sdks/hubs/README.md#get_continue_watching) - Get the continue watching hub
* [get_hub_items](docs/sdks/hubs/README.md#get_hub_items) - Get a hub's items
* [get_promoted_hubs](docs/sdks/hubs/README.md#get_promoted_hubs) - Get the hubs which are promoted
* [get_metadata_hubs](docs/sdks/hubs/README.md#get_metadata_hubs) - Get hubs for section by metadata item
* [get_postplay_hubs](docs/sdks/hubs/README.md#get_postplay_hubs) - Get postplay hubs
* [get_related_hubs](docs/sdks/hubs/README.md#get_related_hubs) - Get related hubs
* [get_section_hubs](docs/sdks/hubs/README.md#get_section_hubs) - Get section hubs
* [reset_section_defaults](docs/sdks/hubs/README.md#reset_section_defaults) - Reset hubs to defaults
* [list_hubs](docs/sdks/hubs/README.md#list_hubs) - Get hubs
* [create_custom_hub](docs/sdks/hubs/README.md#create_custom_hub) - Create a custom hub
* [move_hub](docs/sdks/hubs/README.md#move_hub) - Move Hub
* [delete_custom_hub](docs/sdks/hubs/README.md#delete_custom_hub) - Delete a custom hub
* [update_hub_visibility](docs/sdks/hubs/README.md#update_hub_visibility) - Change hub visibility

### [library](docs/sdks/library/README.md)

* [get_library_items](docs/sdks/library/README.md#get_library_items) - Get all items in library
* [delete_caches](docs/sdks/library/README.md#delete_caches) - Delete library caches
* [clean_bundles](docs/sdks/library/README.md#clean_bundles) - Clean bundles
* [ingest_transient_item](docs/sdks/library/README.md#ingest_transient_item) - Ingest a transient item
* [get_library_matches](docs/sdks/library/README.md#get_library_matches) - Get library matches
* [optimize_database](docs/sdks/library/README.md#optimize_database) - Optimize the Database
* [get_random_artwork](docs/sdks/library/README.md#get_random_artwork) - Get random artwork
* [get_sections](docs/sdks/library/README.md#get_sections) - Get library sections (main Media Provider Only)
* [add_section](docs/sdks/library/README.md#add_section) - Add a library section
* [stop_all_refreshes](docs/sdks/library/README.md#stop_all_refreshes) - Stop refresh
* [get_sections_prefs](docs/sdks/library/README.md#get_sections_prefs) - Get section prefs
* [refresh_sections_metadata](docs/sdks/library/README.md#refresh_sections_metadata) - Refresh all sections
* [get_tags](docs/sdks/library/README.md#get_tags) - Get all library tags of a type
* [delete_metadata_item](docs/sdks/library/README.md#delete_metadata_item) - Delete a metadata item
* [edit_metadata_item](docs/sdks/library/README.md#edit_metadata_item) - Edit a metadata item
* [detect_ads](docs/sdks/library/README.md#detect_ads) - Ad-detect an item
* [get_all_item_leaves](docs/sdks/library/README.md#get_all_item_leaves) - Get the leaves of an item
* [analyze_metadata](docs/sdks/library/README.md#analyze_metadata) - Analyze an item
* [generate_thumbs](docs/sdks/library/README.md#generate_thumbs) - Generate thumbs of chapters for an item
* [detect_credits](docs/sdks/library/README.md#detect_credits) - Credit detect a metadata item
* [get_extras](docs/sdks/library/README.md#get_extras) - Get an item's extras
* [add_extras](docs/sdks/library/README.md#add_extras) - Add to an item's extras
* [get_file](docs/sdks/library/README.md#get_file) - Get a file from a metadata or media bundle
* [start_bif_generation](docs/sdks/library/README.md#start_bif_generation) - Start BIF generation of an item
* [detect_intros](docs/sdks/library/README.md#detect_intros) - Intro detect an item
* [create_marker](docs/sdks/library/README.md#create_marker) - Create a marker
* [match_item](docs/sdks/library/README.md#match_item) - Match a metadata item
* [list_matches](docs/sdks/library/README.md#list_matches) - Get metadata matches for an item
* [merge_items](docs/sdks/library/README.md#merge_items) - Merge a metadata item
* [list_sonically_similar](docs/sdks/library/README.md#list_sonically_similar) - Get nearest tracks to metadata item
* [set_item_preferences](docs/sdks/library/README.md#set_item_preferences) - Set metadata preferences
* [refresh_items_metadata](docs/sdks/library/README.md#refresh_items_metadata) - Refresh a metadata item
* [get_related_items](docs/sdks/library/README.md#get_related_items) - Get related items
* [list_similar](docs/sdks/library/README.md#list_similar) - Get similar items
* [split_item](docs/sdks/library/README.md#split_item) - Split a metadata item
* [add_subtitles](docs/sdks/library/README.md#add_subtitles) - Add subtitles
* [get_item_tree](docs/sdks/library/README.md#get_item_tree) - Get metadata items as a tree
* [unmatch](docs/sdks/library/README.md#unmatch) - Unmatch a metadata item
* [list_top_users](docs/sdks/library/README.md#list_top_users) - Get metadata top users
* [detect_voice_activity](docs/sdks/library/README.md#detect_voice_activity) - Detect voice activity
* [get_augmentation_status](docs/sdks/library/README.md#get_augmentation_status) - Get augmentation status
* [set_stream_selection](docs/sdks/library/README.md#set_stream_selection) - Set stream selection
* [get_person](docs/sdks/library/README.md#get_person) - Get person details
* [list_person_media](docs/sdks/library/README.md#list_person_media) - Get media for a person
* [delete_library_section](docs/sdks/library/README.md#delete_library_section) - Delete a library section
* [get_library_details](docs/sdks/library/README.md#get_library_details) - Get a library section by id
* [edit_section](docs/sdks/library/README.md#edit_section) - Edit a library section
* [update_items](docs/sdks/library/README.md#update_items) - Set the fields of the filtered items
* [start_analysis](docs/sdks/library/README.md#start_analysis) - Analyze a section
* [autocomplete](docs/sdks/library/README.md#autocomplete) - Get autocompletions for search
* [get_collections](docs/sdks/library/README.md#get_collections) - Get collections in a section
* [get_common](docs/sdks/library/README.md#get_common) - Get common fields for items
* [empty_trash](docs/sdks/library/README.md#empty_trash) - Empty section trash
* [get_section_filters](docs/sdks/library/README.md#get_section_filters) - Get section filters
* [get_first_characters](docs/sdks/library/README.md#get_first_characters) - Get list of first characters
* [delete_indexes](docs/sdks/library/README.md#delete_indexes) - Delete section indexes
* [delete_intros](docs/sdks/library/README.md#delete_intros) - Delete section intro markers
* [get_section_preferences](docs/sdks/library/README.md#get_section_preferences) - Get section prefs
* [set_section_preferences](docs/sdks/library/README.md#set_section_preferences) - Set section prefs
* [cancel_refresh](docs/sdks/library/README.md#cancel_refresh) - Cancel section refresh
* [refresh_section](docs/sdks/library/README.md#refresh_section) - Refresh section
* [get_available_sorts](docs/sdks/library/README.md#get_available_sorts) - Get a section sorts
* [get_stream_levels](docs/sdks/library/README.md#get_stream_levels) - Get loudness about a stream in json
* [get_stream_loudness](docs/sdks/library/README.md#get_stream_loudness) - Get loudness about a stream
* [get_chapter_image](docs/sdks/library/README.md#get_chapter_image) - Get a chapter image
* [set_item_artwork](docs/sdks/library/README.md#set_item_artwork) - Set an item's artwork, theme, etc
* [update_item_artwork](docs/sdks/library/README.md#update_item_artwork) - Set an item's artwork, theme, etc
* [delete_marker](docs/sdks/library/README.md#delete_marker) - Delete a marker
* [edit_marker](docs/sdks/library/README.md#edit_marker) - Edit a marker
* [delete_media_item](docs/sdks/library/README.md#delete_media_item) - Delete a media item
* [get_part_index](docs/sdks/library/README.md#get_part_index) - Get BIF index for a part
* [delete_collection](docs/sdks/library/README.md#delete_collection) - Delete a collection
* [get_section_image](docs/sdks/library/README.md#get_section_image) - Get a section composite image
* [delete_stream](docs/sdks/library/README.md#delete_stream) - Delete a stream
* [get_stream](docs/sdks/library/README.md#get_stream) - Get a stream
* [set_stream_offset](docs/sdks/library/README.md#set_stream_offset) - Set a stream offset
* [get_item_artwork](docs/sdks/library/README.md#get_item_artwork) - Get an item's artwork, theme, etc
* [get_media_part](docs/sdks/library/README.md#get_media_part) - Get a media part
* [get_image_from_bif](docs/sdks/library/README.md#get_image_from_bif) - Get an image from part BIF

### [library_collections](docs/sdks/librarycollections/README.md)

* [add_collection_items](docs/sdks/librarycollections/README.md#add_collection_items) - Add items to a collection
* [delete_collection_item](docs/sdks/librarycollections/README.md#delete_collection_item) - Delete an item from a collection
* [move_collection_item](docs/sdks/librarycollections/README.md#move_collection_item) - Reorder an item in the collection

### [library_playlists](docs/sdks/libraryplaylists/README.md)

* [create_playlist](docs/sdks/libraryplaylists/README.md#create_playlist) - Create a Playlist
* [upload_playlist](docs/sdks/libraryplaylists/README.md#upload_playlist) - Upload
* [delete_playlist](docs/sdks/libraryplaylists/README.md#delete_playlist) - Delete a Playlist
* [update_playlist](docs/sdks/libraryplaylists/README.md#update_playlist) - Editing a Playlist
* [get_playlist_generators](docs/sdks/libraryplaylists/README.md#get_playlist_generators) - Get a playlist's generators
* [clear_playlist_items](docs/sdks/libraryplaylists/README.md#clear_playlist_items) - Clearing a playlist
* [add_playlist_items](docs/sdks/libraryplaylists/README.md#add_playlist_items) - Adding to  a Playlist
* [delete_playlist_item](docs/sdks/libraryplaylists/README.md#delete_playlist_item) - Delete a Generator
* [get_playlist_generator](docs/sdks/libraryplaylists/README.md#get_playlist_generator) - Get a playlist generator
* [modify_playlist_generator](docs/sdks/libraryplaylists/README.md#modify_playlist_generator) - Modify a Generator
* [get_playlist_generator_items](docs/sdks/libraryplaylists/README.md#get_playlist_generator_items) - Get a playlist generator's items
* [move_playlist_item](docs/sdks/libraryplaylists/README.md#move_playlist_item) - Moving items in a playlist
* [refresh_playlist](docs/sdks/libraryplaylists/README.md#refresh_playlist) - Reprocess a generator

### [live_tv](docs/sdks/livetv/README.md)

* [get_sessions](docs/sdks/livetv/README.md#get_sessions) - Get all sessions
* [get_live_tv_session](docs/sdks/livetv/README.md#get_live_tv_session) - Get a single session
* [get_session_playlist_index](docs/sdks/livetv/README.md#get_session_playlist_index) - Get a session playlist index
* [get_session_segment](docs/sdks/livetv/README.md#get_session_segment) - Get a single session segment

### [log](docs/sdks/log/README.md)

* [write_log](docs/sdks/log/README.md#write_log) - Logging a multi-line message to the Plex Media Server log
* [write_message](docs/sdks/log/README.md#write_message) - Logging a single-line message to the Plex Media Server log
* [enable_papertrail](docs/sdks/log/README.md#enable_papertrail) - Enabling Papertrail

### [play_queue](docs/sdks/playqueue/README.md)

* [create_play_queue](docs/sdks/playqueue/README.md#create_play_queue) - Create a play queue
* [get_play_queue](docs/sdks/playqueue/README.md#get_play_queue) - Retrieve a play queue
* [add_to_play_queue](docs/sdks/playqueue/README.md#add_to_play_queue) - Add a generator or playlist to a play queue
* [clear_play_queue](docs/sdks/playqueue/README.md#clear_play_queue) - Clear a play queue
* [reset_play_queue](docs/sdks/playqueue/README.md#reset_play_queue) - Reset a play queue
* [shuffle](docs/sdks/playqueue/README.md#shuffle) - Shuffle a play queue
* [unshuffle](docs/sdks/playqueue/README.md#unshuffle) - Unshuffle a play queue
* [delete_play_queue_item](docs/sdks/playqueue/README.md#delete_play_queue_item) - Delete an item from a play queue
* [move_play_queue_item](docs/sdks/playqueue/README.md#move_play_queue_item) - Move an item in a play queue

### [playlist](docs/sdks/playlist/README.md)

* [list_playlists](docs/sdks/playlist/README.md#list_playlists) - List playlists
* [get_playlist](docs/sdks/playlist/README.md#get_playlist) - Retrieve Playlist
* [get_playlist_items](docs/sdks/playlist/README.md#get_playlist_items) - Retrieve Playlist Contents

### [preferences](docs/sdks/preferences/README.md)

* [get_all_preferences](docs/sdks/preferences/README.md#get_all_preferences) - Get all preferences
* [set_preferences](docs/sdks/preferences/README.md#set_preferences) - Set preferences
* [get_preference](docs/sdks/preferences/README.md#get_preference) - Get a preferences

### [provider](docs/sdks/provider/README.md)

* [list_providers](docs/sdks/provider/README.md#list_providers) - Get the list of available media providers
* [add_provider](docs/sdks/provider/README.md#add_provider) - Add a media provider
* [refresh_providers](docs/sdks/provider/README.md#refresh_providers) - Refresh media providers
* [delete_media_provider](docs/sdks/provider/README.md#delete_media_provider) - Delete a media provider

### [rate](docs/sdks/rate/README.md)

* [set_rating](docs/sdks/rate/README.md#set_rating) - Rate an item

### [search](docs/sdks/search/README.md)

* [search_hubs](docs/sdks/search/README.md#search_hubs) - Search Hub
* [voice_search_hubs](docs/sdks/search/README.md#voice_search_hubs) - Voice Search Hub

### [status](docs/sdks/status/README.md)

* [list_sessions](docs/sdks/status/README.md#list_sessions) - List Sessions
* [get_background_tasks](docs/sdks/status/README.md#get_background_tasks) - Get background tasks
* [list_playback_history](docs/sdks/status/README.md#list_playback_history) - List Playback History
* [terminate_session](docs/sdks/status/README.md#terminate_session) - Terminate a session
* [delete_history](docs/sdks/status/README.md#delete_history) - Delete Single History Item
* [get_history_item](docs/sdks/status/README.md#get_history_item) - Get Single History Item

### [subscriptions](docs/sdks/subscriptions/README.md)

* [get_all_subscriptions](docs/sdks/subscriptions/README.md#get_all_subscriptions) - Get all subscriptions
* [create_subscription](docs/sdks/subscriptions/README.md#create_subscription) - Create a subscription
* [process_subscriptions](docs/sdks/subscriptions/README.md#process_subscriptions) - Process all subscriptions
* [get_scheduled_recordings](docs/sdks/subscriptions/README.md#get_scheduled_recordings) - Get all scheduled recordings
* [get_template](docs/sdks/subscriptions/README.md#get_template) - Get the subscription template
* [cancel_grab](docs/sdks/subscriptions/README.md#cancel_grab) - Cancel an existing grab
* [delete_subscription](docs/sdks/subscriptions/README.md#delete_subscription) - Delete a subscription
* [get_subscription](docs/sdks/subscriptions/README.md#get_subscription) - Get a single subscription
* [edit_subscription_preferences](docs/sdks/subscriptions/README.md#edit_subscription_preferences) - Edit a subscription
* [reorder_subscription](docs/sdks/subscriptions/README.md#reorder_subscription) - Re-order a subscription

### [timeline](docs/sdks/timeline/README.md)

* [mark_played](docs/sdks/timeline/README.md#mark_played) - Mark an item as played
* [report](docs/sdks/timeline/README.md#report) - Report media timeline
* [unscrobble](docs/sdks/timeline/README.md#unscrobble) - Mark an item as unplayed

### [transcoder](docs/sdks/transcoder/README.md)

* [transcode_image](docs/sdks/transcoder/README.md#transcode_image) - Transcode an image
* [make_decision](docs/sdks/transcoder/README.md#make_decision) - Make a decision on media playback
* [trigger_fallback](docs/sdks/transcoder/README.md#trigger_fallback) - Manually trigger a transcoder fallback
* [transcode_subtitles](docs/sdks/transcoder/README.md#transcode_subtitles) - Transcode subtitles
* [start_transcode_session](docs/sdks/transcoder/README.md#start_transcode_session) - Start A Transcoding Session

### [ultra_blur](docs/sdks/ultrablur/README.md)

* [get_colors](docs/sdks/ultrablur/README.md#get_colors) - Get UltraBlur Colors
* [get_image](docs/sdks/ultrablur/README.md#get_image) - Get UltraBlur Image

### [updater](docs/sdks/updater/README.md)

* [apply_updates](docs/sdks/updater/README.md#apply_updates) - Applying updates
* [check_updates](docs/sdks/updater/README.md#check_updates) - Checking for updates
* [get_updates_status](docs/sdks/updater/README.md#get_updates_status) - Querying status of updates

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

```python
from plex_api_client import PlexAPI


with PlexAPI(
    token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.log.write_log(request=open("example.file", "rb"))

    assert res is not None

    # Handle response
    print(res)

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from plex_api_client import PlexAPI
from plex_api_client.models import components
from plex_api_client.utils import BackoffStrategy, RetryConfig


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

    res = plex_api.general.get_server_info(request={},
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    assert res.media_container_with_directory is not None

    # Handle response
    print(res.media_container_with_directory)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from plex_api_client import PlexAPI
from plex_api_client.models import components
from plex_api_client.utils import BackoffStrategy, RetryConfig


with PlexAPI(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
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

    res = plex_api.general.get_server_info(request={})

    assert res.media_container_with_directory is not None

    # Handle response
    print(res.media_container_with_directory)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`PlexAPIError`](./src/plex_api_client/models/errors/plexapierror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                            |
| ------------------ | ---------------- | ------------------------------------------------------ |
| `err.message`      | `str`            | Error message                                          |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                     |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                  |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned. |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                      |

### Example
```python
from plex_api_client import PlexAPI
from plex_api_client.models import components, errors


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
    res = None
    try:

        res = plex_api.general.get_server_info(request={})

        assert res.media_container_with_directory is not None

        # Handle response
        print(res.media_container_with_directory)


    except errors.PlexAPIError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

```

### Error Classes
**Primary error:**
* [`PlexAPIError`](./src/plex_api_client/models/errors/plexapierror.py): The base class for HTTP error responses.

<details><summary>Less common errors (5)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`PlexAPIError`](./src/plex_api_client/models/errors/plexapierror.py)**:
* [`ResponseValidationError`](./src/plex_api_client/models/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| #   | Server                                                     | Variables                                    | Description |
| --- | ---------------------------------------------------------- | -------------------------------------------- | ----------- |
| 0   | `https://{IP-description}.{identifier}.plex.direct:{port}` | `identifier`<br/>`IP-description`<br/>`port` |             |
| 1   | `{protocol}://{host}:{port}`                               | `protocol`<br/>`host`<br/>`port`             |             |
| 2   | `https://{server_url}`                                     | `server_url`                                 |             |

If the selected server has variables, you may override its default values through the additional parameters made available in the SDK constructor:

| Variable         | Parameter                | Default                              | Description                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------- | ------------------------ | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `identifier`     | `identifier: str`        | `"0123456789abcdef0123456789abcdef"` | The unique identifier of this particular PMS                                                                                                                                                                                                                                                                                                                                         |
| `IP-description` | `ip_description: str`    | `"1-2-3-4"`                          | A `-` separated string of the IPv4 or IPv6 address components                                                                                                                                                                                                                                                                                                                        |
| `port`           | `port: str`              | `"32400"`                            | The Port number configured on the PMS. Typically (`32400`). <br/>If using a reverse proxy, this would be the port number configured on the proxy.<br/>                                                                                                                                                                                                                               |
| `protocol`       | `protocol: str`          | `"http"`                             | The network protocol to use. Typically (`http` or `https`)                                                                                                                                                                                                                                                                                                                           |
| `host`           | `host: str`              | `"localhost"`                        | The Host of the PMS.<br/>If using on a local network, this is the internal IP address of the server hosting the PMS.<br/>If using on an external network, this is the external IP address for your network, and requires port forwarding.<br/>If using a reverse proxy, this would be the external DNS domain for your network, and requires the proxy handle port forwarding. <br/> |
| `server_url`     | `server_url_global: str` | `"http://localhost:32400"`           | The full manual URL to access the PMS                                                                                                                                                                                                                                                                                                                                                |

#### Example

```python
from plex_api_client import PlexAPI
from plex_api_client.models import components


with PlexAPI(
    server_idx=1,
    protocol="<value>"
    host="electric-excess.name"
    port="36393"
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

    res = plex_api.general.get_server_info(request={})

    assert res.media_container_with_directory is not None

    # Handle response
    print(res.media_container_with_directory)

```

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from plex_api_client import PlexAPI
from plex_api_client.models import components


with PlexAPI(
    server_url="https://http://localhost:32400",
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

    res = plex_api.general.get_server_info(request={})

    assert res.media_container_with_directory is not None

    # Handle response
    print(res.media_container_with_directory)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from plex_api_client import PlexAPI
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = PlexAPI(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from plex_api_client import PlexAPI
from plex_api_client.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = PlexAPI(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name    | Type   | Scheme  |
| ------- | ------ | ------- |
| `token` | apiKey | API key |

To authenticate with the API the `token` parameter must be set when initializing the SDK client instance. For example:
```python
from plex_api_client import PlexAPI
from plex_api_client.models import components


with PlexAPI(
    token="<YOUR_API_KEY_HERE>",
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
) as plex_api:

    res = plex_api.general.get_server_info(request={})

    assert res.media_container_with_directory is not None

    # Handle response
    print(res.media_container_with_directory)

```
<!-- End Authentication [security] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `PlexAPI` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from plex_api_client import PlexAPI
from plex_api_client.models import components
def main():

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
        # Rest of application here...


# Or when using async:
async def amain():

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
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from plex_api_client import PlexAPI
import logging

logging.basicConfig(level=logging.DEBUG)
s = PlexAPI(debug_logger=logging.getLogger("plex_api_client"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
