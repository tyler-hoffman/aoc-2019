from dataclasses import dataclass

from aoc_2019.common.point import Point


@dataclass(frozen=True)
class Portal:
    label: str
    point: Point


@dataclass(frozen=True)
class Map:
    outer_portals: dict[str, Portal]
    inner_portals: dict[str, Portal]
    points: set[Point]

    def __post_init__(self) -> None:
        assert all(p.point in self.points for p in self.outer_portals.values())
        assert all(p.point in self.points for p in self.inner_portals.values())
