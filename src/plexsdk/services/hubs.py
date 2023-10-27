from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.OnlyTransient import OnlyTransient as OnlyTransientModel


class Hubs(BaseService):
    def get_global_hubs(
        self, count: float = None, only_transient: OnlyTransientModel = None
    ):
        """
        Get Global Hubs
        Parameters:
        ----------
            count: float
                The number of items to return with each hub.
            only_transient: OnlyTransient
                Only return hubs which are "transient", meaning those which are prone to changing after media playback or addition (e.g. On Deck, or Recently Added).
        """

        url_endpoint = "/hubs"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if count:
            query_params.append(
                query_serializer.serialize_query("form", False, "count", count)
            )
        if only_transient:
            validated_only_transient = self._enum_matching(
                only_transient, OnlyTransientModel.list(), "only_transient"
            )
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "onlyTransient", validated_only_transient
                )
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        return res

    def get_library_hubs(
        self,
        section_id: float,
        count: float = None,
        only_transient: OnlyTransientModel = None,
    ):
        """
        Get library specific hubs
        Parameters:
        ----------
            section_id: float
                the Id of the library to query
            count: float
                The number of items to return with each hub.
            only_transient: OnlyTransient
                Only return hubs which are "transient", meaning those which are prone to changing after media playback or addition (e.g. On Deck, or Recently Added).
        """

        url_endpoint = "/hubs/sections/{section_id}"
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
        if count:
            query_params.append(
                query_serializer.serialize_query("form", False, "count", count)
            )
        if only_transient:
            validated_only_transient = self._enum_matching(
                only_transient, OnlyTransientModel.list(), "only_transient"
            )
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "onlyTransient", validated_only_transient
                )
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        return res
