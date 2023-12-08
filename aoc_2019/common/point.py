from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def add(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)
