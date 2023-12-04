from dataclasses import dataclass, field
from typing import Callable, Optional


@dataclass
class Machine:
    code: list[int]
    get_input: Optional[Callable[[], int]] = None
    send_output: Optional[Callable[[int], None]] = None
    pos: int = field(default=0, init=False)

    def run(self) -> None:
        code = self.code
        running = True

        while running:
            op_code = self.code[self.pos] % 100

            match op_code:
                case 1:
                    code[self.param(3)] = code[self.param(1)] + code[self.param(2)]
                    self.pos += 4
                case 2:
                    code[self.param(3)] = code[self.param(1)] * code[self.param(2)]
                    self.pos += 4
                case 3:
                    assert self.get_input is not None
                    code[self.param(1)] = self.get_input()
                    self.pos += 2
                case 4:
                    assert self.send_output is not None
                    self.send_output(code[self.param(1)])
                    self.pos += 2
                case 99:
                    running = False
                case _:
                    assert False

    def param(self, offset: int) -> int:
        code = self.code
        pos = self.pos
        mode = code[pos] // (10 ** (offset + 1)) % 10

        match mode:
            case 0:
                return code[pos + offset]
            case 1:
                return pos + offset
            case _:
                assert False
