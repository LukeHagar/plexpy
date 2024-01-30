"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from plex_api import utils
from plex_api.models import errors, operations
from typing import Optional

class Library:
    r"""API Calls interacting with Plex Media Server Libraries"""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def get_file_hash(self, url: str, type: Optional[float] = None) -> operations.GetFileHashResponse:
        r"""Get Hash Value
        This resource returns hash values for local files
        """
        request = operations.GetFileHashRequest(
            url=url,
            type=type,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/library/hashes'
        headers = {}
        query_params = utils.get_query_params(operations.GetFileHashRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.GetFileHashResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass
        elif http_res.status_code == 400 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.GetFileHashResponseBody)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def get_recently_added(self) -> operations.GetRecentlyAddedResponse:
        r"""Get Recently Added
        This endpoint will return the recently added content.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/library/recentlyAdded'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.GetRecentlyAddedResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetRecentlyAddedResponseBody])
                res.object = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 400 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.GetRecentlyAddedResponseBody)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def get_libraries(self) -> operations.GetLibrariesResponse:
        r"""Get All Libraries
        A library section (commonly referred to as just a library) is a collection of media. 
        Libraries are typed, and depending on their type provide either a flat or a hierarchical view of the media. 
        For example, a music library has an artist > albums > tracks structure, whereas a movie library is flat.

        Libraries have features beyond just being a collection of media; for starters, they include information about supported types, filters and sorts. 
        This allows a client to provide a rich interface around the media (e.g. allow sorting movies by release year).
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/library/sections'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.GetLibrariesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetLibrariesResponseBody])
                res.object = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 400 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.GetLibrariesResponseBody)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def get_library(self, section_id: float, include_details: Optional[operations.IncludeDetails] = None) -> operations.GetLibraryResponse:
        r"""Get Library Details
        ## Library Details Endpoint

        This endpoint provides comprehensive details about the library, focusing on organizational aspects rather than the content itself.   

        The details include:

        ### Directories
        Organized into three categories:

        - **Primary Directories**: 
          - Used in some clients for quick access to media subsets (e.g., \"All\", \"On Deck\").
          - Most can be replicated via media queries.
          - Customizable by users.

        - **Secondary Directories**:
          - Marked with `secondary=\"1\"`.
          - Used in older clients for structured navigation.

        - **Special Directories**:
          - Includes a \"By Folder\" entry for filesystem-based browsing.
          - Contains an obsolete `search=\"1\"` entry for on-the-fly search dialog creation.

        ### Types
        Each type in the library comes with a set of filters and sorts, aiding in building dynamic media controls:

        - **Type Object Attributes**:
          - `key`: Endpoint for the media list of this type.
          - `type`: Metadata type (if standard Plex type).
          - `title`: Title for this content type (e.g., \"Movies\").

        - **Filter Objects**:
          - Subset of the media query language.
          - Attributes include `filter` (name), `filterType` (data type), `key` (endpoint for value range), and `title`.

        - **Sort Objects**:
          - Description of sort fields.
          - Attributes include `defaultDirection` (asc/desc), `descKey` and `key` (sort parameters), and `title`.

        > **Note**: Filters and sorts are optional; without them, no filtering controls are rendered.
        """
        request = operations.GetLibraryRequest(
            section_id=section_id,
            include_details=include_details,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetLibraryRequest, base_url, '/library/sections/{sectionId}', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetLibraryRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.GetLibraryResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetLibraryResponseBody])
                res.object = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 400 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.GetLibraryResponseBody)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def delete_library(self, section_id: float) -> operations.DeleteLibraryResponse:
        r"""Delete Library Section
        Delate a library using a specific section
        """
        request = operations.DeleteLibraryRequest(
            section_id=section_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteLibraryRequest, base_url, '/library/sections/{sectionId}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.DeleteLibraryResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass
        elif http_res.status_code == 400 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.DeleteLibraryResponseBody)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def get_library_items(self, section_id: int, tag: operations.Tag) -> operations.GetLibraryItemsResponse:
        r"""Get Library Items
        Fetches details from a specific section of the library identified by a section key and a tag. The tag parameter accepts the following values:
        - `all`: All items in the section.
        - `unwatched`: Items that have not been played.
        - `newest`: Items that are recently released.
        - `recentlyAdded`: Items that are recently added to the library.
        - `recentlyViewed`: Items that were recently viewed.
        - `onDeck`: Items to continue watching.
        - `collection`: Items categorized by collection.
        - `edition`: Items categorized by edition.
        - `genre`: Items categorized by genre.
        - `year`: Items categorized by year of release.
        - `decade`: Items categorized by decade.
        - `director`: Items categorized by director.
        - `actor`: Items categorized by starring actor.
        - `country`: Items categorized by country of origin.
        - `contentRating`: Items categorized by content rating.
        - `rating`: Items categorized by rating.
        - `resolution`: Items categorized by resolution.
        - `firstCharacter`: Items categorized by the first letter.
        - `folder`: Items categorized by folder.
        """
        request = operations.GetLibraryItemsRequest(
            section_id=section_id,
            tag=tag,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetLibraryItemsRequest, base_url, '/library/sections/{sectionId}/{tag}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.GetLibraryItemsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetLibraryItemsResponseBody])
                res.object = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def refresh_library(self, section_id: float) -> operations.RefreshLibraryResponse:
        r"""Refresh Library
        This endpoint Refreshes the library.
        """
        request = operations.RefreshLibraryRequest(
            section_id=section_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.RefreshLibraryRequest, base_url, '/library/sections/{sectionId}/refresh', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.RefreshLibraryResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass
        elif http_res.status_code == 400 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.RefreshLibraryResponseBody)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def search_library(self, section_id: int, type: operations.Type) -> operations.SearchLibraryResponse:
        r"""Search Library
        Search for content within a specific section of the library.

        ### Types
        Each type in the library comes with a set of filters and sorts, aiding in building dynamic media controls:

        - **Type Object Attributes**:
          - `type`: Metadata type (if standard Plex type).  
          - `title`: Title for this content type (e.g., \"Movies\").

        - **Filter Objects**:
          - Subset of the media query language.
          - Attributes include `filter` (name), `filterType` (data type), `key` (endpoint for value range), and `title`.

        - **Sort Objects**:
          - Description of sort fields.
          - Attributes include `defaultDirection` (asc/desc), `descKey` and `key` (sort parameters), and `title`.

        > **Note**: Filters and sorts are optional; without them, no filtering controls are rendered.
        """
        request = operations.SearchLibraryRequest(
            section_id=section_id,
            type=type,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.SearchLibraryRequest, base_url, '/library/sections/{sectionId}/search', request)
        headers = {}
        query_params = utils.get_query_params(operations.SearchLibraryRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.SearchLibraryResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.SearchLibraryResponseBody])
                res.object = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def get_metadata(self, rating_key: float) -> operations.GetMetadataResponse:
        r"""Get Items Metadata
        This endpoint will return the metadata of a library item specified with the ratingKey.
        """
        request = operations.GetMetadataRequest(
            rating_key=rating_key,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetMetadataRequest, base_url, '/library/metadata/{ratingKey}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.GetMetadataResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetMetadataResponseBody])
                res.object = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 400 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.GetMetadataResponseBody)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def get_metadata_children(self, rating_key: float) -> operations.GetMetadataChildrenResponse:
        r"""Get Items Children
        This endpoint will return the children of of a library item specified with the ratingKey.
        """
        request = operations.GetMetadataChildrenRequest(
            rating_key=rating_key,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetMetadataChildrenRequest, base_url, '/library/metadata/{ratingKey}/children', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.GetMetadataChildrenResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetMetadataChildrenResponseBody])
                res.object = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 400 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.GetMetadataChildrenResponseBody)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def get_on_deck(self) -> operations.GetOnDeckResponse:
        r"""Get On Deck
        This endpoint will return the on deck content.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/library/onDeck'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.GetOnDeckResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetOnDeckResponseBody])
                res.object = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 400 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.GetOnDeckResponseBody)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    