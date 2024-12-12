"""
Test for year 2024, day 12 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
"""

from adventofcode.src.d12 import run


def test_run(benchmark) -> None:
    test_data = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
    assert benchmark(run, test_data) == (1930, 1206)
