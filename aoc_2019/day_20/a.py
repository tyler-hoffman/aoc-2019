from dataclasses import dataclass
from aoc_2019.day_20.common import Map
from aoc_2019.day_20.parser import Parser


@dataclass
class Day20PartASolver:
    map: Map

    @property
    def solution(self) -> int:
        dists = self.map.dists
        return -1


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day20PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2019/day_20/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
