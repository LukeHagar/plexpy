from .base import BaseModel
from typing import List


class MediaContainerMetadataMediaPart(BaseModel):
    def __init__(
        self,
        id: float = None,
        key: str = None,
        duration: float = None,
        file: str = None,
        size: float = None,
        container: str = None,
        has64bitOffsets: bool = None,
        hasThumbnail: float = None,
        optimizedForStreaming: bool = None,
        videoProfile: str = None,
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
            container: str
            has64bitOffsets: bool
            hasThumbnail: float
            optimizedForStreaming: bool
            videoProfile: str
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
        if container is not None:
            self.container = container
        if has64bitOffsets is not None:
            self.has64bitOffsets = has64bitOffsets
        if hasThumbnail is not None:
            self.hasThumbnail = hasThumbnail
        if optimizedForStreaming is not None:
            self.optimizedForStreaming = optimizedForStreaming
        if videoProfile is not None:
            self.videoProfile = videoProfile


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
        videoResolution: float = None,
        container: str = None,
        videoFrameRate: str = None,
        optimizedForStreaming: float = None,
        has64bitOffsets: bool = None,
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
            videoResolution: float
            container: str
            videoFrameRate: str
            optimizedForStreaming: float
            has64bitOffsets: bool
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
        if optimizedForStreaming is not None:
            self.optimizedForStreaming = optimizedForStreaming
        if has64bitOffsets is not None:
            self.has64bitOffsets = has64bitOffsets
        if videoProfile is not None:
            self.videoProfile = videoProfile
        if Part is not None:
            self.Part = Part


class MediaContainerMetadataGenre(BaseModel):
    def __init__(self, tag: str = None, **kwargs):
        """
        Initialize MediaContainerMetadataGenre
        Parameters:
        ----------
            tag: str
        """
        if tag is not None:
            self.tag = tag


class MediaContainerMetadataDirector(BaseModel):
    def __init__(self, tag: str = None, **kwargs):
        """
        Initialize MediaContainerMetadataDirector
        Parameters:
        ----------
            tag: str
        """
        if tag is not None:
            self.tag = tag


class MediaContainerMetadataWriter(BaseModel):
    def __init__(self, tag: str = None, **kwargs):
        """
        Initialize MediaContainerMetadataWriter
        Parameters:
        ----------
            tag: str
        """
        if tag is not None:
            self.tag = tag


class MediaContainerMetadataCountry(BaseModel):
    def __init__(self, tag: str = None, **kwargs):
        """
        Initialize MediaContainerMetadataCountry
        Parameters:
        ----------
            tag: str
        """
        if tag is not None:
            self.tag = tag


class MediaContainerMetadataRole(BaseModel):
    def __init__(self, tag: str = None, **kwargs):
        """
        Initialize MediaContainerMetadataRole
        Parameters:
        ----------
            tag: str
        """
        if tag is not None:
            self.tag = tag


class MediaContainerMetadata(BaseModel):
    def __init__(
        self,
        allowSync: bool = None,
        librarySectionID: float = None,
        librarySectionTitle: str = None,
        librarySectionUUID: str = None,
        ratingKey: float = None,
        key: str = None,
        guid: str = None,
        studio: str = None,
        title: str = None,
        contentRating: str = None,
        summary: str = None,
        rating: float = None,
        audienceRating: float = None,
        year: float = None,
        tagline: str = None,
        thumb: str = None,
        art: str = None,
        duration: float = None,
        originallyAvailableAt: str = None,
        addedAt: float = None,
        updatedAt: float = None,
        audienceRatingImage: str = None,
        chapterSource: str = None,
        primaryExtraKey: str = None,
        ratingImage: str = None,
        Media: List[MediaContainerMetadataMedia] = None,
        Genre: List[MediaContainerMetadataGenre] = None,
        Director: List[MediaContainerMetadataDirector] = None,
        Writer: List[MediaContainerMetadataWriter] = None,
        Country: List[MediaContainerMetadataCountry] = None,
        Role: List[MediaContainerMetadataRole] = None,
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
            guid: str
            studio: str
            title: str
            contentRating: str
            summary: str
            rating: float
            audienceRating: float
            year: float
            tagline: str
            thumb: str
            art: str
            duration: float
            originallyAvailableAt: str
            addedAt: float
            updatedAt: float
            audienceRatingImage: str
            chapterSource: str
            primaryExtraKey: str
            ratingImage: str
            Media: list of MediaContainerMetadataMedia
            Genre: list of MediaContainerMetadataGenre
            Director: list of MediaContainerMetadataDirector
            Writer: list of MediaContainerMetadataWriter
            Country: list of MediaContainerMetadataCountry
            Role: list of MediaContainerMetadataRole
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
        if guid is not None:
            self.guid = guid
        if studio is not None:
            self.studio = studio
        if title is not None:
            self.title = title
        if contentRating is not None:
            self.contentRating = contentRating
        if summary is not None:
            self.summary = summary
        if rating is not None:
            self.rating = rating
        if audienceRating is not None:
            self.audienceRating = audienceRating
        if year is not None:
            self.year = year
        if tagline is not None:
            self.tagline = tagline
        if thumb is not None:
            self.thumb = thumb
        if art is not None:
            self.art = art
        if duration is not None:
            self.duration = duration
        if originallyAvailableAt is not None:
            self.originallyAvailableAt = originallyAvailableAt
        if addedAt is not None:
            self.addedAt = addedAt
        if updatedAt is not None:
            self.updatedAt = updatedAt
        if audienceRatingImage is not None:
            self.audienceRatingImage = audienceRatingImage
        if chapterSource is not None:
            self.chapterSource = chapterSource
        if primaryExtraKey is not None:
            self.primaryExtraKey = primaryExtraKey
        if ratingImage is not None:
            self.ratingImage = ratingImage
        if Media is not None:
            self.Media = Media
        if Genre is not None:
            self.Genre = Genre
        if Director is not None:
            self.Director = Director
        if Writer is not None:
            self.Writer = Writer
        if Country is not None:
            self.Country = Country
        if Role is not None:
            self.Role = Role
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


class GetRecentlyAddedResponse(BaseModel):
    def __init__(self, MediaContainer: MediaContainer = None, **kwargs):
        """
        Initialize GetRecentlyAddedResponse
        Parameters:
        ----------
            MediaContainer: MediaContainer
        """
        if MediaContainer is not None:
            self.MediaContainer = MediaContainer
