"""
Solution for day 11 of the 2024 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution 11` from the project root.
"""

from adventofcode.types import Solution
from collections import defaultdict

def simulate_blinks(stones: list[int], blinks: int) -> int:
    stone_counts = defaultdict(int)
    for stone in stones:
        stone_counts[stone] += 1

    for _ in range(blinks):
        new_stone_counts = defaultdict(int)

        for stone, count in stone_counts.items():
            if stone == 0:
                new_stone_counts[1] += count
            elif len(str(stone)) % 2 == 0:
                digits = str(stone)
                half = len(digits) // 2
                left, right = int(digits[:half]), int(digits[half:])
                new_stone_counts[left] += count
                new_stone_counts[right] += count
            else:
                new_stone_counts[stone*2024] += count
        stone_counts = new_stone_counts
    return sum(stone_counts.values())

def part2(stones):
    return simulate_blinks(stones, 75)
def part1(stones):
    return simulate_blinks(stones, 25)


def run(data: str) -> Solution:
    stones = [int(element) for element in "".join(data.splitlines()).split(" ")]
    return (part1(stones), part2(stones))
