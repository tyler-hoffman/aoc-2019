from __future__ import annotations
from dataclasses import dataclass
from functools import cached_property, total_ordering
from queue import PriorityQueue
from typing import Mapping, Optional

from aoc_2019.common.point import Point


@total_ordering
@dataclass(frozen=True)
class Portal:
    label: str
    point: Point
    outside: bool

    def __lt__(self, other: Portal) -> bool:
        return (self.label, self.outside) < (other.label, other.outside)

    @property
    def shadow(self) -> Portal:
        return Portal(self.label, self.point, not self.outside)


@dataclass(frozen=True)
class Map:
    outer_portals: dict[str, Portal]
    inner_portals: dict[str, Portal]
    points: set[Point]

    def __post_init__(self) -> None:
        assert all(p.point in self.points for p in self.outer_portals.values())
        assert all(p.point in self.points for p in self.inner_portals.values())

    @cached_property
    def start(self) -> Portal:
        return next(p for p in self.outer_portals.values() if p.label == "AA")

    @cached_property
    def goal(self) -> Portal:
        return next(p for p in self.outer_portals.values() if p.label == "ZZ")

    @cached_property
    def shadows(self) -> Mapping[Portal, Portal]:
        output = dict[Portal, Portal]()
        for inner in self.inner_portals.values():
            outer = self.outer_portals[inner.label]
            output[inner] = outer
            output[outer] = inner
        return output

    @cached_property
    def portals_by_point(self) -> Mapping[Point, Portal]:
        output = dict[Point, Portal]()
        for p in self.outer_portals.values():
            output[p.point] = p
        for p in self.inner_portals.values():
            output[p.point] = p
        return output

    @cached_property
    def connections(self) -> Mapping[Portal, set[Portal]]:
        output = dict[Portal, set[Portal]]()
        for (a, b), _ in self.dists.items():
            if a not in output:
                output[a] = set()
            output[a].add(b)
        return output

    @cached_property
    def dists(self) -> Mapping[tuple[Portal, Portal], int]:
        output = dict[tuple[Portal, Portal], int]()
        for p in self.outer_portals.values():
            for portal, dist in self.find_connections(p):
                output[(p, portal)] = dist
        for p in self.inner_portals.values():
            for portal, dist in self.find_connections(p):
                output[(p, portal)] = dist
        return output

    def find_connections(self, portal: Portal) -> list[tuple[Portal, int]]:
        output = list[tuple[Portal, int]]()
        queue = PriorityQueue[tuple[int, Point]]()
        queue.put((0, portal.point))
        seen = {portal.point}

        while not queue.empty():
            dist, point = queue.get()
            p = self.portals_by_point.get(point)
            if p and p != portal:
                output.append((p, dist))
            for n in point.neighbors:
                if n in self.points and n not in seen:
                    queue.put((dist + 1, n))
                    seen.add(n)

        return output
