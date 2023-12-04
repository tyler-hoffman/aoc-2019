import copy
from dataclasses import dataclass
from aoc_2019.common.machine import Machine
from aoc_2019.day_02.parser import Parser


@dataclass
class Day02PartBSolver:
    code: list[int]
    target = 19690720

    @property
    def solution(self) -> int:
        for noun in range(100):
            for verb in range(100):
                code = copy.copy(self.code)
                code[1] = noun
                code[2] = verb
                machine = Machine(code)
                machine.run()
                if code[0] == self.target:
                    return 100 * noun + verb

        assert False


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day02PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2019/day_02/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
