"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

import dateutil.parser
from plex_api_client import PlexAPI
from plex_api_client.models import operations


def test_hubs_get_global_hubs():
    s = PlexAPI(
        access_token="<YOUR_API_KEY_HERE>",
    )

    assert s is not None

    res = s.hubs.get_global_hubs()
    assert res.status_code == 200
    assert res.object is not None
    assert res.object == operations.GetGlobalHubsResponseBody(
        media_container=operations.GetGlobalHubsMediaContainer(
            size=8,
            allow_sync=True,
            identifier="com.plexapp.plugins.library",
            hub=[
                operations.Hub(
                    hub_key="/library/metadata/50768,65523,58188,57341,57302,57070",
                    key="/playlists/all?type=15&sort=lastViewedAt:desc&playlistType=video,audio",
                    title="Recent Playlists",
                    type="playlist",
                    hub_identifier="home.playlists",
                    context="hub.home.playlists",
                    size=6,
                    more=True,
                    style="shelf",
                    promoted=True,
                    metadata=[
                        operations.GetGlobalHubsMetadata(
                            rating_key="57070",
                            key="/playlists/57070/items",
                            guid="com.plexapp.agents.none://9fee6c5b-3143-4923-813e-57bd0190056c",
                            type="playlist",
                            title="November Movie Day",
                            title_sort="Tracks",
                            summary="",
                            smart=False,
                            playlist_type="video",
                            composite="/playlists/57070/composite/1668787730",
                            icon="playlist://image.smart",
                            view_count=2,
                            last_viewed_at=1668787732,
                            duration=16873000,
                            leaf_count=3,
                            added_at=1668779618,
                            updated_at=1668787730,
                        ),
                    ],
                ),
            ],
        ),
    )


