import pytest
from aoc_2019.common.machine import Machine
from aoc_2019.day_05.b import get_solution
from aoc_2019.day_05.from_prompt import SAMPLE_DATA, SAMPLE_OUTPUT, SIMPLE_TEST_DATA
from aoc_2019.day_05.parser import Parser


@pytest.mark.parametrize("code, input, expected", SIMPLE_TEST_DATA)
def test_simple_data(code: str, input: int, expected: int):
    output = list[int]()
    machine = Machine(
        code=Parser.parse(code),
        get_input=lambda: input,
        send_output=lambda x: output.append(x),
    )

    machine.run()

    assert len(output) == 1
    assert output[0] == expected


@pytest.mark.parametrize("input, expected", SAMPLE_OUTPUT)
def test_sample(input: int, expected: int):
    output = list[int]()
    machine = Machine(
        code=Parser.parse(SAMPLE_DATA),
        get_input=lambda: input,
        send_output=lambda x: output.append(x),
    )

    machine.run()

    assert len(output) == 1
    assert output[0] == expected


def test_my_solution():
    assert get_solution() == 11430197
