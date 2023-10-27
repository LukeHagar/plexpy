from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.SecurityType import SecurityType as SecurityTypeModel
from ..models.Scope import Scope as ScopeModel


class Security(BaseService):
    def get_transient_token(self, scope: ScopeModel, type_: SecurityTypeModel):
        """
        Get a Transient Token.
        Parameters:
        ----------
            type: SecurityType
                `delegation` - This is the only supported `type` parameter.
            scope: Scope
                `all` - This is the only supported `scope` parameter.
        """

        url_endpoint = "/security/token"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not type_:
            raise ValueError("Parameter type_ is required, cannot be empty or blank.")
        validated_type_ = self._enum_matching(type_, SecurityTypeModel.list(), "type_")
        query_params.append(
            query_serializer.serialize_query("form", False, "type_", validated_type_)
        )
        if not scope:
            raise ValueError("Parameter scope is required, cannot be empty or blank.")
        validated_scope = self._enum_matching(scope, ScopeModel.list(), "scope")
        query_params.append(
            query_serializer.serialize_query("form", False, "scope", validated_scope)
        )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        return res

    def get_source_connection_information(self, source: str):
        """
        Get Source Connection Information
        Parameters:
        ----------
            source: str
                The source identifier with an included prefix.
        """

        url_endpoint = "/security/resources"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not source:
            raise ValueError("Parameter source is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "source", source)
        )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        return res
