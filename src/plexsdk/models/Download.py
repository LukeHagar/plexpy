from enum import Enum

class Download(Enum):
     = "0"
    V1 = "1"
    def list():
        return list(map(lambda x: x.value, Download._member_map_.values()))