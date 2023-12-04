from dataclasses import dataclass
from typing import Callable, Optional


@dataclass
class Machine:
    code: list[int]
    get_input: Optional[Callable[[], int]] = None
    send_output: Optional[Callable[[int], None]] = None

    def run(self) -> None:
        code = self.code
        pos = 0
        running = True

        while running:
            op_code = self.code[pos] % 100
            c = (self.code[pos] // 100) % 10
            b = self.code[pos] // 1000 % 10
            a = self.code[pos] // 10000 % 10

            param_a = code[pos + 1] if c == 0 else pos + 1
            param_b = code[pos + 2] if b == 0 else pos + 2
            param_c = code[pos + 3] if a == 0 else pos + 3

            match op_code:
                case 1:
                    code[param_c] = code[param_a] + code[param_b]
                    pos += 4
                case 2:
                    code[param_c] = code[param_a] * code[param_b]
                    pos += 4
                case 3:
                    assert self.get_input is not None
                    code[param_a] = self.get_input()
                    pos += 2
                case 4:
                    assert self.send_output is not None
                    self.send_output(code[param_a])
                    pos += 2
                case 99:
                    running = False
                case _:
                    assert False
