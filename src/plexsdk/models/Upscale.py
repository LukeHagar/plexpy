from enum import Enum

class Upscale(Enum):
     = "0"
    V1 = "1"
    def list():
        return list(map(lambda x: x.value, Upscale._member_map_.values()))