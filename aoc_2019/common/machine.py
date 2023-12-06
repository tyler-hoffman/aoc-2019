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

    def run(self) -> None:
        memory = self.memory
        running = True

        while running:
            op_code = memory[self.pos] % 100

            match op_code:
                case 1:
                    memory[self.param(3)] = (
                        memory[self.param(1)] + memory[self.param(2)]
                    )
                    self.pos += 4
                case 2:
                    memory[self.param(3)] = (
                        memory[self.param(1)] * memory[self.param(2)]
                    )
                    self.pos += 4
                case 3:
                    assert self.get_input is not None
                    memory[self.param(1)] = self.get_input()
                    self.pos += 2
                case 4:
                    assert self.send_output is not None
                    self.send_output(memory[self.param(1)])
                    self.pos += 2
                case 5:
                    if memory[self.param(1)]:
                        self.pos = memory[self.param(2)]
                    else:
                        self.pos += 3
                case 6:
                    if not memory[self.param(1)]:
                        self.pos = memory[self.param(2)]
                    else:
                        self.pos += 3
                case 7:
                    memory[self.param(3)] = (
                        1 if memory[self.param(1)] < memory[self.param(2)] else 0
                    )
                    self.pos += 4
                case 8:
                    memory[self.param(3)] = (
                        1 if memory[self.param(1)] == memory[self.param(2)] else 0
                    )
                    self.pos += 4
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

    def param(self, offset: int) -> int:
        mode = self.memory[self.pos] // (10 ** (offset + 1)) % 10

        match mode:
            case 0:
                return self.memory[self.pos + offset]
            case 1:
                return self.pos + offset
            case _:
                assert False
