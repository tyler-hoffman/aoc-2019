from dataclasses import dataclass
from functools import cached_property
from aoc_2019.common.machine import Machine
from aoc_2019.common.point import Point
from aoc_2019.day_17.common import get_map
from aoc_2019.day_17.parser import Parser

DIRECTIONS = [
    Point(0, -1),
    Point(1, 0),
    Point(0, 1),
    Point(-1, 0),
]


@dataclass
class Day17PartBSolver:
    code: list[int]

    @property
    def solution(self) -> int:
        path = self.whole_path
        self.run_it()
        return -1

    @cached_property
    def map(self) -> list[str]:
        return get_map(self.code)

    @cached_property
    def start(self) -> Point:
        for y, line in enumerate(self.map):
            for x, ch in enumerate(line):
                if ch == "^":
                    return Point(x, y)
        assert False

    @cached_property
    def width(self) -> int:
        return len(self.map[0])

    @cached_property
    def height(self) -> int:
        return len(self.map)

    @cached_property
    def whole_path(self) -> list[str | int]:
        output = list[str | int]()
        pos = self.start
        direction_index = 0
        steps = 0
        while True:
            direction = DIRECTIONS[direction_index]
            next_pos = pos.add(direction)
            if self.is_scaffold(next_pos):
                pos = next_pos
                steps += 1
            else:
                if steps:
                    output.append(steps)
                    steps = 0
                right_index = (direction_index + 1) % 4
                left_index = (direction_index + 3) % 4
                right = DIRECTIONS[right_index]
                left = DIRECTIONS[left_index]
                if self.is_scaffold(pos.add(right)):
                    direction_index = right_index
                    output.append("R")
                elif self.is_scaffold(pos.add(left)):
                    direction_index = left_index
                    output.append("L")
                else:
                    break

        return output

    def run_it(self) -> None:
        code = self.code[:]
        code[0] = 2
        instruction_stack = get_instructions()
        chars = list[str]()

        def send_output(val: int) -> None:
            char = chr(val)
            if char == "\n" and chars[-1] == "\n":
                the_map = "".join(chars).split("\n")
                print("\n".join(the_map))
                chars.clear()
            else:
                chars.append(char)

        machine = Machine(
            code,
            send_output=send_output,
            get_input=lambda: instruction_stack.pop(),
        )
        machine.run()

    def is_scaffold(self, point: Point) -> bool:
        return (
            point.x >= 0
            and point.x < self.width
            and point.y >= 0
            and point.y < self.height
            and self.map[point.y][point.x] != "."
        )


def get_instructions() -> list[int]:
    instructions = """
        A,A,A,A,A,A,A,A,A,A
        R,R,R,R,R,R,R,R,R,R
        R
        R
        y
        """.strip()

    lines = [line.strip() for line in instructions.splitlines()]
    together = "\n".join(lines) + "\n"

    return list(reversed([ord(x) for x in together]))


def solve(input: str) -> int:
    code = Parser.parse(input)
    solver = Day17PartBSolver(code)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2019/day_17/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
