from enum import Enum

class Force(Enum):
     = "0"
    V1 = "1"
    def list():
        return list(map(lambda x: x.value, Force._member_map_.values()))