def test_hubs_get_recently_added():
    s = PlexAPI(
        access_token="<YOUR_API_KEY_HERE>",
    )

    assert s is not None

    res = s.hubs.get_recently_added(
        request={
            "content_directory_id": 470161,
            "section_id": 2,
            "type": operations.Type.TV_SHOW,
            "include_meta": operations.IncludeMeta.ENABLE,
            "x_plex_container_start": 0,
            "x_plex_container_size": 50,
        }
    )
    assert res.status_code == 200
    assert res.object is not None
    assert res.object == operations.GetRecentlyAddedResponseBody(
        media_container=operations.GetRecentlyAddedMediaContainer(
            size=50,
            identifier="com.plexapp.plugins.library",
            meta=operations.Meta(
                type=[
                    operations.GetRecentlyAddedType(
                        key="/library/sections/2/all?type=2",
                        type="show",
                        title="TV Shows",
                        active=False,
                        filter_=[
                            operations.GetRecentlyAddedFilter(
                                filter_="genre",
                                filter_type="string",
                                key="/library/sections/2/genre?type=2",
                                title="Genre",
                                type="filter",
                            ),
                            operations.GetRecentlyAddedFilter(
                                filter_="genre",
                                filter_type="string",
                                key="/library/sections/2/genre?type=2",
                                title="Genre",
                                type="filter",
                            ),
                            operations.GetRecentlyAddedFilter(
                                filter_="genre",
                                filter_type="string",
                                key="/library/sections/2/genre?type=2",
                                title="Genre",
                                type="filter",
                            ),
                        ],
                        sort=[
                            operations.GetRecentlyAddedSort(
                                default="asc",
                                active=False,
                                active_direction=operations.GetRecentlyAddedActiveDirection.ASCENDING,
                                default_direction=operations.GetRecentlyAddedDefaultDirection.ASCENDING,
                                desc_key="titleSort:desc",
                                first_character_key="/library/sections/2/firstCharacter",
                                key="titleSort",
                                title="Title",
                            ),
                        ],
                        field=[
                            operations.GetRecentlyAddedField(
                                key="show.title",
                                title="Show Title",
                                type="string",
                                sub_type="rating",
                            ),
                            operations.GetRecentlyAddedField(
                                key="show.title",
                                title="Show Title",
                                type="string",
                                sub_type="rating",
                            ),
                            operations.GetRecentlyAddedField(
                                key="show.title",
                                title="Show Title",
                                type="string",
                                sub_type="rating",
                            ),
                        ],
                    ),
                    operations.GetRecentlyAddedType(
                        key="/library/sections/2/all?type=2",
                        type="show",
                        title="TV Shows",
                        active=False,
                        filter_=[
                            operations.GetRecentlyAddedFilter(
                                filter_="genre",
                                filter_type="string",
                                key="/library/sections/2/genre?type=2",
                                title="Genre",
                                type="filter",
                            ),
                            operations.GetRecentlyAddedFilter(
                                filter_="genre",
                                filter_type="string",
                                key="/library/sections/2/genre?type=2",
                                title="Genre",
                                type="filter",
                            ),
                            operations.GetRecentlyAddedFilter(
                                filter_="genre",
                                filter_type="string",
                                key="/library/sections/2/genre?type=2",
                                title="Genre",
                                type="filter",
                            ),
                        ],
                        sort=[
                            operations.GetRecentlyAddedSort(
                                default="asc",
                                active=False,
                                active_direction=operations.GetRecentlyAddedActiveDirection.ASCENDING,
                                default_direction=operations.GetRecentlyAddedDefaultDirection.ASCENDING,
                                desc_key="titleSort:desc",
                                first_character_key="/library/sections/2/firstCharacter",
                                key="titleSort",
                                title="Title",
                            ),
                            operations.GetRecentlyAddedSort(
                                default="asc",
                                active=False,
                                active_direction=operations.GetRecentlyAddedActiveDirection.ASCENDING,
                                default_direction=operations.GetRecentlyAddedDefaultDirection.ASCENDING,
                                desc_key="titleSort:desc",
                                first_character_key="/library/sections/2/firstCharacter",
                                key="titleSort",
                                title="Title",
                            ),
                            operations.GetRecentlyAddedSort(
                                default="asc",
                                active=False,
                                active_direction=operations.GetRecentlyAddedActiveDirection.ASCENDING,
                                default_direction=operations.GetRecentlyAddedDefaultDirection.ASCENDING,
                                desc_key="titleSort:desc",
                                first_character_key="/library/sections/2/firstCharacter",
                                key="titleSort",
                                title="Title",
                            ),
                        ],
                        field=[
                            operations.GetRecentlyAddedField(
                                key="show.title",
                                title="Show Title",
                                type="string",
                                sub_type="rating",
                            ),
                            operations.GetRecentlyAddedField(
                                key="show.title",
                                title="Show Title",
                                type="string",
                                sub_type="rating",
                            ),
                            operations.GetRecentlyAddedField(
                                key="show.title",
                                title="Show Title",
                                type="string",
                                sub_type="rating",
                            ),
                        ],
                    ),
                    operations.GetRecentlyAddedType(
                        key="/library/sections/2/all?type=2",
                        type="show",
                        title="TV Shows",
                        active=False,
                        filter_=[
                            operations.GetRecentlyAddedFilter(
                                filter_="genre",
                                filter_type="string",
                                key="/library/sections/2/genre?type=2",
                                title="Genre",
                                type="filter",
                            ),
                            operations.GetRecentlyAddedFilter(
                                filter_="genre",
                                filter_type="string",
                                key="/library/sections/2/genre?type=2",
                                title="Genre",
                                type="filter",
                            ),
                            operations.GetRecentlyAddedFilter(
                                filter_="genre",
                                filter_type="string",
                                key="/library/sections/2/genre?type=2",
                                title="Genre",
                                type="filter",
                            ),
                        ],
                        sort=[
                            operations.GetRecentlyAddedSort(
                                default="asc",
                                active=False,
                                active_direction=operations.GetRecentlyAddedActiveDirection.ASCENDING,
                                default_direction=operations.GetRecentlyAddedDefaultDirection.ASCENDING,
                                desc_key="titleSort:desc",
                                first_character_key="/library/sections/2/firstCharacter",
                                key="titleSort",
                                title="Title",
                            ),
                            operations.GetRecentlyAddedSort(
                                default="asc",
                                active=False,
                                active_direction=operations.GetRecentlyAddedActiveDirection.ASCENDING,
                                default_direction=operations.GetRecentlyAddedDefaultDirection.ASCENDING,
                                desc_key="titleSort:desc",
                                first_character_key="/library/sections/2/firstCharacter",
                                key="titleSort",
                                title="Title",
                            ),
                        ],
                        field=[
                            operations.GetRecentlyAddedField(
                                key="show.title",
                                title="Show Title",
                                type="string",
                                sub_type="rating",
                            ),
                            operations.GetRecentlyAddedField(
                                key="show.title",
                                title="Show Title",
                                type="string",
                                sub_type="rating",
                            ),
                            operations.GetRecentlyAddedField(
                                key="show.title",
                                title="Show Title",
                                type="string",
                                sub_type="rating",
                            ),
                        ],
                    ),
                ],
                field_type=[
                    operations.GetRecentlyAddedFieldType(
                        type="tag",
                        operator=[
                            operations.GetRecentlyAddedOperator(
                                key="=",
                                title="is",
                            ),
                        ],
                    ),
                    operations.GetRecentlyAddedFieldType(
                        type="tag",
                        operator=[
                            operations.GetRecentlyAddedOperator(
                                key="=",
                                title="is",
                            ),
                        ],
                    ),
                    operations.GetRecentlyAddedFieldType(
                        type="tag",
                        operator=[
                            operations.GetRecentlyAddedOperator(
                                key="=",
                                title="is",
                            ),
                        ],
                    ),
                ],
            ),
            metadata=[
                operations.GetRecentlyAddedMetadata(
                    rating_key="58683",
                    key="/library/metadata/58683",
                    guid="plex://movie/5d7768ba96b655001fdc0408",
                    studio="20th Century Studios",
                    skip_children=False,
                    library_section_id=1,
                    library_section_title="Movies",
                    library_section_key="/library/sections/1",
                    type=operations.GetRecentlyAddedHubsType.MOVIE,
                    title="Avatar: The Way of Water",
                    slug="4-for-texas",
                    content_rating="PG-13",
                    summary="Jake Sully lives with his newfound family formed on the extrasolar moon Pandora. Once a familiar threat returns to finish what was previously started, Jake must work with Neytiri and the army of the Na'vi race to protect their home.",
                    rating=7.6,
                    audience_rating=9.2,
                    year=2022,
                    season_count=2022,
                    tagline="Return to Pandora.",
                    flatten_seasons=operations.FlattenSeasons.TRUE,
                    show_ordering=operations.ShowOrdering.DVD,
                    thumb="/library/metadata/58683/thumb/1703239236",
                    art="/library/metadata/58683/art/1703239236",
                    banner="/library/metadata/58683/banner/1703239236",
                    duration=11558112,
                    originally_available_at=dateutil.parser.parse(
                        "2022-12-14T00:00:00Z"
                    ).date(),
                    added_at=1556281940,
                    updated_at=1556281940,
                    audience_rating_image="rottentomatoes://image.rating.upright",
                    chapter_source="media",
                    primary_extra_key="/library/metadata/58684",
                    rating_image="rottentomatoes://image.rating.ripe",
                    grandparent_rating_key="66",
                    grandparent_guid="plex://show/5d9c081b170e24001f2a7be4",
                    grandparent_key="/library/metadata/66",
                    grandparent_title="Caprica",
                    grandparent_thumb="/library/metadata/66/thumb/1705716261",
                    parent_slug="alice-in-borderland-2020",
                    grandparent_slug="alice-in-borderland-2020",
                    grandparent_art="/library/metadata/66/art/1705716261",
                    grandparent_theme="/library/metadata/66/theme/1705716261",
                    media=[
                        operations.Media(
                            id=119534,
                            duration=11558112,
                            bitrate=25025,
                            width=3840,
                            height=2072,
                            aspect_ratio=1.85,
                            audio_profile="dts",
                            audio_channels=6,
                            audio_codec="eac3",
                            video_codec="hevc",
                            video_resolution="4k",
                            container="mkv",
                            video_frame_rate="24p",
                            video_profile="main 10",
                            has_voice_activity=False,
                            optimized_for_streaming=operations.OptimizedForStreaming.ENABLE,
                            has64bit_offsets=False,
                            part=[
                                operations.Part(
                                    id=119542,
                                    key="/library/parts/119542/1680457526/file.mkv",
                                    duration=11558112,
                                    file="/movies/Avatar The Way of Water (2022)/Avatar.The.Way.of.Water.2022.2160p.WEB-DL.DDP5.1.Atmos.DV.HDR10.HEVC-CMRG.mkv",
                                    size=36158371307,
                                    container="mkv",
                                    audio_profile="dts",
                                    has64bit_offsets=False,
                                    optimized_for_streaming=False,
                                    video_profile="main 10",
                                    indexes="sd",
                                    has_thumbnail=operations.HasThumbnail.TRUE,
                                    stream=[
                                        operations.Stream(
                                            id=272796,
                                            stream_type=1,
                                            default=True,
                                            selected=True,
                                            codec="h264",
                                            index=0,
                                            bitrate=6273,
                                            color_primaries="bt709",
                                            color_range="tv",
                                            color_space="bt709",
                                            color_trc="bt709",
                                            bit_depth=8,
                                            chroma_location="left",
                                            stream_identifier="2",
                                            chroma_subsampling="4:2:0",
                                            coded_height=1088,
                                            coded_width=1920,
                                            frame_rate=29.97,
                                            has_scaling_matrix=False,
                                            hearing_impaired=False,
                                            closed_captions=False,
                                            embedded_in_video="1",
                                            height=1080,
                                            level=40,
                                            profile="main",
                                            ref_frames=4,
                                            scan_type="progressive",
                                            width=1920,
                                            display_title="1080p (H.264)",
                                            extended_display_title="1080p (H.264)",
                                            channels=2,
                                            language="English",
                                            language_tag="en",
                                            language_code="eng",
                                            audio_channel_layout="stereo",
                                            sampling_rate=48000,
                                            title="English",
                                            can_auto_sync=False,
                                        ),
                                    ],
                                ),
                                operations.Part(
                                    id=119542,
                                    key="/library/parts/119542/1680457526/file.mkv",
                                    duration=11558112,
                                    file="/movies/Avatar The Way of Water (2022)/Avatar.The.Way.of.Water.2022.2160p.WEB-DL.DDP5.1.Atmos.DV.HDR10.HEVC-CMRG.mkv",
                                    size=36158371307,
                                    container="mkv",
                                    audio_profile="dts",
                                    has64bit_offsets=False,
                                    optimized_for_streaming=False,
                                    video_profile="main 10",
                                    indexes="sd",
                                    has_thumbnail=operations.HasThumbnail.TRUE,
                                    stream=[
                                        operations.Stream(
                                            id=272796,
                                            stream_type=1,
                                            default=True,
                                            selected=True,
                                            codec="h264",
                                            index=0,
                                            bitrate=6273,
                                            color_primaries="bt709",
                                            color_range="tv",
                                            color_space="bt709",
                                            color_trc="bt709",
                                            bit_depth=8,
                                            chroma_location="left",
                                            stream_identifier="2",
                                            chroma_subsampling="4:2:0",
                                            coded_height=1088,
                                            coded_width=1920,
                                            frame_rate=29.97,
                                            has_scaling_matrix=False,
                                            hearing_impaired=False,
                                            closed_captions=False,
                                            embedded_in_video="1",
                                            height=1080,
                                            level=40,
                                            profile="main",
                                            ref_frames=4,
                                            scan_type="progressive",
                                            width=1920,
                                            display_title="1080p (H.264)",
                                            extended_display_title="1080p (H.264)",
                                            channels=2,
                                            language="English",
                                            language_tag="en",
                                            language_code="eng",
                                            audio_channel_layout="stereo",
                                            sampling_rate=48000,
                                            title="English",
                                            can_auto_sync=False,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                    genre=[
                        operations.Genre(
                            tag="Adventure",
                        ),
                    ],
                    country=[
                        operations.Country(
                            tag="United States of America",
                        ),
                    ],
                    director=[
                        operations.Director(
                            tag="James Cameron",
                        ),
                        operations.Director(
                            tag="James Cameron",
                        ),
                    ],
                    writer=[
                        operations.Writer(
                            tag="James Cameron",
                        ),
                    ],
                    collection=[
                        operations.Collection(
                            tag="Working NL Subs",
                        ),
                    ],
                    role=[
                        operations.Role(
                            id=294129,
                            filter_="actor=294129",
                            thumb="https://metadata-static.plex.tv/2/people/27b85844536c39f3f9ac943aaad46608.jpg",
                            tag="Mike Smith",
                            tag_key="668e7e7b22bcad9064350c91",
                            role="Self",
                        ),
                        operations.Role(
                            id=294129,
                            filter_="actor=294129",
                            thumb="https://metadata-static.plex.tv/2/people/27b85844536c39f3f9ac943aaad46608.jpg",
                            tag="Mike Smith",
                            tag_key="668e7e7b22bcad9064350c91",
                            role="Self",
                        ),
                        operations.Role(
                            id=294129,
                            filter_="actor=294129",
                            thumb="https://metadata-static.plex.tv/2/people/27b85844536c39f3f9ac943aaad46608.jpg",
                            tag="Mike Smith",
                            tag_key="668e7e7b22bcad9064350c91",
                            role="Self",
                        ),
                    ],
                    media_guid=[
                        operations.MediaGUID(
                            id="imdb://tt13015952",
                        ),
                        operations.MediaGUID(
                            id="imdb://tt13015952",
                        ),
                        operations.MediaGUID(
                            id="imdb://tt13015952",
                        ),
                    ],
                    ultra_blur_colors=operations.UltraBlurColors(
                        top_left="11333b",
                        top_right="0a232d",
                        bottom_right="73958",
                        bottom_left="1f5066",
                    ),
                    meta_data_rating=[
                        operations.MetaDataRating(
                            image="themoviedb://image.rating",
                            value=3,
                            type="audience",
                        ),
                    ],
                    image=[
                        operations.GetRecentlyAddedImage(
                            alt="Episode 1",
                            type=operations.GetRecentlyAddedHubsResponseType.BACKGROUND,
                            url="/library/metadata/45521/thumb/1644710589",
                        ),
                        operations.GetRecentlyAddedImage(
                            alt="Episode 1",
                            type=operations.GetRecentlyAddedHubsResponseType.BACKGROUND,
                            url="/library/metadata/45521/thumb/1644710589",
                        ),
                        operations.GetRecentlyAddedImage(
                            alt="Episode 1",
                            type=operations.GetRecentlyAddedHubsResponseType.BACKGROUND,
                            url="/library/metadata/45521/thumb/1644710589",
                        ),
                    ],
                    title_sort="Whale",
                    view_count=1,
                    last_viewed_at=1682752242,
                    original_title="映画 ブラッククローバー 魔法帝の剣",
                    view_offset=5222500,
                    skip_count=1,
                    index=1,
                    theme="/library/metadata/1/theme/1705636920",
                    leaf_count=14,
                    viewed_leaf_count=0,
                    child_count=1,
                    has_premium_extras="1",
                    has_premium_primary_extra="1",
                    parent_rating_key="66",
                    parent_guid="plex://show/5d9c081b170e24001f2a7be4",
                    parent_studio="UCP",
                    parent_key="/library/metadata/66",
                    parent_title="Caprica",
                    parent_index=1,
                    parent_year=2010,
                    parent_thumb="/library/metadata/66/thumb/1705716261",
                    parent_theme="/library/metadata/66/theme/1705716261",
                ),
            ],
        ),
    )


def test_hubs_get_library_hubs():
    s = PlexAPI(
        access_token="<YOUR_API_KEY_HERE>",
    )

    assert s is not None

    res = s.hubs.get_library_hubs(section_id=6728.76)
    assert res.status_code == 200
    assert res.object is not None
    assert res.object == operations.GetLibraryHubsResponseBody(
        media_container=operations.GetLibraryHubsMediaContainer(
            size=7,
            allow_sync=True,
            identifier="com.plexapp.plugins.library",
            library_section_id=1,
            library_section_title="Movies",
            library_section_uuid="322a231a-b7f7-49f5-920f-14c61199cd30",
            hub=[
                operations.GetLibraryHubsHub(
                    key="/library/sections/1/all?sort=lastViewedAt:desc&unwatched=0&viewOffset=0",
                    title="Recently Played Movies",
                    type="movie",
                    hub_identifier="movie.recentlyviewed.1",
                    context="hub.movie.recentlyviewed",
                    size=6,
                    more=True,
                    style="shelf",
                    hub_key="/library/metadata/66485,66098,57249,11449,5858,14944",
                    metadata=[
                        operations.GetLibraryHubsMetadata(
                            rating_key="14944",
                            key="/library/metadata/14944",
                            guid="plex://movie/5d77686eeb5d26001f1eb339",
                            studio="Walt Disney Animation Studios",
                            type="movie",
                            title="Tangled",
                            library_section_title="Movies",
                            library_section_id=1,
                            library_section_key="/library/sections/1",
                            content_rating="PG",
                            summary="The magically long-haired Rapunzel has spent her entire life in a tower, but now that a runaway thief has stumbled upon her, she is about to discover the world for the first time, and who she really is.",
                            rating=8.9,
                            audience_rating=8.7,
                            view_count=1,
                            last_viewed_at=1704936047,
                            year=2010,
                            tagline="They're taking adventure to new lengths.",
                            thumb="/library/metadata/14944/thumb/1705739847",
                            art="/library/metadata/14944/art/1705739847",
                            duration=6017237,
                            originally_available_at=dateutil.parser.parse(
                                "2010-11-24T00:00:00Z"
                            ).date(),
                            added_at=1589412494,
                            updated_at=1705739847,
                            audience_rating_image="rottentomatoes://image.rating.upright",
                            primary_extra_key="/library/metadata/14952",
                            rating_image="rottentomatoes://image.rating.ripe",
                            media=[
                                operations.GetLibraryHubsMedia(
                                    id=38247,
                                    duration=6017237,
                                    bitrate=2051,
                                    width=1920,
                                    height=1080,
                                    aspect_ratio=1.78,
                                    audio_channels=2,
                                    audio_codec="aac",
                                    video_codec="h264",
                                    video_resolution="1080",
                                    container="mp4",
                                    video_frame_rate="24p",
                                    optimized_for_streaming=1,
                                    audio_profile="lc",
                                    has64bit_offsets=False,
                                    video_profile="high",
                                    part=[
                                        operations.GetLibraryHubsPart(
                                            id=38247,
                                            key="/library/parts/38247/1589412494/file.mp4",
                                            duration=6017237,
                                            file="/movies/Tangled (2010)/Tangled (2010) Bluray-1080p.mp4",
                                            size=1545647447,
                                            audio_profile="lc",
                                            container="mp4",
                                            has64bit_offsets=False,
                                            optimized_for_streaming=True,
                                            video_profile="high",
                                        ),
                                    ],
                                ),
                            ],
                            genre=[
                                operations.GetLibraryHubsGenre(
                                    tag="Animation",
                                ),
                            ],
                            country=[
                                operations.GetLibraryHubsCountry(
                                    tag="United States of America",
                                ),
                            ],
                            director=[
                                operations.GetLibraryHubsDirector(
                                    tag="Nathan Greno",
                                ),
                            ],
                            role=[
                                operations.GetLibraryHubsRole(
                                    tag="Donna Murphy",
                                ),
                            ],
                            writer=[
                                operations.GetLibraryHubsWriter(
                                    tag="Wilhelm Grimm",
                                ),
                            ],
                            skip_count=1,
                            chapter_source="media",
                        ),
                    ],
                    promoted=True,
                    random=True,
                ),
            ],
        ),
    )
