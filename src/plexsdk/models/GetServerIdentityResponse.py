from .base import BaseModel


class MediaContainer(BaseModel):
    def __init__(
        self,
        size: float = None,
        claimed: bool = None,
        machineIdentifier: str = None,
        version: str = None,
        **kwargs,
    ):
        """
        Initialize MediaContainer
        Parameters:
        ----------
            size: float
            claimed: bool
            machineIdentifier: str
            version: str
        """
        if size is not None:
            self.size = size
        if claimed is not None:
            self.claimed = claimed
        if machineIdentifier is not None:
            self.machineIdentifier = machineIdentifier
        if version is not None:
            self.version = version


class GetServerIdentityResponse(BaseModel):
    def __init__(self, MediaContainer: MediaContainer = None, **kwargs):
        """
        Initialize GetServerIdentityResponse
        Parameters:
        ----------
            MediaContainer: MediaContainer
        """
        if MediaContainer is not None:
            self.MediaContainer = MediaContainer
