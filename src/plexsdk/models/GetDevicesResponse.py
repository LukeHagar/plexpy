from .base import BaseModel
from typing import List


class MediaContainerDevice(BaseModel):
    def __init__(
        self,
        id: float = None,
        name: str = None,
        platform: str = None,
        clientIdentifier: str = None,
        createdAt: float = None,
        **kwargs,
    ):
        """
        Initialize MediaContainerDevice
        Parameters:
        ----------
            id: float
            name: str
            platform: str
            clientIdentifier: str
            createdAt: float
        """
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if platform is not None:
            self.platform = platform
        if clientIdentifier is not None:
            self.clientIdentifier = clientIdentifier
        if createdAt is not None:
            self.createdAt = createdAt


class MediaContainer(BaseModel):
    def __init__(
        self,
        size: float = None,
        identifier: str = None,
        Device: List[MediaContainerDevice] = None,
        **kwargs,
    ):
        """
        Initialize MediaContainer
        Parameters:
        ----------
            size: float
            identifier: str
            Device: list of MediaContainerDevice
        """
        if size is not None:
            self.size = size
        if identifier is not None:
            self.identifier = identifier
        if Device is not None:
            self.Device = Device


class GetDevicesResponse(BaseModel):
    def __init__(self, MediaContainer: MediaContainer = None, **kwargs):
        """
        Initialize GetDevicesResponse
        Parameters:
        ----------
            MediaContainer: MediaContainer
        """
        if MediaContainer is not None:
            self.MediaContainer = MediaContainer
