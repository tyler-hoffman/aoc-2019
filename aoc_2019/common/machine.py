from collections import defaultdict
from dataclasses import dataclass, field
from functools import cached_property
from typing import Callable, Optional, Sequence


@dataclass
class Machine:
    code: Sequence[int]
    get_input: Optional[Callable[[], int]] = None
    send_output: Optional[Callable[[int], None]] = None
    pos: int = field(default=0, init=False)
    relative_base: int = field(default=0, init=False)

    def run(self) -> None:
        memory = self.memory
        running = True

        while running:
            op_code = memory[self.pos] % 100

            match op_code:
                case 1:
                    self.write(3, self.read(1) + self.read(2))
                    self.pos += 4
                case 2:
                    self.write(3, self.read(1) * self.read(2))
                    self.pos += 4
                case 3:
                    assert self.get_input is not None
                    self.write(1, self.get_input())
                    self.pos += 2
                case 4:
                    assert self.send_output is not None
                    self.send_output(self.read(1))
                    self.pos += 2
                case 5:
                    if self.read(1):
                        self.pos = self.read(2)
                    else:
                        self.pos += 3
                case 6:
                    if not self.read(1):
                        self.pos = self.read(2)
                    else:
                        self.pos += 3
                case 7:
                    self.write(3, 1 if self.read(1) < self.read(2) else 0)
                    self.pos += 4
                case 8:
                    self.write(3, 1 if self.read(1) == self.read(2) else 0)
                    self.pos += 4
                case 9:
                    self.relative_base += self.read(1)
                    self.pos += 2
                case 99:
                    running = False
                case _:
                    assert False

    @cached_property
    def memory(self) -> defaultdict[int, int]:
        output = defaultdict[int, int](int)

        for index, value in enumerate(self.code):
            output[index] = value

        return output

    def read(self, offset: int) -> int:
        mode = self.memory[self.pos] // (10 ** (offset + 1)) % 10
        value = self.memory[self.pos + offset]

        match mode:
            case 0:  # position
                return self.memory[value]
            case 1:  # immediate
                return value
            case 2:  # relative
                return self.memory[self.relative_base + value]
            case _:
                assert False

    def write(self, offset: int, value: int) -> None:
        mode = self.memory[self.pos] // (10 ** (offset + 1)) % 10
        address = self.memory[self.pos + offset]

        match mode:
            case 0:
                self.memory[address] = value
            case 2:
                self.memory[self.relative_base + address] = value
            case _:
                assert False
