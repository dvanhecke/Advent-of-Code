"""
Test for year 2024, day 5 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
"""

from adventofcode.src.d05 import run


def test_run(benchmark) -> None:
    test_data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
    assert benchmark(run, test_data) == (143, 123)
