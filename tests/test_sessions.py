"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

import dateutil.parser
from plex_api_client import PlexAPI
from plex_api_client.models import operations


def test_sessions_get_sessions():
    s = PlexAPI(
        access_token="<YOUR_API_KEY_HERE>",
    )

    assert s is not None

    res = s.sessions.get_sessions()
    assert res.status_code == 200
    assert res.object is not None
    assert res.object == operations.GetSessionsResponseBody(
        media_container=operations.GetSessionsMediaContainer(
            size=1,
            metadata=[
                operations.GetSessionsMetadata(
                    added_at=1705543312,
                    art="/library/metadata/39904/art/1705310687",
                    duration=186240,
                    grandparent_art="/library/metadata/39904/art/1705310687",
                    grandparent_guid="plex://artist/5d07bbfd403c6402904a6480",
                    grandparent_key="/library/metadata/39904",
                    grandparent_rating_key="39904",
                    grandparent_thumb="/library/metadata/39904/thumb/1705310687",
                    grandparent_title="Green Day",
                    guid="plex://track/6535834f71f22f36f71a8e8f",
                    index=1,
                    key="/library/metadata/67085",
                    library_section_id="3",
                    library_section_key="/library/sections/3",
                    library_section_title="Music",
                    music_analysis_version="1",
                    parent_guid="plex://album/65394d6d472b8ab03ef47f12",
                    parent_index=1,
                    parent_key="/library/metadata/67084",
                    parent_rating_key="67084",
                    parent_studio="Reprise Records",
                    parent_thumb="/library/metadata/67084/thumb/1705543314",
                    parent_title="Saviors",
                    parent_year=2024,
                    rating_count=45885,
                    rating_key="67085",
                    session_key="203",
                    thumb="/library/metadata/67084/thumb/1705543314",
                    title="The American Dream Is Killing Me",
                    title_sort="American Dream Is Killing Me",
                    type="track",
                    updated_at=1705543314,
                    view_offset=1000,
                    media=[
                        operations.GetSessionsMedia(
                            audio_channels=2,
                            audio_codec="flac",
                            bitrate=1014,
                            container="flac",
                            duration=186240,
                            id="130355",
                            selected=True,
                            part=[
                                operations.GetSessionsPart(
                                    container="flac",
                                    duration=186240,
                                    file="/music/Green Day/Saviors (2024)/Green Day - Saviors - 01 - The American Dream Is Killing Me.flac",
                                    has_thumbnail="1",
                                    id="130625",
                                    key="/library/parts/130625/1705543268/file.flac",
                                    size=23644000,
                                    decision="directplay",
                                    selected=True,
                                    stream=[
                                        operations.GetSessionsStream(
                                            album_gain="-12.94",
                                            album_peak="1.000000",
                                            album_range="4.751014",
                                            audio_channel_layout="stereo",
                                            bit_depth=16,
                                            bitrate=1014,
                                            channels=2,
                                            codec="flac",
                                            display_title="FLAC (Stereo)",
                                            extended_display_title="FLAC (Stereo)",
                                            gain="-12.94",
                                            id="352487",
                                            index=0,
                                            loudness="-5.94",
                                            lra="1.74",
                                            peak="1.000000",
                                            sampling_rate=44100,
                                            selected=True,
                                            stream_type=2,
                                            location="direct",
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                    user=operations.GetSessionsUser(
                        id="1",
                        thumb="https://plex.tv/users/844780fc6f8a26b5/avatar?c=1705853661",
                        title="Blindkitty38",
                    ),
                    player=operations.Player(
                        address="10.10.10.171",
                        machine_identifier="3tsdzir85m2onc3qyr255aq1",
                        model="standalone",
                        platform="windows",
                        platform_version="10.0.22621",
                        product="Plex for Windows",
                        profile="Plex Desktop",
                        remote_public_address="68.248.140.20",
                        state="playing",
                        title="DESKTOP-BL80MTD",
                        version="1.85.0.4071-21128b56",
                        local=True,
                        relayed=False,
                        secure=True,
                        user_id=1,
                    ),
                    session=operations.Session(
                        id="93h7e00ncblxncqw9lkfaoxi",
                        bandwidth=1050,
                        location="lan",
                    ),
                ),
            ],
        ),
    )


def test_sessions_get_session_history_viewed_at_descending():
    s = PlexAPI(
        access_token="<YOUR_API_KEY_HERE>",
    )

    assert s is not None

    res = s.sessions.get_session_history(
        sort="viewedAt:desc", account_id=1, filter_={}, library_section_id=12
    )
    assert res.status_code == 200
    assert res.object is not None
    assert res.object == operations.GetSessionHistoryResponseBody(
        media_container=operations.GetSessionHistoryMediaContainer(
            size=10855,
            metadata=[
                operations.GetSessionHistoryMetadata(
                    history_key="/status/sessions/history/1",
                    key="/library/metadata/32171",
                    rating_key="32171",
                    library_section_id="2",
                    parent_key="/library/metadata/32170",
                    grandparent_key="/library/metadata/32132",
                    title="The Noise That Blue Makes",
                    grandparent_title="Taskmaster",
                    type="episode",
                    thumb="/library/metadata/32171/thumb/-1",
                    parent_thumb="/library/metadata/32170/thumb/1654134301",
                    grandparent_thumb="/library/metadata/32132/thumb/1703933346",
                    grandparent_art="/library/metadata/32132/art/1703933346",
                    index=1,
                    parent_index=13,
                    originally_available_at=dateutil.parser.parse(
                        "2022-04-14T00:00:00Z"
                    ).date(),
                    viewed_at=1654139223,
                    account_id=1,
                    device_id=5,
                ),
            ],
        ),
    )


def test_sessions_get_session_history_viewed_at_ascending():
    s = PlexAPI(
        access_token="<YOUR_API_KEY_HERE>",
    )

    assert s is not None

    res = s.sessions.get_session_history(
        sort="viewedAt:asc", account_id=1, filter_={}, library_section_id=12
    )
    assert res.status_code == 200
    assert res.object is not None
    assert res.object == operations.GetSessionHistoryResponseBody(
        media_container=operations.GetSessionHistoryMediaContainer(
            size=10855,
            metadata=[
                operations.GetSessionHistoryMetadata(
                    history_key="/status/sessions/history/1",
                    key="/library/metadata/32171",
                    rating_key="32171",
                    library_section_id="2",
                    parent_key="/library/metadata/32170",
                    grandparent_key="/library/metadata/32132",
                    title="The Noise That Blue Makes",
                    grandparent_title="Taskmaster",
                    type="episode",
                    thumb="/library/metadata/32171/thumb/-1",
                    parent_thumb="/library/metadata/32170/thumb/1654134301",
                    grandparent_thumb="/library/metadata/32132/thumb/1703933346",
                    grandparent_art="/library/metadata/32132/art/1703933346",
                    index=1,
                    parent_index=13,
                    originally_available_at=dateutil.parser.parse(
                        "2022-04-14T00:00:00Z"
                    ).date(),
                    viewed_at=1654139223,
                    account_id=1,
                    device_id=5,
                ),
            ],
        ),
    )


def test_sessions_get_session_history_rating_descending():
    s = PlexAPI(
        access_token="<YOUR_API_KEY_HERE>",
    )

    assert s is not None

    res = s.sessions.get_session_history(
        sort="rating:desc", account_id=1, filter_={}, library_section_id=12
    )
    assert res.status_code == 200
    assert res.object is not None
    assert res.object == operations.GetSessionHistoryResponseBody(
        media_container=operations.GetSessionHistoryMediaContainer(
            size=10855,
            metadata=[
                operations.GetSessionHistoryMetadata(
                    history_key="/status/sessions/history/1",
                    key="/library/metadata/32171",
                    rating_key="32171",
                    library_section_id="2",
                    parent_key="/library/metadata/32170",
                    grandparent_key="/library/metadata/32132",
                    title="The Noise That Blue Makes",
                    grandparent_title="Taskmaster",
                    type="episode",
                    thumb="/library/metadata/32171/thumb/-1",
                    parent_thumb="/library/metadata/32170/thumb/1654134301",
                    grandparent_thumb="/library/metadata/32132/thumb/1703933346",
                    grandparent_art="/library/metadata/32132/art/1703933346",
                    index=1,
                    parent_index=13,
                    originally_available_at=dateutil.parser.parse(
                        "2022-04-14T00:00:00Z"
                    ).date(),
                    viewed_at=1654139223,
                    account_id=1,
                    device_id=5,
                ),
            ],
        ),
    )


def test_sessions_get_session_history_rating_ascending():
    s = PlexAPI(
        access_token="<YOUR_API_KEY_HERE>",
    )

    assert s is not None

    res = s.sessions.get_session_history(
        sort="rating:asc", account_id=1, filter_={}, library_section_id=12
    )
    assert res.status_code == 200
    assert res.object is not None
    assert res.object == operations.GetSessionHistoryResponseBody(
        media_container=operations.GetSessionHistoryMediaContainer(
            size=10855,
            metadata=[
                operations.GetSessionHistoryMetadata(
                    history_key="/status/sessions/history/1",
                    key="/library/metadata/32171",
                    rating_key="32171",
                    library_section_id="2",
                    parent_key="/library/metadata/32170",
                    grandparent_key="/library/metadata/32132",
                    title="The Noise That Blue Makes",
                    grandparent_title="Taskmaster",
                    type="episode",
                    thumb="/library/metadata/32171/thumb/-1",
                    parent_thumb="/library/metadata/32170/thumb/1654134301",
                    grandparent_thumb="/library/metadata/32132/thumb/1703933346",
                    grandparent_art="/library/metadata/32132/art/1703933346",
                    index=1,
                    parent_index=13,
                    originally_available_at=dateutil.parser.parse(
                        "2022-04-14T00:00:00Z"
                    ).date(),
                    viewed_at=1654139223,
                    account_id=1,
                    device_id=5,
                ),
            ],
        ),
    )


def test_sessions_get_session_history_():
    s = PlexAPI(
        access_token="<YOUR_API_KEY_HERE>",
    )

    assert s is not None

    res = s.sessions.get_session_history(
        sort="viewedAt:desc", account_id=1, filter_={}, library_section_id=12
    )
    assert res.status_code == 200
    assert res.object is not None
    assert res.object == operations.GetSessionHistoryResponseBody(
        media_container=operations.GetSessionHistoryMediaContainer(
            size=10855,
            metadata=[
                operations.GetSessionHistoryMetadata(
                    history_key="/status/sessions/history/1",
                    key="/library/metadata/32171",
                    rating_key="32171",
                    library_section_id="2",
                    parent_key="/library/metadata/32170",
                    grandparent_key="/library/metadata/32132",
                    title="The Noise That Blue Makes",
                    grandparent_title="Taskmaster",
                    type="episode",
                    thumb="/library/metadata/32171/thumb/-1",
                    parent_thumb="/library/metadata/32170/thumb/1654134301",
                    grandparent_thumb="/library/metadata/32132/thumb/1703933346",
                    grandparent_art="/library/metadata/32132/art/1703933346",
                    index=1,
                    parent_index=13,
                    originally_available_at=dateutil.parser.parse(
                        "2022-04-14T00:00:00Z"
                    ).date(),
                    viewed_at=1654139223,
                    account_id=1,
                    device_id=5,
                ),
            ],
        ),
    )


def test_sessions_get_session_history_viewed_at():
    s = PlexAPI(
        access_token="<YOUR_API_KEY_HERE>",
    )

    assert s is not None

    res = s.sessions.get_session_history(
        account_id=1, filter_={}, library_section_id=12
    )
    assert res.status_code == 200
    assert res.object is not None
    assert res.object == operations.GetSessionHistoryResponseBody(
        media_container=operations.GetSessionHistoryMediaContainer(
            size=10855,
            metadata=[
                operations.GetSessionHistoryMetadata(
                    history_key="/status/sessions/history/1",
                    key="/library/metadata/32171",
                    rating_key="32171",
                    library_section_id="2",
                    parent_key="/library/metadata/32170",
                    grandparent_key="/library/metadata/32132",
                    title="The Noise That Blue Makes",
                    grandparent_title="Taskmaster",
                    type="episode",
                    thumb="/library/metadata/32171/thumb/-1",
                    parent_thumb="/library/metadata/32170/thumb/1654134301",
                    grandparent_thumb="/library/metadata/32132/thumb/1703933346",
                    grandparent_art="/library/metadata/32132/art/1703933346",
                    index=1,
                    parent_index=13,
                    originally_available_at=dateutil.parser.parse(
                        "2022-04-14T00:00:00Z"
                    ).date(),
                    viewed_at=1654139223,
                    account_id=1,
                    device_id=5,
                ),
            ],
        ),
    )


def test_sessions_get_transcode_sessions():
    s = PlexAPI(
        access_token="<YOUR_API_KEY_HERE>",
    )

    assert s is not None

    res = s.sessions.get_transcode_sessions()
    assert res.status_code == 200
    assert res.object is not None
    assert res.object == operations.GetTranscodeSessionsResponseBody(
        media_container=operations.GetTranscodeSessionsMediaContainer(
            size=1,
            transcode_session=[
                operations.TranscodeSession(
                    key="vv3i2q2lax92qlzul1hbd4bx",
                    throttled=False,
                    complete=False,
                    progress=1.7999999523162842,
                    size=-22,
                    speed=25.100000381469727,
                    error=False,
                    duration=1445695,
                    remaining=53,
                    context="streaming",
                    source_video_codec="h264",
                    source_audio_codec="aac",
                    video_decision="transcode",
                    audio_decision="transcode",
                    subtitle_decision="burn",
                    protocol="http",
                    container="mkv",
                    video_codec="h264",
                    audio_codec="opus",
                    audio_channels=1,
                    transcode_hw_requested=True,
                    time_stamp=1705895805.4919229,
                    max_offset_available=29.53,
                    min_offset_available=3.003000020980835,
                ),
            ],
        ),
    )


def test_sessions_stop_transcode_session():
    s = PlexAPI(
        access_token="<YOUR_API_KEY_HERE>",
    )

    assert s is not None

    res = s.sessions.stop_transcode_session(session_key="zz7llzqlx8w9vnrsbnwhbmep")
    assert res.status_code == 204