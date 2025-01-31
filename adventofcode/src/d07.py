"""
Solution for day 7 of the 2024 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution 7` from the project root.
"""

from adventofcode.types import Solution
from itertools import product
from concurrent.futures import ProcessPoolExecutor, as_completed


def find_operations(numbers, target, idx, use_concat=False):
    n = len(numbers)
    if n < 2:
        return []

    operators = ["+", "*"]
    if use_concat:
        operators.append("||")

    # Generate all combinations of operators
    operator_combinations = product(operators, repeat=n - 1)
    state = False

    for ops in operator_combinations:
        result = numbers[0]
        expression = str(numbers[0])

        for i, op in enumerate(ops):
            if op == "+":
                result += numbers[i + 1]
            elif op == "*":
                result *= numbers[i + 1]
            elif op == "||":
                # Concatenate as strings, then convert to integer
                result = int(str(result) + str(numbers[i + 1]))
            expression += f" {op} {numbers[i+1]}"

        if result == target:
            state = True
            break

    return state, use_concat, idx


def run_parallel_tasks(numbers, targets):
    with ProcessPoolExecutor() as executor:
        tasks = []

        for idx, target in enumerate(targets):
            tasks.append(executor.submit(find_operations, numbers[idx], target, idx))
            tasks.append(
                executor.submit(find_operations, numbers[idx], target, idx, True)
            )

        # Wait for all processes to finish
        results = [
            [0, 0] for _ in range(len(targets))
        ]  # Initialize results for all targets

        for task in as_completed(tasks):
            res, concat, idx = task.result()
            if concat:
                results[idx][1] = res
            else:
                results[idx][0] = res

    return results


def run(data: str) -> Solution:
    results = [int(line.split(": ")[0]) for line in data.split("\n")]
    values = [
        [int(char) for char in line.split(": ")[1].split(" ")]
        for line in data.split("\n")
    ]
    calibrations = run_parallel_tasks(values, results)
    with_concat = sum([res for idx, res in enumerate(results) if calibrations[idx][1]])
    without_concat = sum(
        [res for idx, res in enumerate(results) if calibrations[idx][0]]
    )
    return (without_concat, with_concat)
