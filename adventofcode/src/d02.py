"""
Solution for day 2 of the 2024 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution 2` from the project root.
"""

from adventofcode.types import Solution


def is_decreasing(digits):
    for idx in range(len(digits) - 1):
        if int(digits[idx]) - int(digits[idx + 1]) < 0:
            return False
    return True


def is_increasing(digits):
    for idx in range(len(digits) - 1):
        if int(digits[idx]) - int(digits[idx + 1]) > 0:
            return False
    return True


def is_safe(digits):
    if not is_decreasing(digits) and not is_increasing(digits):
        return False
    last_digit = None
    for digit in digits:
        if last_digit is None:
            last_digit = int(digit)
            continue
        if abs(last_digit - int(digit)) not in range(1, 4):
            return False
        last_digit = int(digit)
    return True


def damper(digits):
    print("-" * 40)
    states = []
    print(digits)
    states.append(is_safe(digits))
    for i in range(len(digits)):
        new_digits = [j for idx, j in enumerate(digits) if i != idx]
        states.append(is_safe(new_digits))
        print(f"{new_digits=}, {states[-1]=}")
    return True in states


def run(data: str) -> Solution:
    lines = data.split("\n")
    count = 0
    count2 = 0
    for line in lines:
        count = count + 1 if is_safe(line.split(" ")) else count
        count2 = count2 + 1 if damper(line.split(" ")) else count2
    return (count, count2)
