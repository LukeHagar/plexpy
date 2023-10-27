from enum import Enum

class OnlyTransient(Enum):
     = "0"
    V1 = "1"
    def list():
        return list(map(lambda x: x.value, OnlyTransient._member_map_.values()))