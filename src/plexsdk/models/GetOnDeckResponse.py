from .base import BaseModel
from typing import List


class MediaContainerMetadataMediaPartStream(BaseModel):
    def __init__(
        self,
        id: float = None,
        streamType: float = None,
        default: bool = None,
        codec: str = None,
        index: float = None,
        bitrate: float = None,
        language: str = None,
        languageTag: str = None,
        languageCode: str = None,
        bitDepth: float = None,
        chromaLocation: str = None,
        chromaSubsampling: str = None,
        codedHeight: float = None,
        codedWidth: float = None,
        colorRange: str = None,
        frameRate: float = None,
        height: float = None,
        level: float = None,
        profile: str = None,
        refFrames: float = None,
        width: float = None,
        displayTitle: str = None,
        extendedDisplayTitle: str = None,
        **kwargs,
    ):
        """
        Initialize MediaContainerMetadataMediaPartStream
        Parameters:
        ----------
            id: float
            streamType: float
            default: bool
            codec: str
            index: float
            bitrate: float
            language: str
            languageTag: str
            languageCode: str
            bitDepth: float
            chromaLocation: str
            chromaSubsampling: str
            codedHeight: float
            codedWidth: float
            colorRange: str
            frameRate: float
            height: float
            level: float
            profile: str
            refFrames: float
            width: float
            displayTitle: str
            extendedDisplayTitle: str
        """
        if id is not None:
            self.id = id
        if streamType is not None:
            self.streamType = streamType
        if default is not None:
            self.default = default
        if codec is not None:
            self.codec = codec
        if index is not None:
            self.index = index
        if bitrate is not None:
            self.bitrate = bitrate
        if language is not None:
            self.language = language
        if languageTag is not None:
            self.languageTag = languageTag
        if languageCode is not None:
            self.languageCode = languageCode
        if bitDepth is not None:
            self.bitDepth = bitDepth
        if chromaLocation is not None:
            self.chromaLocation = chromaLocation
        if chromaSubsampling is not None:
            self.chromaSubsampling = chromaSubsampling
        if codedHeight is not None:
            self.codedHeight = codedHeight
        if codedWidth is not None:
            self.codedWidth = codedWidth
        if colorRange is not None:
            self.colorRange = colorRange
        if frameRate is not None:
            self.frameRate = frameRate
        if height is not None:
            self.height = height
        if level is not None:
            self.level = level
        if profile is not None:
            self.profile = profile
        if refFrames is not None:
            self.refFrames = refFrames
        if width is not None:
            self.width = width
        if displayTitle is not None:
            self.displayTitle = displayTitle
        if extendedDisplayTitle is not None:
            self.extendedDisplayTitle = extendedDisplayTitle


class MediaContainerMetadataMediaPart(BaseModel):
    def __init__(
        self,
        id: float = None,
        key: str = None,
        duration: float = None,
        file: str = None,
        size: float = None,
        audioProfile: str = None,
        container: str = None,
        videoProfile: str = None,
        Stream: List[MediaContainerMetadataMediaPartStream] = None,
        **kwargs,
    ):
        """
        Initialize MediaContainerMetadataMediaPart
        Parameters:
        ----------
            id: float
            key: str
            duration: float
            file: str
            size: float
            audioProfile: str
            container: str
            videoProfile: str
            Stream: list of MediaContainerMetadataMediaPartStream
        """
        if id is not None:
            self.id = id
        if key is not None:
            self.key = key
        if duration is not None:
            self.duration = duration
        if file is not None:
            self.file = file
        if size is not None:
            self.size = size
        if audioProfile is not None:
            self.audioProfile = audioProfile
        if container is not None:
            self.container = container
        if videoProfile is not None:
            self.videoProfile = videoProfile
        if Stream is not None:
            self.Stream = Stream


