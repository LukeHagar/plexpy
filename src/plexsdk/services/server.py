from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.GetServerCapabilitiesResponse import (
    GetServerCapabilitiesResponse as GetServerCapabilitiesResponseModel,
)
from ..models.GetAvailableClientsResponse import (
    GetAvailableClientsResponse as GetAvailableClientsResponseModel,
)
from ..models.GetAvailableClientsResponse import (
    GetAvailableClientsResponseItem as GetAvailableClientsResponseItemModel,
)
from ..models.GetDevicesResponse import GetDevicesResponse as GetDevicesResponseModel
from ..models.GetServerIdentityResponse import (
    GetServerIdentityResponse as GetServerIdentityResponseModel,
)
from ..models.GetMyPlexAccountResponse import (
    GetMyPlexAccountResponse as GetMyPlexAccountResponseModel,
)
from ..models.MinSize import MinSize as MinSizeModel
from ..models.Upscale import Upscale as UpscaleModel
from ..models.GetServerListResponse import (
    GetServerListResponse as GetServerListResponseModel,
)


class Server(BaseService):
    def get_server_capabilities(self) -> GetServerCapabilitiesResponseModel:
        """
        Server Capabilities
        """

        url_endpoint = "/"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetServerCapabilitiesResponseModel(**res)
        return res

    def get_server_preferences(self):
        """
        Get Server Preferences
        """

        url_endpoint = "/:/prefs"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        return res

    def get_available_clients(self) -> GetAvailableClientsResponseModel:
        """
        Get Available Clients
        """

        url_endpoint = "/clients"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, list):
            return [GetAvailableClientsResponseItemModel(**model) for model in res]
        return res

    def get_devices(self) -> GetDevicesResponseModel:
        """
        Get Devices
        """

        url_endpoint = "/devices"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetDevicesResponseModel(**res)
        return res

    def get_server_identity(self) -> GetServerIdentityResponseModel:
        """
        Get Server Identity
        """

        url_endpoint = "/identity"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetServerIdentityResponseModel(**res)
        return res

    def get_my_plex_account(self) -> GetMyPlexAccountResponseModel:
        """
        Get MyPlex Account
        """

        url_endpoint = "/myplex/account"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetMyPlexAccountResponseModel(**res)
        return res

    def get_resized_photo(
        self,
        url: str,
        upscale: UpscaleModel,
        min_size: MinSizeModel,
        blur: float,
        opacity: int,
        height: float,
        width: float,
    ):
        """
        Get a Resized Photo
        Parameters:
        ----------
            width: float
                The width for the resized photo
            height: float
                The height for the resized photo
            opacity: int
                The opacity for the resized photo
            blur: float
                The width for the resized photo
            min_size: MinSize
                images are always scaled proportionally. A value of '1' in minSize will make the smaller native dimension the dimension resized against.
            upscale: Upscale
                allow images to be resized beyond native dimensions.
            url: str
                path to image within Plex
        """

        url_endpoint = "/photo/:/transcode"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not width:
            raise ValueError("Parameter width is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "width", width)
        )
        if not height:
            raise ValueError("Parameter height is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "height", height)
        )
        if not opacity:
            raise ValueError("Parameter opacity is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "opacity", opacity)
        )
        if not blur:
            raise ValueError("Parameter blur is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "blur", blur)
        )
        if not min_size:
            raise ValueError(
                "Parameter min_size is required, cannot be empty or blank."
            )
        validated_min_size = self._enum_matching(
            min_size, MinSizeModel.list(), "min_size"
        )
        query_params.append(
            query_serializer.serialize_query(
                "form", False, "minSize", validated_min_size
            )
        )
        if not upscale:
            raise ValueError("Parameter upscale is required, cannot be empty or blank.")
        validated_upscale = self._enum_matching(upscale, UpscaleModel.list(), "upscale")
        query_params.append(
            query_serializer.serialize_query(
                "form", False, "upscale", validated_upscale
            )
        )
        if not url:
            raise ValueError("Parameter url is required, cannot be empty or blank.")
        query_params.append(query_serializer.serialize_query("form", False, "url", url))
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        return res

    def get_server_list(self) -> GetServerListResponseModel:
        """
        Get Server List
        """

        url_endpoint = "/servers"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetServerListResponseModel(**res)
        return res
