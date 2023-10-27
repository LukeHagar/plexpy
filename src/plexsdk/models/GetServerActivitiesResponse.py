from .base import BaseModel
from typing import List


class Context(BaseModel):
    def __init__(self, librarySectionID: str = None, **kwargs):
        """
        Initialize Context
        Parameters:
        ----------
            librarySectionID: str
        """
        if librarySectionID is not None:
            self.librarySectionID = librarySectionID


class MediaContainerActivity(BaseModel):
    def __init__(
        self,
        uuid: str = None,
        cancellable: bool = None,
        userID: float = None,
        title: str = None,
        subtitle: str = None,
        progress: float = None,
        Context: Context = None,
        type_: str = None,
        **kwargs,
    ):
        """
        Initialize MediaContainerActivity
        Parameters:
        ----------
            uuid: str
            cancellable: bool
            userID: float
            title: str
            subtitle: str
            progress: float
            Context: Context
            type_: str
        """
        if uuid is not None:
            self.uuid = uuid
        if cancellable is not None:
            self.cancellable = cancellable
        if userID is not None:
            self.userID = userID
        if title is not None:
            self.title = title
        if subtitle is not None:
            self.subtitle = subtitle
        if progress is not None:
            self.progress = progress
        if Context is not None:
            self.Context = Context
        if type_ is not None:
            self.type_ = type_


class MediaContainer(BaseModel):
    def __init__(
        self,
        size: float = None,
        Activity: List[MediaContainerActivity] = None,
        **kwargs,
    ):
        """
        Initialize MediaContainer
        Parameters:
        ----------
            size: float
            Activity: list of MediaContainerActivity
        """
        if size is not None:
            self.size = size
        if Activity is not None:
            self.Activity = Activity


class GetServerActivitiesResponse(BaseModel):
    def __init__(self, MediaContainer: MediaContainer = None, **kwargs):
        """
        Initialize GetServerActivitiesResponse
        Parameters:
        ----------
            MediaContainer: MediaContainer
        """
        if MediaContainer is not None:
            self.MediaContainer = MediaContainer