class MediaContainerMetadataMedia(BaseModel):
    def __init__(
        self,
        id: float = None,
        duration: float = None,
        bitrate: float = None,
        width: float = None,
        height: float = None,
        aspectRatio: float = None,
        audioChannels: float = None,
        audioCodec: str = None,
        videoCodec: str = None,
        videoResolution: str = None,
        container: str = None,
        videoFrameRate: str = None,
        audioProfile: str = None,
        videoProfile: str = None,
        Part: List[MediaContainerMetadataMediaPart] = None,
        **kwargs,
    ):
        """
        Initialize MediaContainerMetadataMedia
        Parameters:
        ----------
            id: float
            duration: float
            bitrate: float
            width: float
            height: float
            aspectRatio: float
            audioChannels: float
            audioCodec: str
            videoCodec: str
            videoResolution: str
            container: str
            videoFrameRate: str
            audioProfile: str
            videoProfile: str
            Part: list of MediaContainerMetadataMediaPart
        """
        if id is not None:
            self.id = id
        if duration is not None:
            self.duration = duration
        if bitrate is not None:
            self.bitrate = bitrate
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if aspectRatio is not None:
            self.aspectRatio = aspectRatio
        if audioChannels is not None:
            self.audioChannels = audioChannels
        if audioCodec is not None:
            self.audioCodec = audioCodec
        if videoCodec is not None:
            self.videoCodec = videoCodec
        if videoResolution is not None:
            self.videoResolution = videoResolution
        if container is not None:
            self.container = container
        if videoFrameRate is not None:
            self.videoFrameRate = videoFrameRate
        if audioProfile is not None:
            self.audioProfile = audioProfile
        if videoProfile is not None:
            self.videoProfile = videoProfile
        if Part is not None:
            self.Part = Part


class MediaContainerMetadataGuid(BaseModel):
    def __init__(self, id: str = None, **kwargs):
        """
        Initialize MediaContainerMetadataGuid
        Parameters:
        ----------
            id: str
        """
        if id is not None:
            self.id = id


