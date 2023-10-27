from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.GetSearchResultsResponse import (
    GetSearchResultsResponse as GetSearchResultsResponseModel,
)


class Search(BaseService):
    def perform_search(self, query: str, section_id: float = None, limit: float = None):
        """
        Perform a search
        Parameters:
        ----------
            query: str
                The query term
            section_id: float
                This gives context to the search, and can result in re-ordering of search result hubs
            limit: float
                The number of items to return per hub
        """

        url_endpoint = "/hubs/search"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not query:
            raise ValueError("Parameter query is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "query", query)
        )
        if section_id:
            query_params.append(
                query_serializer.serialize_query("form", False, "sectionId", section_id)
            )
        if limit:
            query_params.append(
                query_serializer.serialize_query("form", False, "limit", limit)
            )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        return res

    def perform_voice_search(
        self, query: str, section_id: float = None, limit: float = None
    ):
        """
        Perform a voice search
        Parameters:
        ----------
            query: str
                The query term
            section_id: float
                This gives context to the search, and can result in re-ordering of search result hubs
            limit: float
                The number of items to return per hub
        """

        url_endpoint = "/hubs/search/voice"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not query:
            raise ValueError("Parameter query is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "query", query)
        )
        if section_id:
            query_params.append(
                query_serializer.serialize_query("form", False, "sectionId", section_id)
            )
        if limit:
            query_params.append(
                query_serializer.serialize_query("form", False, "limit", limit)
            )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        return res

    def get_search_results(self, query: str) -> GetSearchResultsResponseModel:
        """
        Get Search Results
        Parameters:
        ----------
            query: str
                The search query string to use
        """

        url_endpoint = "/search"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not query:
            raise ValueError("Parameter query is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "query", query)
        )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetSearchResultsResponseModel(**res)
        return res
