"""
Solution for dacol 16 of the 2024 Advent of Code calendar.
Run it with the command `pcolthon -m adventofcode run_solution 16` from the project root.
"""

from adventofcode.types import Solution
import heapq


END = "E"
START = "S"
WALL = "#"

DIRECTIONS = {"l": (0, -1), "u": (-1, 0), "r": (0, 1), "d": (1, 0)}


def find_char(grid, char):
    for x, row in enumerate(grid):
        for y, _char in enumerate(row):
            if _char == char:
                return (x, y)


def parse_data(data):
    return [list(row) for row in data.splitlines()]


def rotate(current_dir, rotation):
    keys = list(DIRECTIONS.keys())
    idx = keys.index(current_dir)
    if rotation == "CW":  # Clockwise rotation
        return keys[(idx + 1) % 4]
    elif rotation == "CCW":  # Counterclockwise rotation
        return keys[(idx - 1) % 4]


def heuristic(pos, target):
    # Manhattan distance heuristic
    return abs(pos[0] - target[0]) + abs(pos[1] - target[1])


def find_lowest_score(grid, start, end):
    start_state = (start[0], start[1], "r")  # Starting position and facing right
    pq = []
    heapq.heappush(pq, (0, start_state))  # Priority queue: (cost, (x, y, direction))
    visited = set()

    while pq:
        cost, (x, y, facing) = heapq.heappop(pq)

        # Check if we've reached the end
        if (x, y) == end:
            return cost

        # Skip if already visited
        if (x, y, facing) in visited:
            continue
        visited.add((x, y, facing))

        # Move forward
        dx, dy = DIRECTIONS[facing]
        nx, ny = x + dx, y + dy
        if grid[nx][ny] != WALL:
            heapq.heappush(pq, (cost + 1, (nx, ny, facing)))

        # Rotate clockwise and counterclockwise
        for rotation in ["CW", "CCW"]:
            new_facing = rotate(facing, rotation)
            heapq.heappush(pq, (cost + 1000, (x, y, new_facing)))

    return float("inf")  # If no path is found


def run(data: str) -> Solution:
    grid = parse_data(data)
    start = find_char(grid, START)
    end = find_char(grid, END)
    lowest_score = find_lowest_score(grid, start, end)
    return (lowest_score, None)
