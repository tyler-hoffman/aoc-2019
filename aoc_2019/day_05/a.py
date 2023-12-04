from dataclasses import dataclass
from aoc_2019.common.machine import Machine
from aoc_2019.day_05.parser import Parser


@dataclass
class Day05PartASolver:
    code: list[int]

    @property
    def solution(self) -> int:
        output = list[int]()
        machine = Machine(
            code=self.code, get_input=lambda: 1, send_output=lambda x: output.append(x)
        )
        machine.run()

        return output[-1]


def solve(input: str) -> int:
    code = Parser.parse(input)
    solver = Day05PartASolver(code)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2019/day_05/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
