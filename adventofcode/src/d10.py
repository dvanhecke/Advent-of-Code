"""
Solution for day 10 of the 2024 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution 10` from the project root.
"""

from adventofcode.types import Solution
from collections import deque
from tqdm import tqdm

def bfs(grid, start):
    rows, cols = len(grid), len(grid[0])  # Dimensions of the grid
    visited = set()  # To track visited positions
    queue = deque([start])  # Initialize the queue with the starting position
    reachable_nines = set()  # To store reachable positions with height 9

    while queue:
        r, c = queue.popleft()  # Dequeue a position
        if (r, c) in visited:
            continue
        visited.add((r, c))  # Mark as visited
        
        # Check if current position is height 9
        if grid[r][c] == 9:
            reachable_nines.add((r, c))
        
        # Explore neighbors (up, down, left, right)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:  # Check bounds
                if grid[nr][nc] == grid[r][c] + 1:  # Check valid step
                    queue.append((nr, nc))  # Add valid neighbor to the queue

    return len(reachable_nines)  # Return the count of reachable 9s

def dfs(grid, r, c, memo):
    rows, cols = len(grid), len(grid[0])
    
    # If we've already calculated the result for this cell, return it
    if (r, c) in memo:
        return memo[(r, c)]

    # If the current cell is height 9, this is the end of a trail
    if grid[r][c] == 9:
        return 1

    total_trails = 0

    # Explore all valid neighbors (up, down, left, right)
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:  # Check bounds
            if grid[nr][nc] == grid[r][c] + 1:  # Check for valid height increment
                total_trails += dfs(grid, nr, nc, memo)  # Recursive exploration

    # Store the result in the memoization table and return it
    memo[(r, c)] = total_trails
    return total_trails

def get_trailheads(grid):
    trailheads = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                trailheads.append((row, col))
    return trailheads

def part1(grid):
    total_score = 0
    for trailhead in tqdm(get_trailheads(grid), desc="searching paths", unit="trailhead"):
        total_score += bfs(grid, trailhead)
    return total_score


def part2(grid):
    memo = {}  # Memoization table
    total_rating = 0

    for (r, c) in tqdm(get_trailheads(grid), desc="searching paths", unit="trailhead"):
        total_rating += dfs(grid, r, c, memo)

    return total_rating

def run(data: str) -> Solution:
    grid = [list(map(int, line)) for line in data.splitlines()]
    return (part1(grid), part2(grid))
