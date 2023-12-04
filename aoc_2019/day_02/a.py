from dataclasses import dataclass
from functools import cached_property
from aoc_2019.common.machine import Machine
from aoc_2019.day_02.parser import Parser


@dataclass
class Day02PartASolver:
    code: list[int]

    @property
    def solution(self) -> int:
        self.code[1] = 12
        self.code[2] = 2
        self.machine.run()
        return self.machine.code[0]

    @cached_property
    def machine(self) -> Machine:
        return Machine(self.code)


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day02PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2019/day_02/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
