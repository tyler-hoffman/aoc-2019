from __future__ import annotations
from dataclasses import dataclass
from functools import total_ordering


@total_ordering
@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def add(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)

    @property
    def neighbors(self) -> set[Point]:
        return {
            Point(self.x + 1, self.y),
            Point(self.x - 1, self.y),
            Point(self.x, self.y + 1),
            Point(self.x, self.y - 1),
        }

    def __lt__(self, other: Point) -> bool:
        return (self.y, self.x) < (other.y, other.x)
