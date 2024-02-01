"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .activities import Activities
from .butler import Butler
from .hubs import Hubs
from .library import Library
from .log import Log
from .media import Media
from .playlists import Playlists
from .plex import Plex
from .sdkconfiguration import SDKConfiguration, ServerProtocol
from .search import Search
from .security import Security
from .server import Server
from .sessions import Sessions
from .updater import Updater
from .video import Video
from plex_api import utils
from plex_api.models import components
from typing import Callable, Dict, Union

class PlexAPI:
    r"""Plex-API: A Plex Media Server API Map
    An Open API Spec for interacting with Plex.tv and Plex Servers
    """
    server: Server
    r"""Operations against the Plex Media Server System."""
    media: Media
    r"""API Calls interacting with Plex Media Server Media"""
    activities: Activities
    r"""Activities are awesome. They provide a way to monitor and control asynchronous operations on the server. In order to receive real-time updates for activities, a client would normally subscribe via either EventSource or Websocket endpoints.
    Activities are associated with HTTP replies via a special `X-Plex-Activity` header which contains the UUID of the activity.
    Activities are optional cancellable. If cancellable, they may be cancelled via the `DELETE` endpoint. Other details:
    - They can contain a `progress` (from 0 to 100) marking the percent completion of the activity.
    - They must contain an `type` which is used by clients to distinguish the specific activity.
    - They may contain a `Context` object with attributes which associate the activity with various specific entities (items, libraries, etc.)
    - The may contain a `Response` object which attributes which represent the result of the asynchronous operation.
    """
    butler: Butler
    r"""Butler is the task manager of the Plex Media Server Ecosystem."""
    hubs: Hubs
    r"""Hubs are a structured two-dimensional container for media, generally represented by multiple horizontal rows."""
    search: Search
    r"""API Calls that perform search operations with Plex Media Server"""
    library: Library
    r"""API Calls interacting with Plex Media Server Libraries"""
    log: Log
    r"""Submit logs to the Log Handler for Plex Media Server"""
    plex: Plex
    playlists: Playlists
    r"""Playlists are ordered collections of media. They can be dumb (just a list of media) or smart (based on a media query, such as \\"all albums from 2017\\").
    They can be organized in (optionally nesting) folders.
    Retrieving a playlist, or its items, will trigger a refresh of its metadata. 
    This may cause the duration and number of items to change.
    """
    security: Security
    r"""API Calls against Security for Plex Media Server"""
    sessions: Sessions
    r"""API Calls that perform search operations with Plex Media Server Sessions"""
    updater: Updater
    r"""This describes the API for searching and applying updates to the Plex Media Server.
    Updates to the status can be observed via the Event API.
    """
    video: Video
    r"""API Calls that perform operations with Plex Media Server Videos"""

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 access_token: Union[str, Callable[[], str]],
                 protocol: ServerProtocol = None,
                 ip: str = None,
                 port: str = None,
                 server_idx: int = None,
                 server_url: str = None,
                 url_params: Dict[str, str] = None,
                 client: requests_http.Session = None,
                 retry_config: utils.RetryConfig = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param access_token: The access_token required for authentication
        :type access_token: Union[str, Callable[[], str]]
        :param protocol: Allows setting the protocol variable for url substitution
        :type protocol: ServerProtocolmodels.ServerProtocol
        :param ip: Allows setting the ip variable for url substitution
        :type ip: 
        :param port: Allows setting the port variable for url substitution
        :type port: 
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: utils.RetryConfig
        """
        if client is None:
            client = requests_http.Session()
        
        if callable(access_token):
            def security():
                return components.Security(access_token = access_token())
        else:
            security = components.Security(access_token = access_token)
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)
        server_defaults = [
            {
                'protocol': protocol or 'http',
                'ip': ip or '10.10.10.47',
                'port': port or '32400',
            },
        ]

        self.sdk_configuration = SDKConfiguration(client, security, server_url, server_idx, server_defaults, retry_config=retry_config)
       
        self._init_sdks()
    
    def _init_sdks(self):
        self.server = Server(self.sdk_configuration)
        self.media = Media(self.sdk_configuration)
        self.activities = Activities(self.sdk_configuration)
        self.butler = Butler(self.sdk_configuration)
        self.hubs = Hubs(self.sdk_configuration)
        self.search = Search(self.sdk_configuration)
        self.library = Library(self.sdk_configuration)
        self.log = Log(self.sdk_configuration)
        self.plex = Plex(self.sdk_configuration)
        self.playlists = Playlists(self.sdk_configuration)
        self.security = Security(self.sdk_configuration)
        self.sessions = Sessions(self.sdk_configuration)
        self.updater = Updater(self.sdk_configuration)
        self.video = Video(self.sdk_configuration)
    