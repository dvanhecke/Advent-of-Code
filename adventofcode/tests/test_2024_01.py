"""
Test for year 2024, day 1 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
"""

from adventofcode.src.d01 import run


def test_run(benchmark) -> None:
    test_input = """3   4
4   3
2   5
1   3
3   9
3   3"""
    assert benchmark(run, test_input) == (11, 31)
