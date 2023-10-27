from enum import Enum

class Level(Enum):
     = "0"
    V1 = "1"
    V2 = "2"
    V3 = "3"
    V4 = "4"
    def list():
        return list(map(lambda x: x.value, Level._member_map_.values()))