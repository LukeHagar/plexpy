from .base import BaseModel
from typing import List


class MediaContainerTranscodeSession(BaseModel):
    def __init__(
        self,
        key: str = None,
        throttled: bool = None,
        complete: bool = None,
        progress: float = None,
        size: float = None,
        speed: float = None,
        error: bool = None,
        duration: float = None,
        context: str = None,
        sourceVideoCodec: str = None,
        sourceAudioCodec: str = None,
        videoDecision: str = None,
        audioDecision: str = None,
        protocol: str = None,
        container: str = None,
        videoCodec: str = None,
        audioCodec: str = None,
        audioChannels: float = None,
        transcodeHwRequested: bool = None,
        timeStamp: float = None,
        maxOffsetAvailable: float = None,
        minOffsetAvailable: float = None,
        **kwargs,
    ):
        """
        Initialize MediaContainerTranscodeSession
        Parameters:
        ----------
            key: str
            throttled: bool
            complete: bool
            progress: float
            size: float
            speed: float
            error: bool
            duration: float
            context: str
            sourceVideoCodec: str
            sourceAudioCodec: str
            videoDecision: str
            audioDecision: str
            protocol: str
            container: str
            videoCodec: str
            audioCodec: str
            audioChannels: float
            transcodeHwRequested: bool
            timeStamp: float
            maxOffsetAvailable: float
            minOffsetAvailable: float
        """
        if key is not None:
            self.key = key
        if throttled is not None:
            self.throttled = throttled
        if complete is not None:
            self.complete = complete
        if progress is not None:
            self.progress = progress
        if size is not None:
            self.size = size
        if speed is not None:
            self.speed = speed
        if error is not None:
            self.error = error
        if duration is not None:
            self.duration = duration
        if context is not None:
            self.context = context
        if sourceVideoCodec is not None:
            self.sourceVideoCodec = sourceVideoCodec
        if sourceAudioCodec is not None:
            self.sourceAudioCodec = sourceAudioCodec
        if videoDecision is not None:
            self.videoDecision = videoDecision
        if audioDecision is not None:
            self.audioDecision = audioDecision
        if protocol is not None:
            self.protocol = protocol
        if container is not None:
            self.container = container
        if videoCodec is not None:
            self.videoCodec = videoCodec
        if audioCodec is not None:
            self.audioCodec = audioCodec
        if audioChannels is not None:
            self.audioChannels = audioChannels
        if transcodeHwRequested is not None:
            self.transcodeHwRequested = transcodeHwRequested
        if timeStamp is not None:
            self.timeStamp = timeStamp
        if maxOffsetAvailable is not None:
            self.maxOffsetAvailable = maxOffsetAvailable
        if minOffsetAvailable is not None:
            self.minOffsetAvailable = minOffsetAvailable


class MediaContainer(BaseModel):
    def __init__(
        self,
        size: float = None,
        TranscodeSession: List[MediaContainerTranscodeSession] = None,
        **kwargs,
    ):
        """
        Initialize MediaContainer
        Parameters:
        ----------
            size: float
            TranscodeSession: list of MediaContainerTranscodeSession
        """
        if size is not None:
            self.size = size
        if TranscodeSession is not None:
            self.TranscodeSession = TranscodeSession


class GetTranscodeSessionsResponse(BaseModel):
    def __init__(self, MediaContainer: MediaContainer = None, **kwargs):
        """
        Initialize GetTranscodeSessionsResponse
        Parameters:
        ----------
            MediaContainer: MediaContainer
        """
        if MediaContainer is not None:
            self.MediaContainer = MediaContainer
