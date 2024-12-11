"""
Test for year 2024, day 11 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
"""

from adventofcode.src.d11 import run


def test_run() -> None:
    test = "125 17"
    assert run(test) == (55312, 65601038650482)
