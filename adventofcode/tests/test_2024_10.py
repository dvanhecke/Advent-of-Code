"""
Test for year 2024, day 10 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
"""

from adventofcode.src.d10 import run


def test_run() -> None:
    test_data = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
    assert run(test_data) == (36, 81)
