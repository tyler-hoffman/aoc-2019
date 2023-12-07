from aoc_2019.day_17.a import Day17PartASolver, get_solution
from aoc_2019.day_17.from_prompt import SAMPLE_MAP, SAMPLE_OUTPUT


def test_for_map():
    assert Day17PartASolver(SAMPLE_MAP).solution == SAMPLE_OUTPUT  # type: ignore


def test_my_solution():
    assert get_solution() == 1544
