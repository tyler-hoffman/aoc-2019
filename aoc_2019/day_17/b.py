from dataclasses import dataclass
from functools import cached_property
from typing import Iterable, Optional
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
        function_options = list(self.get_function_options(0, []))
        instructions = self.get_instructions(function_options)

        return self.run_it(instructions)

    def to_instruction_stack(self, lines: list[str]) -> list[int]:
        together = "\n".join(lines) + "\n"

        return list(reversed([ord(x) for x in together]))

    def get_instructions(
        self,
        function_options: list[list[list[str | int]]],
    ) -> list[str]:
        for function_option in function_options:
            main = self.get_main(
                {
                    "A": function_option[0],
                    "B": function_option[1],
                    "C": function_option[2],
                }
            )
            if main:
                return [
                    ",".join(main),
                    *[",".join([str(x) for x in f]) for f in function_option],
                ]
        assert False

    def get_main(
        self,
        functions: dict[str, list[str | int]],
        pos: int = 0,
        so_far: list[str] = [],
    ) -> Optional[list[str]]:
        if pos > len(self.path):
            return None
        elif len(so_far) > 10:
            return None
        elif pos == len(self.path):
            return so_far[:]
        else:
            found_match: Optional[list[str]] = None
            for key, function in functions.items():
                if self.path[pos : pos + len(function)] == function:
                    so_far.append(key)
                    match = self.get_main(functions, pos + len(function), so_far)
                    so_far.pop()
                    if match:
                        found_match = match
            return found_match

    def get_function_options(
        self,
        pos: int,
        found: list[list[str | int]],
    ) -> Iterable[list[list[str | int]]]:
        if pos >= len(self.path):
            return

        if len(found) == 3:
            if all([len(",".join([str(x) for x in f])) <= 20 for f in found]):
                yield found[:]
            return

        for f in found:
            if self.path[pos : pos + len(f)] == f:
                yield from self.get_function_options(pos + len(f), found)
        for i in range(1, 10):
            variation = self.path[pos : pos + i]
            found.append(variation)
            yield from self.get_function_options(pos + i, found)
            found.pop()

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
    def path(self) -> list[str | int]:
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

    def debug(self, instructions: list[str]) -> None:
        """Just for visual debugging"""
        instructions.append("y")
        instruction_stack = self.to_instruction_stack(instructions)
        code = self.code[:]
        code[0] = 2
        chars = list[str]()

        def send_visual_output(val: int) -> None:
            char = chr(val)
            if char == "\n" and chars[-1] == "\n":
                the_map = "".join(chars).split("\n")
                print("\n".join(the_map))
                chars.clear()
            else:
                chars.append(char)

        machine = Machine(
            code,
            send_output=send_visual_output,
            get_input=lambda: instruction_stack.pop(),
        )
        machine.run()

    def run_it(self, instructions: list[str]) -> int:
        instructions.append("n")
        instruction_stack = self.to_instruction_stack(instructions)
        code = self.code[:]
        code[0] = 2
        output_vals = list[int]()

        machine = Machine(
            code,
            send_output=lambda x: output_vals.append(x),
            get_input=lambda: instruction_stack.pop(),
        )
        machine.run()
        return output_vals[-1]

    def is_scaffold(self, point: Point) -> bool:
        return (
            point.x >= 0
            and point.x < self.width
            and point.y >= 0
            and point.y < self.height
            and self.map[point.y][point.x] != "."
        )


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