class MediaContainerMetadata(BaseModel):
    def __init__(
        self,
        allowSync: bool = None,
        librarySectionID: float = None,
        librarySectionTitle: str = None,
        librarySectionUUID: str = None,
        ratingKey: float = None,
        key: str = None,
        parentRatingKey: float = None,
        grandparentRatingKey: float = None,
        guid: str = None,
        parentGuid: str = None,
        grandparentGuid: str = None,
        title: str = None,
        grandparentKey: str = None,
        parentKey: str = None,
        librarySectionKey: str = None,
        grandparentTitle: str = None,
        parentTitle: str = None,
        contentRating: str = None,
        summary: str = None,
        index: float = None,
        parentIndex: float = None,
        lastViewedAt: float = None,
        year: float = None,
        thumb: str = None,
        art: str = None,
        parentThumb: str = None,
        grandparentThumb: str = None,
        grandparentArt: str = None,
        grandparentTheme: str = None,
        duration: float = None,
        originallyAvailableAt: str = None,
        addedAt: float = None,
        updatedAt: float = None,
        Media: List[MediaContainerMetadataMedia] = None,
        Guid: List[MediaContainerMetadataGuid] = None,
        type_: str = None,
        **kwargs,
    ):
        """
        Initialize MediaContainerMetadata
        Parameters:
        ----------
            allowSync: bool
            librarySectionID: float
            librarySectionTitle: str
            librarySectionUUID: str
            ratingKey: float
            key: str
            parentRatingKey: float
            grandparentRatingKey: float
            guid: str
            parentGuid: str
            grandparentGuid: str
            title: str
            grandparentKey: str
            parentKey: str
            librarySectionKey: str
            grandparentTitle: str
            parentTitle: str
            contentRating: str
            summary: str
            index: float
            parentIndex: float
            lastViewedAt: float
            year: float
            thumb: str
            art: str
            parentThumb: str
            grandparentThumb: str
            grandparentArt: str
            grandparentTheme: str
            duration: float
            originallyAvailableAt: str
            addedAt: float
            updatedAt: float
            Media: list of MediaContainerMetadataMedia
            Guid: list of MediaContainerMetadataGuid
            type_: str
        """
        if allowSync is not None:
            self.allowSync = allowSync
        if librarySectionID is not None:
            self.librarySectionID = librarySectionID
        if librarySectionTitle is not None:
            self.librarySectionTitle = librarySectionTitle
        if librarySectionUUID is not None:
            self.librarySectionUUID = librarySectionUUID
        if ratingKey is not None:
            self.ratingKey = ratingKey
        if key is not None:
            self.key = key
        if parentRatingKey is not None:
            self.parentRatingKey = parentRatingKey
        if grandparentRatingKey is not None:
            self.grandparentRatingKey = grandparentRatingKey
        if guid is not None:
            self.guid = guid
        if parentGuid is not None:
            self.parentGuid = parentGuid
        if grandparentGuid is not None:
            self.grandparentGuid = grandparentGuid
        if title is not None:
            self.title = title
        if grandparentKey is not None:
            self.grandparentKey = grandparentKey
        if parentKey is not None:
            self.parentKey = parentKey
        if librarySectionKey is not None:
            self.librarySectionKey = librarySectionKey
        if grandparentTitle is not None:
            self.grandparentTitle = grandparentTitle
        if parentTitle is not None:
            self.parentTitle = parentTitle
        if contentRating is not None:
            self.contentRating = contentRating
        if summary is not None:
            self.summary = summary
        if index is not None:
            self.index = index
        if parentIndex is not None:
            self.parentIndex = parentIndex
        if lastViewedAt is not None:
            self.lastViewedAt = lastViewedAt
        if year is not None:
            self.year = year
        if thumb is not None:
            self.thumb = thumb
        if art is not None:
            self.art = art
        if parentThumb is not None:
            self.parentThumb = parentThumb
        if grandparentThumb is not None:
            self.grandparentThumb = grandparentThumb
        if grandparentArt is not None:
            self.grandparentArt = grandparentArt
        if grandparentTheme is not None:
            self.grandparentTheme = grandparentTheme
        if duration is not None:
            self.duration = duration
        if originallyAvailableAt is not None:
            self.originallyAvailableAt = originallyAvailableAt
        if addedAt is not None:
            self.addedAt = addedAt
        if updatedAt is not None:
            self.updatedAt = updatedAt
        if Media is not None:
            self.Media = Media
        if Guid is not None:
            self.Guid = Guid
        if type_ is not None:
            self.type_ = type_


class MediaContainer(BaseModel):
    def __init__(
        self,
        size: float = None,
        allowSync: bool = None,
        identifier: str = None,
        mediaTagPrefix: str = None,
        mediaTagVersion: float = None,
        mixedParents: bool = None,
        Metadata: List[MediaContainerMetadata] = None,
        **kwargs,
    ):
        """
        Initialize MediaContainer
        Parameters:
        ----------
            size: float
            allowSync: bool
            identifier: str
            mediaTagPrefix: str
            mediaTagVersion: float
            mixedParents: bool
            Metadata: list of MediaContainerMetadata
        """
        if size is not None:
            self.size = size
        if allowSync is not None:
            self.allowSync = allowSync
        if identifier is not None:
            self.identifier = identifier
        if mediaTagPrefix is not None:
            self.mediaTagPrefix = mediaTagPrefix
        if mediaTagVersion is not None:
            self.mediaTagVersion = mediaTagVersion
        if mixedParents is not None:
            self.mixedParents = mixedParents
        if Metadata is not None:
            self.Metadata = Metadata


class GetOnDeckResponse(BaseModel):
    def __init__(self, MediaContainer: MediaContainer = None, **kwargs):
        """
        Initialize GetOnDeckResponse
        Parameters:
        ----------
            MediaContainer: MediaContainer
        """
        if MediaContainer is not None:
            self.MediaContainer = MediaContainer
