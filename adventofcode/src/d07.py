"""
Solution for day 7 of the 2024 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution 7` from the project root.
"""

from adventofcode.types import Solution
from itertools import product

def find_operations(numbers, target, use_concat=False):
    n = len(numbers)
    if n < 2:
        return []

    operators = ["+", "*"]
    if use_concat:
        operators.append("||")

    # Generate all combinations of operators
    operator_combinations = product(operators, repeat=n-1)
    state = False

    for ops in operator_combinations:
        result = numbers[0]
        expression = str(numbers[0])
        
        for i, op in enumerate(ops):
            if op == "+":
                result += numbers[i+1]
            elif op == "*":
                result *= numbers[i+1]
            elif op == "||":
                # Concatenate as strings, then convert to integer
                result = int(str(result) + str(numbers[i+1]))
            expression += f" {op} {numbers[i+1]}"
        
        if result == target:
            state = True
            break

    return state

def run(data: str) -> Solution:
    results = [int(line.split(": ")[0]) for line in data.split("\n")]
    values = [[int(char) for char in line.split(": ")[1].split(" ")] for line in data.split("\n")]
    calibration = [find_operations(values[idx], res) for idx, res in enumerate(results)]
    calibration2 = [find_operations(values[idx], res, True) for idx, res in enumerate(results)]
    final_sum = sum([res for idx, res in enumerate(results) if calibration[idx]])
    final_sum2 = sum([res for idx, res in enumerate(results) if calibration2[idx]])
    return (final_sum, final_sum2)
