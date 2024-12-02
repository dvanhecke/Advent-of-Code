"""
Test for year 2024, day 2 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
"""

from adventofcode.src.d02 import run


def test_run() -> None:
    test_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
    assert run(test_data) == (2, 4)
