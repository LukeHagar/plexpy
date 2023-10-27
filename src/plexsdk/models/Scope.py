from enum import Enum


class Scope(Enum):
    ALL = "all"

    def list():
        return list(map(lambda x: x.value, Scope._member_map_.values()))
