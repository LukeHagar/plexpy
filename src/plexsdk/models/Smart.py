from enum import Enum

class Smart(Enum):
     = "0"
    V1 = "1"
    def list():
        return list(map(lambda x: x.value, Smart._member_map_.values()))