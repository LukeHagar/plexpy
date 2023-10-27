from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.GetRecentlyAddedResponse import (
    GetRecentlyAddedResponse as GetRecentlyAddedResponseModel,
)
from ..models.IncludeDetails import IncludeDetails as IncludeDetailsModel
from ..models.GetOnDeckResponse import GetOnDeckResponse as GetOnDeckResponseModel


class Library(BaseService):
    def get_file_hash(self, url: str, type_: float = None):
        """
        Get Hash Value
        Parameters:
        ----------
            url: str
                This is the path to the local file, must be prefixed by `file://`
            type: float
                Item type
        """

        url_endpoint = "/library/hashes"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not url:
            raise ValueError("Parameter url is required, cannot be empty or blank.")
        query_params.append(query_serializer.serialize_query("form", False, "url", url))
        if type_:
            query_params.append(
                query_serializer.serialize_query("form", False, "type_", type_)
            )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        return res

    def get_recently_added(self) -> GetRecentlyAddedResponseModel:
        """
        Get Recently Added
        """

        url_endpoint = "/library/recentlyAdded"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetRecentlyAddedResponseModel(**res)
        return res

    def get_libraries(self):
        """
        Get All Libraries
        """

        url_endpoint = "/library/sections"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        return res

    def get_library(
        self, section_id: float, include_details: IncludeDetailsModel = None
    ):
        """
        Get Library Details
        Parameters:
        ----------
            section_id: float
                the Id of the library to query
            include_details: IncludeDetails
                Whether or not to include details for a section (types, filters, and sorts).
        Only exists for backwards compatibility, media providers other than the server libraries have it on always.

        """

        url_endpoint = "/library/sections/{section_id}"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not section_id:
            raise ValueError(
                "Parameter section_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{section_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, section_id, None))
            ),
        )
        if include_details:
            validated_include_details = self._enum_matching(
                include_details, IncludeDetailsModel.list(), "include_details"
            )
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "includeDetails", validated_include_details
                )
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        return res

    def delete_library(self, section_id: float):
        """
        Delete Library Section
        Parameters:
        ----------
            section_id: float
                the Id of the library to query
        """

        url_endpoint = "/library/sections/{section_id}"
        headers = {}
        self._add_required_headers(headers)
        if not section_id:
            raise ValueError(
                "Parameter section_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{section_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, section_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        return res

    def get_library_items(
        self, section_id: float, type_: float = None, filter: str = None
    ):
        """
        Get Library Items
        Parameters:
        ----------
            section_id: float
                the Id of the library to query
            type: float
                item type
            filter: str
                the filter parameter
        """

        url_endpoint = "/library/sections/{section_id}/all"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not section_id:
            raise ValueError(
                "Parameter section_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{section_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, section_id, None))
            ),
        )
        if type_:
            query_params.append(
                query_serializer.serialize_query("form", False, "type_", type_)
            )
        if filter:
            query_params.append(
                query_serializer.serialize_query("form", False, "filter", filter)
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        return res

    def refresh_library(self, section_id: float):
        """
        Refresh Library
        Parameters:
        ----------
            section_id: float
                the Id of the library to refresh
        """

        url_endpoint = "/library/sections/{section_id}/refresh"
        headers = {}
        self._add_required_headers(headers)
        if not section_id:
            raise ValueError(
                "Parameter section_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{section_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, section_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        return res

    def get_latest_library_items(
        self, type_: float, section_id: float, filter: str = None
    ):
        """
        Get Latest Library Items
        Parameters:
        ----------
            section_id: float
                the Id of the library to query
            type: float
                item type
            filter: str
                the filter parameter
        """

        url_endpoint = "/library/sections/{section_id}/latest"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not section_id:
            raise ValueError(
                "Parameter section_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{section_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, section_id, None))
            ),
        )
        if not type_:
            raise ValueError("Parameter type_ is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "type_", type_)
        )
        if filter:
            query_params.append(
                query_serializer.serialize_query("form", False, "filter", filter)
            )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        return res

    def get_common_library_items(
        self, type_: float, section_id: float, filter: str = None
    ):
        """
        Get Common Library Items
        Parameters:
        ----------
            section_id: float
                the Id of the library to query
            type: float
                item type
            filter: str
                the filter parameter
        """

        url_endpoint = "/library/sections/{section_id}/common"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not section_id:
            raise ValueError(
                "Parameter section_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{section_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, section_id, None))
            ),
        )
        if not type_:
            raise ValueError("Parameter type_ is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "type_", type_)
        )
        if filter:
            query_params.append(
                query_serializer.serialize_query("form", False, "filter", filter)
            )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        return res

    def get_metadata(self, rating_key: float):
        """
        Get Items Metadata
        Parameters:
        ----------
            rating_key: float
                the id of the library item to return the children of.
        """

        url_endpoint = "/library/metadata/{rating_key}"
        headers = {}
        self._add_required_headers(headers)
        if not rating_key:
            raise ValueError(
                "Parameter rating_key is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{rating_key}",
            quote(
                str(query_serializer.serialize_path("simple", False, rating_key, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        return res

    def get_metadata_children(self, rating_key: float):
        """
        Get Items Children
        Parameters:
        ----------
            rating_key: float
                the id of the library item to return the children of.
        """

        url_endpoint = "/library/metadata/{rating_key}/children"
        headers = {}
        self._add_required_headers(headers)
        if not rating_key:
            raise ValueError(
                "Parameter rating_key is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{rating_key}",
            quote(
                str(query_serializer.serialize_path("simple", False, rating_key, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        return res

    def get_on_deck(self) -> GetOnDeckResponseModel:
        """
        Get On Deck
        """

        url_endpoint = "/library/onDeck"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetOnDeckResponseModel(**res)
        return res
