"""
Test for year 2024, day 15 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
"""

from adventofcode.src.d15 import run


def test_run(benchmark) -> None:
    test_data = ""
    assert benchmark(run, test_data) == (None, None)
