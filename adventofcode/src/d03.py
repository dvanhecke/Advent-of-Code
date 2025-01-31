"""
Solution for day 3 of the 2024 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution 3` from the project root.
"""

from adventofcode.types import Solution
import re


def mul(a, b):
    return a * b


def run(data: str) -> Solution:
    matches = re.findall(r"mul\([0-9]+,[0-9]+\)", data)
    matches2 = re.findall(r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", data)
    results = [eval(instruction) for instruction in matches]
    results2 = []
    mul_enabled = True
    for match in matches2:
        if match == "do()":
            mul_enabled = True
            continue
        elif match == "don't()":
            mul_enabled = False
            continue
        if mul_enabled:
            results2.append(eval(match))
    return (sum(results), sum(results2))
