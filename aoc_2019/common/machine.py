from dataclasses import dataclass


@dataclass
class Machine:
    code: list[int]

    def run(self) -> None:
        c = self.code
        pos = 0
        running = True

        while running:
            op_code = self.code[pos]
            match op_code:
                case 1:
                    c[c[pos + 3]] = c[c[pos + 1]] + c[c[pos + 2]]
                    pos += 4
                case 2:
                    c[c[pos + 3]] = c[c[pos + 1]] * c[c[pos + 2]]
                    pos += 4
                case 99:
                    running = False
                case _:
                    assert False
