"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from plex_api import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Directory:
    count: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('count'), 'exclude': lambda f: f is None }})
    key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('key'), 'exclude': lambda f: f is None }})
    title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class MediaContainer:
    allow_camera_upload: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allowCameraUpload'), 'exclude': lambda f: f is None }})
    allow_channel_access: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allowChannelAccess'), 'exclude': lambda f: f is None }})
    allow_media_deletion: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allowMediaDeletion'), 'exclude': lambda f: f is None }})
    allow_sharing: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allowSharing'), 'exclude': lambda f: f is None }})
    allow_sync: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allowSync'), 'exclude': lambda f: f is None }})
    allow_tuners: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allowTuners'), 'exclude': lambda f: f is None }})
    background_processing: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('backgroundProcessing'), 'exclude': lambda f: f is None }})
    certificate: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('certificate'), 'exclude': lambda f: f is None }})
    companion_proxy: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('companionProxy'), 'exclude': lambda f: f is None }})
    country_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('countryCode'), 'exclude': lambda f: f is None }})
    diagnostics: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('diagnostics'), 'exclude': lambda f: f is None }})
    directory: Optional[List[Directory]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Directory'), 'exclude': lambda f: f is None }})
    event_stream: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('eventStream'), 'exclude': lambda f: f is None }})
    friendly_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('friendlyName'), 'exclude': lambda f: f is None }})
    hub_search: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hubSearch'), 'exclude': lambda f: f is None }})
    item_clusters: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('itemClusters'), 'exclude': lambda f: f is None }})
    livetv: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('livetv'), 'exclude': lambda f: f is None }})
    machine_identifier: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('machineIdentifier'), 'exclude': lambda f: f is None }})
    media_providers: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mediaProviders'), 'exclude': lambda f: f is None }})
    multiuser: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('multiuser'), 'exclude': lambda f: f is None }})
    music_analysis: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('musicAnalysis'), 'exclude': lambda f: f is None }})
    my_plex: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('myPlex'), 'exclude': lambda f: f is None }})
    my_plex_mapping_state: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('myPlexMappingState'), 'exclude': lambda f: f is None }})
    my_plex_signin_state: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('myPlexSigninState'), 'exclude': lambda f: f is None }})
    my_plex_subscription: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('myPlexSubscription'), 'exclude': lambda f: f is None }})
    my_plex_username: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('myPlexUsername'), 'exclude': lambda f: f is None }})
    offline_transcode: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('offlineTranscode'), 'exclude': lambda f: f is None }})
    owner_features: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ownerFeatures'), 'exclude': lambda f: f is None }})
    photo_auto_tag: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('photoAutoTag'), 'exclude': lambda f: f is None }})
    platform: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('platform'), 'exclude': lambda f: f is None }})
    platform_version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('platformVersion'), 'exclude': lambda f: f is None }})
    plugin_host: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pluginHost'), 'exclude': lambda f: f is None }})
    push_notifications: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pushNotifications'), 'exclude': lambda f: f is None }})
    read_only_libraries: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('readOnlyLibraries'), 'exclude': lambda f: f is None }})
    size: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('size'), 'exclude': lambda f: f is None }})
    streaming_brain_abr_version: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streamingBrainABRVersion'), 'exclude': lambda f: f is None }})
    streaming_brain_version: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streamingBrainVersion'), 'exclude': lambda f: f is None }})
    sync: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sync'), 'exclude': lambda f: f is None }})
    transcoder_active_video_sessions: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transcoderActiveVideoSessions'), 'exclude': lambda f: f is None }})
    transcoder_audio: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transcoderAudio'), 'exclude': lambda f: f is None }})
    transcoder_lyrics: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transcoderLyrics'), 'exclude': lambda f: f is None }})
    transcoder_photo: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transcoderPhoto'), 'exclude': lambda f: f is None }})
    transcoder_subtitles: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transcoderSubtitles'), 'exclude': lambda f: f is None }})
    transcoder_video: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transcoderVideo'), 'exclude': lambda f: f is None }})
    transcoder_video_bitrates: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transcoderVideoBitrates'), 'exclude': lambda f: f is None }})
    transcoder_video_qualities: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transcoderVideoQualities'), 'exclude': lambda f: f is None }})
    transcoder_video_resolutions: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transcoderVideoResolutions'), 'exclude': lambda f: f is None }})
    updated_at: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt'), 'exclude': lambda f: f is None }})
    updater: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updater'), 'exclude': lambda f: f is None }})
    version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('version'), 'exclude': lambda f: f is None }})
    voice_search: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('voiceSearch'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetServerCapabilitiesResponseBody:
    r"""The Server Capabilities"""
    media_container: Optional[MediaContainer] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('MediaContainer'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class GetServerCapabilitiesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    object: Optional[GetServerCapabilitiesResponseBody] = dataclasses.field(default=None)
    r"""The Server Capabilities"""
    

