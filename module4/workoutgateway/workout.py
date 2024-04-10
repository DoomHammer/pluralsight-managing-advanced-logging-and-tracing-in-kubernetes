from dataclasses import dataclass, asdict
from enum import Enum
from typing import Dict

class WorkoutKind(Enum):
    RUNNING = "running"
    JUMPING = "jumping"
    SWIMMING = "swimming"


@dataclass
class Workout:
    kind: WorkoutKind
    begin: int
    end: int
    other: Dict

    @classmethod
    def from_dict(cls, d: Dict) -> "Workout":
        kind = d.pop("kind")
        if kind not in set(map(lambda e: e[1].value, dict(WorkoutKind.__members__).items())):
            raise ValueError("'{}' is not a WorkoutKind".format(kind))

        begin = int(d.pop("begin"))
        if not 0 <= begin < 2459:
            raise ValueError("Wrong value for begin!")

        end = int(d.pop("end"))
        if not 0 <= end < 2459:
            raise ValueError("Wrong value for end!")

        other = d

        return cls(kind=kind, begin=begin, end=end, other=other)

    def as_dict(self) -> Dict:
        d = asdict(self)
        do = d.pop("other")
        d.pop("kind")
        d.update(do)

        return d