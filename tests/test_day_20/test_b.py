import pytest

from aoc_2019.day_20.b import get_solution, solve
from aoc_2019.day_20.from_prompt import (
    SAMPLE_INPUT_1,
    SAMPLE_INPUT_3,
    SAMPLE_SOLUTION_1_B,
    SAMPLE_SOLUTION_3_B,
)


@pytest.mark.parametrize(
    "input, expected",
    [
        (SAMPLE_INPUT_1, SAMPLE_SOLUTION_1_B),
        (SAMPLE_INPUT_3, SAMPLE_SOLUTION_3_B),
    ],
)
def test_solve(input: str, expected: int):
    assert solve(input) == expected


def test_my_solution():
    assert get_solution() == 7152
