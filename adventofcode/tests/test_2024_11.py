"""
Test for year 2024, day 11 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
"""

from adventofcode.src.d11 import run


def test_run(benchmark) -> None:
    test_data = "125 17"
    assert benchmark(run, test_data) == (55312, 65601038650482)
