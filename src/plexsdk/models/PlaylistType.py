from enum import Enum


class PlaylistType(Enum):
    AUDIO = "audio"
    VIDEO = "video"
    PHOTO = "photo"

    def list():
        return list(map(lambda x: x.value, PlaylistType._member_map_.values()))
