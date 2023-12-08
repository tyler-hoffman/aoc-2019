from collections import defaultdict
from dataclasses import dataclass
from functools import cached_property
from typing import Iterable
from aoc_2019.common.point import Point
from aoc_2019.day_17.common import get_map
from aoc_2019.day_17.parser import Parser


@dataclass
class Day17PartASolver:
    input: list[str]

    @property
    def solution(self) -> int:
        intersections = [p for p in self.documented_points if self.is_intersection(p)]
        return sum(i.x * i.y for i in intersections)

    def is_intersection(self, p: Point) -> bool:
        return all(
            [
                self.points[Point(p.x, p.y)] == "#",
                self.points[Point(p.x - 1, p.y)] == "#",
                self.points[Point(p.x + 1, p.y)] == "#",
                self.points[Point(p.x, p.y - 1)] == "#",
                self.points[Point(p.x, p.y + 1)] == "#",
            ]
        )

    @cached_property
    def points(self) -> defaultdict[Point, str]:
        output = defaultdict[Point, str](lambda: ".")
        for point in self.documented_points:
            output[point] = self.input[point.y][point.x]
        return output

    @cached_property
    def documented_points(self) -> Iterable[Point]:
        output = list[Point]()
        for y, line in enumerate(self.input):
            for x, _ in enumerate(line):
                output.append(Point(x, y))
        return output


def solve(input: str) -> int:
    lines = Parser.parse(input)
    the_map = get_map(lines)
    solver = Day17PartASolver(the_map)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2019/day_17/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
