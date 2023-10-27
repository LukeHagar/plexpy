from enum import Enum


class Type(Enum):
    AUDIO = "audio"
    VIDEO = "video"
    PHOTO = "photo"

    def list():
        return list(map(lambda x: x.value, Type._member_map_.values()))
