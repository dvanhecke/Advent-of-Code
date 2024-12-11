"""
Test for year 2024, day 3 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
"""

from adventofcode.src.d03 import run


def test_run(benchmark) -> None:
    test_data="xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    assert benchmark(run, test_data) == (161,48)
