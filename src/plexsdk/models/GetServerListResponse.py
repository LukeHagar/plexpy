from .base import BaseModel
from typing import List


class MediaContainerServer(BaseModel):
    def __init__(
        self,
        name: str = None,
        host: str = None,
        address: str = None,
        port: float = None,
        machineIdentifier: str = None,
        version: str = None,
        **kwargs,
    ):
        """
        Initialize MediaContainerServer
        Parameters:
        ----------
            name: str
            host: str
            address: str
            port: float
            machineIdentifier: str
            version: str
        """
        if name is not None:
            self.name = name
        if host is not None:
            self.host = host
        if address is not None:
            self.address = address
        if port is not None:
            self.port = port
        if machineIdentifier is not None:
            self.machineIdentifier = machineIdentifier
        if version is not None:
            self.version = version


class MediaContainer(BaseModel):
    def __init__(
        self, size: float = None, Server: List[MediaContainerServer] = None, **kwargs
    ):
        """
        Initialize MediaContainer
        Parameters:
        ----------
            size: float
            Server: list of MediaContainerServer
        """
        if size is not None:
            self.size = size
        if Server is not None:
            self.Server = Server


class GetServerListResponse(BaseModel):
    def __init__(self, MediaContainer: MediaContainer = None, **kwargs):
        """
        Initialize GetServerListResponse
        Parameters:
        ----------
            MediaContainer: MediaContainer
        """
        if MediaContainer is not None:
            self.MediaContainer = MediaContainer
