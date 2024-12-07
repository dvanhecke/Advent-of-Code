"""
Test for year 2024, day 7 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
"""

from adventofcode.src.d07 import run


def test_run() -> None:
    test_data = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
    assert run(test_data) == (3749, 11387)
