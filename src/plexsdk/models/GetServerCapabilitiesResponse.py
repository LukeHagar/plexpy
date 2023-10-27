from .base import BaseModel
from typing import List


class MediaContainerDirectory(BaseModel):
    def __init__(
        self, count: float = None, key: str = None, title: str = None, **kwargs
    ):
        """
        Initialize MediaContainerDirectory
        Parameters:
        ----------
            count: float
            key: str
            title: str
        """
        if count is not None:
            self.count = count
        if key is not None:
            self.key = key
        if title is not None:
            self.title = title


class MediaContainer(BaseModel):
    def __init__(
        self,
        size: float = None,
        allowCameraUpload: bool = None,
        allowChannelAccess: bool = None,
        allowMediaDeletion: bool = None,
        allowSharing: bool = None,
        allowSync: bool = None,
        allowTuners: bool = None,
        backgroundProcessing: bool = None,
        certificate: bool = None,
        companionProxy: bool = None,
        countryCode: str = None,
        diagnostics: str = None,
        eventStream: bool = None,
        friendlyName: str = None,
        hubSearch: bool = None,
        itemClusters: bool = None,
        livetv: float = None,
        machineIdentifier: str = None,
        mediaProviders: bool = None,
        multiuser: bool = None,
        musicAnalysis: float = None,
        myPlex: bool = None,
        myPlexMappingState: str = None,
        myPlexSigninState: str = None,
        myPlexSubscription: bool = None,
        myPlexUsername: str = None,
        offlineTranscode: float = None,
        ownerFeatures: str = None,
        photoAutoTag: bool = None,
        platform: str = None,
        platformVersion: str = None,
        pluginHost: bool = None,
        pushNotifications: bool = None,
        readOnlyLibraries: bool = None,
        streamingBrainABRVersion: float = None,
        streamingBrainVersion: float = None,
        sync: bool = None,
        transcoderActiveVideoSessions: float = None,
        transcoderAudio: bool = None,
        transcoderLyrics: bool = None,
        transcoderPhoto: bool = None,
        transcoderSubtitles: bool = None,
        transcoderVideo: bool = None,
        transcoderVideoBitrates: str = None,
        transcoderVideoQualities: str = None,
        transcoderVideoResolutions: str = None,
        updatedAt: float = None,
        updater: bool = None,
        version: str = None,
        voiceSearch: bool = None,
        Directory: List[MediaContainerDirectory] = None,
        **kwargs,
    ):
        """
        Initialize MediaContainer
        Parameters:
        ----------
            size: float
            allowCameraUpload: bool
            allowChannelAccess: bool
            allowMediaDeletion: bool
            allowSharing: bool
            allowSync: bool
            allowTuners: bool
            backgroundProcessing: bool
            certificate: bool
            companionProxy: bool
            countryCode: str
            diagnostics: str
            eventStream: bool
            friendlyName: str
            hubSearch: bool
            itemClusters: bool
            livetv: float
            machineIdentifier: str
            mediaProviders: bool
            multiuser: bool
            musicAnalysis: float
            myPlex: bool
            myPlexMappingState: str
            myPlexSigninState: str
            myPlexSubscription: bool
            myPlexUsername: str
            offlineTranscode: float
            ownerFeatures: str
            photoAutoTag: bool
            platform: str
            platformVersion: str
            pluginHost: bool
            pushNotifications: bool
            readOnlyLibraries: bool
            streamingBrainABRVersion: float
            streamingBrainVersion: float
            sync: bool
            transcoderActiveVideoSessions: float
            transcoderAudio: bool
            transcoderLyrics: bool
            transcoderPhoto: bool
            transcoderSubtitles: bool
            transcoderVideo: bool
            transcoderVideoBitrates: str
            transcoderVideoQualities: str
            transcoderVideoResolutions: str
            updatedAt: float
            updater: bool
            version: str
            voiceSearch: bool
            Directory: list of MediaContainerDirectory
        """
        if size is not None:
            self.size = size
        if allowCameraUpload is not None:
            self.allowCameraUpload = allowCameraUpload
        if allowChannelAccess is not None:
            self.allowChannelAccess = allowChannelAccess
        if allowMediaDeletion is not None:
            self.allowMediaDeletion = allowMediaDeletion
        if allowSharing is not None:
            self.allowSharing = allowSharing
        if allowSync is not None:
            self.allowSync = allowSync
        if allowTuners is not None:
            self.allowTuners = allowTuners
        if backgroundProcessing is not None:
            self.backgroundProcessing = backgroundProcessing
        if certificate is not None:
            self.certificate = certificate
        if companionProxy is not None:
            self.companionProxy = companionProxy
        if countryCode is not None:
            self.countryCode = countryCode
        if diagnostics is not None:
            self.diagnostics = diagnostics
        if eventStream is not None:
            self.eventStream = eventStream
        if friendlyName is not None:
            self.friendlyName = friendlyName
        if hubSearch is not None:
            self.hubSearch = hubSearch
        if itemClusters is not None:
            self.itemClusters = itemClusters
        if livetv is not None:
            self.livetv = livetv
        if machineIdentifier is not None:
            self.machineIdentifier = machineIdentifier
        if mediaProviders is not None:
            self.mediaProviders = mediaProviders
        if multiuser is not None:
            self.multiuser = multiuser
        if musicAnalysis is not None:
            self.musicAnalysis = musicAnalysis
        if myPlex is not None:
            self.myPlex = myPlex
        if myPlexMappingState is not None:
            self.myPlexMappingState = myPlexMappingState
        if myPlexSigninState is not None:
            self.myPlexSigninState = myPlexSigninState
        if myPlexSubscription is not None:
            self.myPlexSubscription = myPlexSubscription
        if myPlexUsername is not None:
            self.myPlexUsername = myPlexUsername
        if offlineTranscode is not None:
            self.offlineTranscode = offlineTranscode
        if ownerFeatures is not None:
            self.ownerFeatures = ownerFeatures
        if photoAutoTag is not None:
            self.photoAutoTag = photoAutoTag
        if platform is not None:
            self.platform = platform
        if platformVersion is not None:
            self.platformVersion = platformVersion
        if pluginHost is not None:
            self.pluginHost = pluginHost
        if pushNotifications is not None:
            self.pushNotifications = pushNotifications
        if readOnlyLibraries is not None:
            self.readOnlyLibraries = readOnlyLibraries
        if streamingBrainABRVersion is not None:
            self.streamingBrainABRVersion = streamingBrainABRVersion
        if streamingBrainVersion is not None:
            self.streamingBrainVersion = streamingBrainVersion
        if sync is not None:
            self.sync = sync
        if transcoderActiveVideoSessions is not None:
            self.transcoderActiveVideoSessions = transcoderActiveVideoSessions
        if transcoderAudio is not None:
            self.transcoderAudio = transcoderAudio
        if transcoderLyrics is not None:
            self.transcoderLyrics = transcoderLyrics
        if transcoderPhoto is not None:
            self.transcoderPhoto = transcoderPhoto
        if transcoderSubtitles is not None:
            self.transcoderSubtitles = transcoderSubtitles
        if transcoderVideo is not None:
            self.transcoderVideo = transcoderVideo
        if transcoderVideoBitrates is not None:
            self.transcoderVideoBitrates = transcoderVideoBitrates
        if transcoderVideoQualities is not None:
            self.transcoderVideoQualities = transcoderVideoQualities
        if transcoderVideoResolutions is not None:
            self.transcoderVideoResolutions = transcoderVideoResolutions
        if updatedAt is not None:
            self.updatedAt = updatedAt
        if updater is not None:
            self.updater = updater
        if version is not None:
            self.version = version
        if voiceSearch is not None:
            self.voiceSearch = voiceSearch
        if Directory is not None:
            self.Directory = Directory


class GetServerCapabilitiesResponse(BaseModel):
    def __init__(self, MediaContainer: MediaContainer = None, **kwargs):
        """
        Initialize GetServerCapabilitiesResponse
        Parameters:
        ----------
            MediaContainer: MediaContainer
        """
        if MediaContainer is not None:
            self.MediaContainer = MediaContainer
