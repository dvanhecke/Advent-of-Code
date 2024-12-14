"""
Solution for day 13 of the 2024 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution 13` from the project root.
"""

from adventofcode.types import Solution
import re


def parse_input(data: str):
    """
    {
        "A": (DX, DY),
        "B": (DX, DY),
        "P": (X, Y)
    }
    """
    split = data.splitlines()
    parsed_data = []
    for i in range(0, len(split), 4):
        dictionary = dict()
        dictionary["A"] = tuple(map(int, split[i].removeprefix("Button A: ").replace("X+", "").replace("Y+", "").split(", ")))
        dictionary["B"] = tuple(map(int, split[i + 1].removeprefix("Button B: ").replace("X+", "").replace("Y+", "").split(", ")))
        dictionary["P"] = tuple(map(int, split[i + 2].removeprefix("Prize: ").replace("X=", "").replace("Y=", "").split(", ")))
        parsed_data.append(dictionary)
    return parsed_data


def find_min_cost(A, B, P, max_presses=100):
    A_x, A_y = A
    B_x, B_y = B
    P_x, P_y = P
    
    min_cost = float("inf")
    found_solution = False

    # Brute force over all possible presses of A and B
    for a in range(max_presses + 1):
        for b in range(max_presses + 1):
            if A_x * a + B_x * b == P_x and A_y * a + B_y * b == P_y:
                cost = 3 * a + b
                min_cost = min(min_cost, cost)
                found_solution = True
    
    return min_cost if found_solution else None


def part1(machines):
    total_cost = 0

    for machine in machines:
        A = machine["A"]
        B = machine["B"]
        C = machine["P"]
        
        cost = find_min_cost(A, B, C)
        if cost is not None:
            total_cost += cost
    return total_cost


def part2(puzzle_input):
    total = 0
    tolerance = 0.0001
    offset = 10_000_000_000_000
    for machine in puzzle_input.split('\n\n'):
        ax, ay, bx, by, x, y = map(int, re.findall(r'(\d+)', machine))
        x += offset
        y += offset
        A = (bx*y - by*x) / (bx*ay - by*ax)
        B = (x-ax*A) / bx
        if abs(A - round(A)) < tolerance and abs(B - round(B)) < tolerance:
            total += 3*A + B

    return int(total)

def run(data: str) -> Solution:
    machines = parse_input(data)
    return (part1(machines), part2(data))
