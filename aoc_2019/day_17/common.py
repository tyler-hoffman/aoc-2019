from aoc_2019.common.machine import Machine


def get_map(code: list[int]) -> list[str]:
    chars = list[str]()
    machine = Machine(code, send_output=lambda x: chars.append(chr(x)))
    machine.run()
    return [line for line in "".join(chars).split("\n") if line]
