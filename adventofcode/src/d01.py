"""
Solution for day 1 of the 2024 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution 1` from the project root.
"""

from adventofcode.types import Solution


def run(data: str) -> Solution:
    first_column = [int(line.split("   ")[0]) for line in data.split("\n")]
    second_column = [int(line.split("   ")[1]) for line in data.split("\n")]
    first_column.sort()
    second_column.sort()
    distances = [abs(first_column[i] - second_column[i]) for i in range(len(first_column))]
    multiplicants = [i * second_column.count(i) for i in first_column]
    return sum(distances), sum(multiplicants)
