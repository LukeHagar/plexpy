from .base import BaseModel
from typing import List


class ButlerTasksButlerTask(BaseModel):
    def __init__(
        self,
        name: str = None,
        interval: float = None,
        scheduleRandomized: bool = None,
        enabled: bool = None,
        title: str = None,
        description: str = None,
        **kwargs,
    ):
        """
        Initialize ButlerTasksButlerTask
        Parameters:
        ----------
            name: str
            interval: float
            scheduleRandomized: bool
            enabled: bool
            title: str
            description: str
        """
        if name is not None:
            self.name = name
        if interval is not None:
            self.interval = interval
        if scheduleRandomized is not None:
            self.scheduleRandomized = scheduleRandomized
        if enabled is not None:
            self.enabled = enabled
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description


class ButlerTasks(BaseModel):
    def __init__(self, ButlerTask: List[ButlerTasksButlerTask] = None, **kwargs):
        """
        Initialize ButlerTasks
        Parameters:
        ----------
            ButlerTask: list of ButlerTasksButlerTask
        """
        if ButlerTask is not None:
            self.ButlerTask = ButlerTask


class GetButlerTasksResponse(BaseModel):
    def __init__(self, ButlerTasks: ButlerTasks = None, **kwargs):
        """
        Initialize GetButlerTasksResponse
        Parameters:
        ----------
            ButlerTasks: ButlerTasks
        """
        if ButlerTasks is not None:
            self.ButlerTasks = ButlerTasks
