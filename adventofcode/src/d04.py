"""
Solution for day 4 of the 2024 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution 4` from the project root.
"""

from adventofcode.types import Solution

def count_xmas_x(grid):
    # Get the dimensions of the grid
    rows = len(grid) - 1
    cols = len(grid[0]) - 1
    count = 0

    for row in range(1, rows):
        for col in range(1, cols):
            if grid[row][col] == "A":
                arm1 = "".join([grid[row - 1][col - 1], grid[row][col], grid[row + 1][col + 1]])
                arm2 = "".join([grid[row - 1][col + 1], grid[row][col], grid[row + 1][col - 1]])
                if (arm1 == "MAS" or arm1 == "SAM") and (arm2 == "MAS" or arm2 == "SAM"):
                    count += 1

    return count


def run(data) -> Solution:
    grid = data.split("\n")
    rows = len(grid)
    cols = len(grid[0])

    # Directions to check: (row_offset, col_offset)
    directions = [
        (0, 1),   # Horizontal right
        (0, -1),  # Horizontal left
        (1, 0),   # Vertical down
        (-1, 0),  # Vertical up
        (1, 1),   # Diagonal down-right
        (-1, -1), # Diagonal up-left
        (1, -1),  # Diagonal down-left
        (-1, 1)   # Diagonal up-right
    ]

    # Initialize the count of occurrences
    xmas_count = 0

    # Function to check if "XMAS" can be found starting at (r, c) in a specific direction
    def check_direction(r, c, dr, dc):
        word = "XMAS"
        for i in range(4):  # We want to check 4 characters (X, M, A, S)
            nr = r + dr * i
            nc = c + dc * i
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != word[i]:
                return False
        return True

    # Iterate over each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # For each starting point (r, c), check all directions
            if grid[r][c] == 'X':
                for dr, dc in directions:
                    if check_direction(r, c, dr, dc):
                        xmas_count += 1

    return xmas_count, count_xmas_x(grid)
