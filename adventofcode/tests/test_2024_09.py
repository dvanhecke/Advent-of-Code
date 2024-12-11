"""
Test for year 2024, day 9 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
"""

from adventofcode.src.d09 import run


def test_run(benchmark) -> None:
    test_data = "2333133121414131402"
    assert benchmark(run, test_data) == (1928, 2858)
