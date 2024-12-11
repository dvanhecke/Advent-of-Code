"""
Test for year 2024, day 19 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
"""

from adventofcode.src.d19 import run


def test_run(benchmark) -> None:
    test_data = ""
    assert benchmark(run, test_data) == (None, None)
