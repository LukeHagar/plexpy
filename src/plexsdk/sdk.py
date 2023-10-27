"""
Creates a PlexSDK class.
Generates the main SDK with all available queries as attributes.

Class:
    PlexSDK
"""
from .net.environment import Environment

from .services.activities import Activities
from .services.butler import Butler
from .services.hubs import Hubs
from .services.library import Library
from .services.log import Log
from .services.media import Media
from .services.playlists import Playlists
from .services.search import Search
from .services.security import Security
from .services.server import Server
from .services.sessions import Sessions
from .services.updater import Updater
from .services.video import Video


class PlexSDK:
    """
    A class representing the full PlexSDK SDK

    Attributes
    ----------
    activities : Activities
    butler : Butler
    hubs : Hubs
    library : Library
    log : Log
    media : Media
    playlists : Playlists
    search : Search
    security : Security
    server : Server
    sessions : Sessions
    updater : Updater
    video : Video

    Methods
    -------
    set_base_url(url: str)
        Sets the end URL
    set_api_key(api_key, api_key_header))
        Set the api key
    """

    def __init__(
        self, api_key="", api_key_header="X-Plex-Token", environment=Environment.DEFAULT
    ) -> None:
        """
        Initializes the PlexSDK SDK class.
        Parameters
        ----------
        environment: str
            The environment that the SDK is accessing
        api_key : str
            The api key
        api_key_header : str
            The API key header
        """
        self.activities = Activities(api_key, api_key_header)
        self.butler = Butler(api_key, api_key_header)
        self.hubs = Hubs(api_key, api_key_header)
        self.library = Library(api_key, api_key_header)
        self.log = Log(api_key, api_key_header)
        self.media = Media(api_key, api_key_header)
        self.playlists = Playlists(api_key, api_key_header)
        self.search = Search(api_key, api_key_header)
        self.security = Security(api_key, api_key_header)
        self.server = Server(api_key, api_key_header)
        self.sessions = Sessions(api_key, api_key_header)
        self.updater = Updater(api_key, api_key_header)
        self.video = Video(api_key, api_key_header)

        self.set_base_url(environment.value)

    def set_base_url(self, url: str) -> None:
        """
        Sets the end URL

        Parameters
        ----------
            url:
                The end URL
        """
        self.activities.set_base_url(url)
        self.butler.set_base_url(url)
        self.hubs.set_base_url(url)
        self.library.set_base_url(url)
        self.log.set_base_url(url)
        self.media.set_base_url(url)
        self.playlists.set_base_url(url)
        self.search.set_base_url(url)
        self.security.set_base_url(url)
        self.server.set_base_url(url)
        self.sessions.set_base_url(url)
        self.updater.set_base_url(url)
        self.video.set_base_url(url)

    def set_api_key(self, api_key: str, api_key_header: str = None) -> None:
        """
        Sets api key and api key header name

        Parameters
        ----------
        api_key: string
            API Key value
        api_key_header: string
            Name of API Key
        """
        self.activities.set_api_key(api_key, api_key_header)
        self.butler.set_api_key(api_key, api_key_header)
        self.hubs.set_api_key(api_key, api_key_header)
        self.library.set_api_key(api_key, api_key_header)
        self.log.set_api_key(api_key, api_key_header)
        self.media.set_api_key(api_key, api_key_header)
        self.playlists.set_api_key(api_key, api_key_header)
        self.search.set_api_key(api_key, api_key_header)
        self.security.set_api_key(api_key, api_key_header)
        self.server.set_api_key(api_key, api_key_header)
        self.sessions.set_api_key(api_key, api_key_header)
        self.updater.set_api_key(api_key, api_key_header)
        self.video.set_api_key(api_key, api_key_header)
