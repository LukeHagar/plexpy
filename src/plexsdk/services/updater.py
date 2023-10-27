from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.Download import Download as DownloadModel
from ..models.Tonight import Tonight as TonightModel
from ..models.Skip import Skip as SkipModel


class Updater(BaseService):
    def get_update_status(self):
        """
        Querying status of updates
        """

        url_endpoint = "/updater/status"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        return res

    def check_for_updates(self, download: DownloadModel = None):
        """
        Checking for updates
        Parameters:
        ----------
            download: Download
                Indicate that you want to start download any updates found.
        """

        url_endpoint = "/updater/check"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if download:
            validated_download = self._enum_matching(
                download, DownloadModel.list(), "download"
            )
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "download", validated_download
                )
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.put(final_url, headers, {}, True)
        return res

    def apply_updates(self, tonight: TonightModel = None, skip: SkipModel = None):
        """
        Apply Updates
        Parameters:
        ----------
            tonight: Tonight
                Indicate that you want the update to run during the next Butler execution. Omitting this or setting it to false indicates that the update should install
            skip: Skip
                Indicate that the latest version should be marked as skipped. The <Release> entry for this version will have the `state` set to `skipped`.
        """

        url_endpoint = "/updater/apply"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if tonight:
            validated_tonight = self._enum_matching(
                tonight, TonightModel.list(), "tonight"
            )
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "tonight", validated_tonight
                )
            )
        if skip:
            validated_skip = self._enum_matching(skip, SkipModel.list(), "skip")
            query_params.append(
                query_serializer.serialize_query("form", False, "skip", validated_skip)
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.put(final_url, headers, {}, True)
        return res
