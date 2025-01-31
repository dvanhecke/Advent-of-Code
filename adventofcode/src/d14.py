"""
Solution for day 14 of the 2024 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution 14` from the project root.
"""

from adventofcode.types import Solution
import re
from statistics import variance as var


def parse_input(data):
    return [[int(n) for n in re.findall(r"-?\d+", item)] for item in data.splitlines()]


def part1(bots, size: tuple[int], offset=100):
    w, h = size
    grid = [[0 for _ in range(w)] for _ in range(h)]
    for bot in bots:
        x, y, vx, vy = bot
        new_x = (x + (offset * vx)) % w
        new_y = (y + (offset * vy)) % h
        grid[new_y][new_x] += 1

    q1 = sum(
        grid[y][x]
        for y in range(0, h // 2)
        for x in range(0, w // 2)
        if x != w // 2 and y != h // 2
    )
    q2 = sum(
        grid[y][x]
        for y in range(0, h // 2)
        for x in range(w // 2, w)
        if x != w // 2 and y != h // 2
    )
    q3 = sum(
        grid[y][x]
        for y in range(h // 2, h)
        for x in range(0, w // 2)
        if x != w // 2 and y != h // 2
    )
    q4 = sum(
        grid[y][x]
        for y in range(h // 2, h)
        for x in range(w // 2, w)
        if x != w // 2 and y != h // 2
    )

    return q1 * q2 * q3 * q4


def part2(bots, size):
    W, H = size
    bx = min(range(W), key=lambda t: var((s + t * v) % W for (s, _, v, _) in bots))
    by = min(range(H), key=lambda t: var((s + t * v) % H for (_, s, _, v) in bots))
    return bx + ((pow(W, -1, H) * (by - bx)) % H) * W


def run(data: str, test=False) -> Solution:
    bots = parse_input(data)
    return (
        part1(bots, (11, 7) if test else (101, 103)),
        part2(bots, (11, 7) if test else (101, 103)),
    )
