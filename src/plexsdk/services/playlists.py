from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.Type import Type as TypeModel
from ..models.Smart import Smart as SmartModel
from ..models.PlaylistType import PlaylistType as PlaylistTypeModel
from ..models.Force import Force as ForceModel


class Playlists(BaseService):
    def create_playlist(
        self,
        smart: SmartModel,
        type_: TypeModel,
        title: str,
        uri: str = None,
        play_queue_id: float = None,
    ):
        """
        Create a Playlist
        Parameters:
        ----------
            title: str
                name of the playlist
            type: Type
                type of playlist to create
            smart: Smart
                whether the playlist is smart or not
            uri: str
                the content URI for the playlist
            play_queue_id: float
                the play queue to copy to a playlist
        """

        url_endpoint = "/playlists"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not title:
            raise ValueError("Parameter title is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "title", title)
        )
        if not type_:
            raise ValueError("Parameter type_ is required, cannot be empty or blank.")
        validated_type_ = self._enum_matching(type_, TypeModel.list(), "type_")
        query_params.append(
            query_serializer.serialize_query("form", False, "type_", validated_type_)
        )
        if not smart:
            raise ValueError("Parameter smart is required, cannot be empty or blank.")
        validated_smart = self._enum_matching(smart, SmartModel.list(), "smart")
        query_params.append(
            query_serializer.serialize_query("form", False, "smart", validated_smart)
        )
        if uri:
            query_params.append(
                query_serializer.serialize_query("form", False, "uri", uri)
            )
        if play_queue_id:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "playQueueID", play_queue_id
                )
            )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.post(final_url, headers, {}, True)
        return res

    def get_playlists(
        self, playlist_type: PlaylistTypeModel = None, smart: SmartModel = None
    ):
        """
        Get All Playlists
        Parameters:
        ----------
            playlist_type: PlaylistType
                limit to a type of playlist.
            smart: Smart
                type of playlists to return (default is all).
        """

        url_endpoint = "/playlists/all"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if playlist_type:
            validated_playlist_type = self._enum_matching(
                playlist_type, PlaylistTypeModel.list(), "playlist_type"
            )
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "playlistType", validated_playlist_type
                )
            )
        if smart:
            validated_smart = self._enum_matching(smart, SmartModel.list(), "smart")
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "smart", validated_smart
                )
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        return res

    def get_playlist(self, playlist_id: float):
        """
        Retrieve Playlist
        Parameters:
        ----------
            playlist_id: float
                the ID of the playlist
        """

        url_endpoint = "/playlists/{playlist_id}"
        headers = {}
        self._add_required_headers(headers)
        if not playlist_id:
            raise ValueError(
                "Parameter playlist_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{playlist_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, playlist_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        return res

    def update_playlist(self, playlist_id: float):
        """
        Update a Playlist
        Parameters:
        ----------
            playlist_id: float
                the ID of the playlist
        """

        url_endpoint = "/playlists/{playlist_id}"
        headers = {}
        self._add_required_headers(headers)
        if not playlist_id:
            raise ValueError(
                "Parameter playlist_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{playlist_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, playlist_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.put(final_url, headers, {}, True)
        return res

    def delete_playlist(self, playlist_id: float):
        """
        Deletes a Playlist
        Parameters:
        ----------
            playlist_id: float
                the ID of the playlist
        """

        url_endpoint = "/playlists/{playlist_id}"
        headers = {}
        self._add_required_headers(headers)
        if not playlist_id:
            raise ValueError(
                "Parameter playlist_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{playlist_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, playlist_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        return res

    def get_playlist_contents(self, type_: float, playlist_id: float):
        """
        Retrieve Playlist Contents
        Parameters:
        ----------
            playlist_id: float
                the ID of the playlist
            type: float
                the metadata type of the item to return
        """

        url_endpoint = "/playlists/{playlist_id}/items"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not playlist_id:
            raise ValueError(
                "Parameter playlist_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{playlist_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, playlist_id, None))
            ),
        )
        if not type_:
            raise ValueError("Parameter type_ is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "type_", type_)
        )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        return res

    def add_playlist_contents(self, play_queue_id: float, uri: str, playlist_id: float):
        """
        Adding to a Playlist
        Parameters:
        ----------
            playlist_id: float
                the ID of the playlist
            uri: str
                the content URI for the playlist
            play_queue_id: float
                the play queue to add to a playlist
        """

        url_endpoint = "/playlists/{playlist_id}/items"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not playlist_id:
            raise ValueError(
                "Parameter playlist_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{playlist_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, playlist_id, None))
            ),
        )
        if not uri:
            raise ValueError("Parameter uri is required, cannot be empty or blank.")
        query_params.append(query_serializer.serialize_query("form", False, "uri", uri))
        if not play_queue_id:
            raise ValueError(
                "Parameter play_queue_id is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query(
                "form", False, "playQueueID", play_queue_id
            )
        )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.put(final_url, headers, {}, True)
        return res

    def clear_playlist_contents(self, playlist_id: float):
        """
        Delete Playlist Contents
        Parameters:
        ----------
            playlist_id: float
                the ID of the playlist
        """

        url_endpoint = "/playlists/{playlist_id}/items"
        headers = {}
        self._add_required_headers(headers)
        if not playlist_id:
            raise ValueError(
                "Parameter playlist_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{playlist_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, playlist_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        return res

    def upload_playlist(self, force: ForceModel, path: str):
        """
        Upload Playlist
        Parameters:
        ----------
            path: str
                absolute path to a directory on the server where m3u files are stored, or the absolute path to a playlist file on the server.
        If the `path` argument is a directory, that path will be scanned for playlist files to be processed.
        Each file in that directory creates a separate playlist, with a name based on the filename of the file that created it.
        The GUID of each playlist is based on the filename.
        If the `path` argument is a file, that file will be used to create a new playlist, with the name based on the filename of the file that created it.
        The GUID of each playlist is based on the filename.

            force: Force
                force overwriting of duplicate playlists. By default, a playlist file uploaded with the same path will overwrite the existing playlist.
        The `force` argument is used to disable overwriting. If the `force` argument is set to 0, a new playlist will be created suffixed with the date and time that the duplicate was uploaded.

        """

        url_endpoint = "/playlists/upload"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not path:
            raise ValueError("Parameter path is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "path", path)
        )
        if not force:
            raise ValueError("Parameter force is required, cannot be empty or blank.")
        validated_force = self._enum_matching(force, ForceModel.list(), "force")
        query_params.append(
            query_serializer.serialize_query("form", False, "force", validated_force)
        )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.post(final_url, headers, {}, True)
        return res
