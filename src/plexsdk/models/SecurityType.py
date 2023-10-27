from enum import Enum


class SecurityType(Enum):
    DELEGATION = "delegation"

    def list():
        return list(map(lambda x: x.value, SecurityType._member_map_.values()))
