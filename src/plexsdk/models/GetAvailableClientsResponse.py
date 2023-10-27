from .base import BaseModel
from typing import List


class MediaContainer(BaseModel):
    def __init__(self, size: float = None, Server: list = None, **kwargs):
        """
        Initialize MediaContainer
        Parameters:
        ----------
            size: float
            Server: list of dict
        """
        if size is not None:
            self.size = size
        if Server is not None:
            self.Server = Server


class GetAvailableClientsResponseItem(BaseModel):
    def __init__(self, MediaContainer: MediaContainer = None, **kwargs):
        """
        Initialize GetAvailableClientsResponseItem
        Parameters:
        ----------
            MediaContainer: MediaContainer
        """
        if MediaContainer is not None:
            self.MediaContainer = MediaContainer


GetAvailableClientsResponse = List[GetAvailableClientsResponseItem]
