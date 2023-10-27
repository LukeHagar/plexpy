from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.State import State as StateModel


class Video(BaseService):
    def start_universal_transcode(
        self,
        protocol: str,
        part_index: float,
        media_index: float,
        path: str,
        has_mde: float,
        fast_seek: float = None,
        direct_play: float = None,
        direct_stream: float = None,
        subtitle_size: float = None,
        subtites: str = None,
        audio_boost: float = None,
        location: str = None,
        media_buffer_size: float = None,
        session: str = None,
        add_debug_overlay: float = None,
        auto_adjust_quality: float = None,
    ):
        """
        Start Universal Transcode
        Parameters:
        ----------
            has_mde: float
                Whether the media item has MDE
            path: str
                The path to the media item to transcode
            media_index: float
                The index of the media item to transcode
            part_index: float
                The index of the part to transcode
            protocol: str
                The protocol to use for the transcode session
            fast_seek: float
                Whether to use fast seek or not
            direct_play: float
                Whether to use direct play or not
            direct_stream: float
                Whether to use direct stream or not
            subtitle_size: float
                The size of the subtitles
            subtites: str
                The subtitles
            audio_boost: float
                The audio boost
            location: str
                The location of the transcode session
            media_buffer_size: float
                The size of the media buffer
            session: str
                The session ID
            add_debug_overlay: float
                Whether to add a debug overlay or not
            auto_adjust_quality: float
                Whether to auto adjust quality or not
        """

        url_endpoint = "/video/:/transcode/universal/start.mpd"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not has_mde:
            raise ValueError("Parameter has_mde is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "hasMDE", has_mde)
        )
        if not path:
            raise ValueError("Parameter path is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "path", path)
        )
        if not media_index:
            raise ValueError(
                "Parameter media_index is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query("form", False, "mediaIndex", media_index)
        )
        if not part_index:
            raise ValueError(
                "Parameter part_index is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query("form", False, "partIndex", part_index)
        )
        if not protocol:
            raise ValueError(
                "Parameter protocol is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query("form", False, "protocol", protocol)
        )
        if fast_seek:
            query_params.append(
                query_serializer.serialize_query("form", False, "fastSeek", fast_seek)
            )
        if direct_play:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "directPlay", direct_play
                )
            )
        if direct_stream:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "directStream", direct_stream
                )
            )
        if subtitle_size:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "subtitleSize", subtitle_size
                )
            )
        if subtites:
            query_params.append(
                query_serializer.serialize_query("form", False, "subtites", subtites)
            )
        if audio_boost:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "audioBoost", audio_boost
                )
            )
        if location:
            query_params.append(
                query_serializer.serialize_query("form", False, "location", location)
            )
        if media_buffer_size:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "mediaBufferSize", media_buffer_size
                )
            )
        if session:
            query_params.append(
                query_serializer.serialize_query("form", False, "session", session)
            )
        if add_debug_overlay:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "addDebugOverlay", add_debug_overlay
                )
            )
        if auto_adjust_quality:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "autoAdjustQuality", auto_adjust_quality
                )
            )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        return res

    def get_timeline(
        self,
        row: float,
        play_back_time: float,
        play_queue_item_id: float,
        context: str,
        duration: float,
        time: float,
        has_mde: float,
        state: StateModel,
        key: str,
        rating_key: float,
    ):
        """
        Get the timeline for a media item
        Parameters:
        ----------
            rating_key: float
                The rating key of the media item
            key: str
                The key of the media item to get the timeline for
            state: State
                The state of the media item
            has_mde: float
                Whether the media item has MDE
            time: float
                The time of the media item
            duration: float
                The duration of the media item
            context: str
                The context of the media item
            play_queue_item_id: float
                The play queue item ID of the media item
            play_back_time: float
                The playback time of the media item
            row: float
                The row of the media item
        """

        url_endpoint = "/:/timeline"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not rating_key:
            raise ValueError(
                "Parameter rating_key is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query("form", False, "ratingKey", rating_key)
        )
        if not key:
            raise ValueError("Parameter key is required, cannot be empty or blank.")
        query_params.append(query_serializer.serialize_query("form", False, "key", key))
        if not state:
            raise ValueError("Parameter state is required, cannot be empty or blank.")
        validated_state = self._enum_matching(state, StateModel.list(), "state")
        query_params.append(
            query_serializer.serialize_query("form", False, "state", validated_state)
        )
        if not has_mde:
            raise ValueError("Parameter has_mde is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "hasMDE", has_mde)
        )
        if not time:
            raise ValueError("Parameter time is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "time", time)
        )
        if not duration:
            raise ValueError(
                "Parameter duration is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query("form", False, "duration", duration)
        )
        if not context:
            raise ValueError("Parameter context is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "context", context)
        )
        if not play_queue_item_id:
            raise ValueError(
                "Parameter play_queue_item_id is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query(
                "form", False, "playQueueItemID", play_queue_item_id
            )
        )
        if not play_back_time:
            raise ValueError(
                "Parameter play_back_time is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query(
                "form", False, "playBackTime", play_back_time
            )
        )
        if not row:
            raise ValueError("Parameter row is required, cannot be empty or blank.")
        query_params.append(query_serializer.serialize_query("form", False, "row", row))
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        return res
