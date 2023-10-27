from enum import Enum

class IncludeDetails(Enum):
     = "0"
    V1 = "1"
    def list():
        return list(map(lambda x: x.value, IncludeDetails._member_map_.values()))