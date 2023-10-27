from enum import Enum


class State(Enum):
    PLAYING = "playing"
    PAUSED = "paused"
    STOPPED = "stopped"

    def list():
        return list(map(lambda x: x.value, State._member_map_.values()))
