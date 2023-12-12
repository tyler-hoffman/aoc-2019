import pytest

from aoc_2019.day_20.a import get_solution, solve
from aoc_2019.day_20.from_prompt import (
    SAMPLE_INPUT_1,
    SAMPLE_INPUT_2,
    SAMPLE_SOLUTION_1,
    SAMPLE_SOLUTION_2,
)


@pytest.mark.parametrize(
    "input, expected",
    [
        (SAMPLE_INPUT_1, SAMPLE_SOLUTION_1),
        (SAMPLE_INPUT_2, SAMPLE_SOLUTION_2),
    ],
)
def test_solve(input: str, expected: int):
    assert solve(input) == expected


@pytest.mark.skip
def test_my_solution():
    assert get_solution() == "NOT THIS"
