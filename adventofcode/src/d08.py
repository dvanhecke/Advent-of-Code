"""
Solution for day 8 of the 2024 Advent of Code calendar.
Run it with the command python -m adventofcode run_solution 8 from the project root.
"""

from adventofcode.types import Solution


def is_on_same_diagonal(r1, c1, r2, c2):
    # To handle divide by zero errors, ensure c1 != c2 (or r1 != r2)
    if c2 - c1 == 0:
        return r2 - r1 != 0  # Same column but different rows (vertical line)
    
    # Calculate the difference in rows and columns
    dr = r2 - r1
    dc = c2 - c1
    
    # Check if the slope (dr / dc) is the same for both points
    return dr * dc == (r2 - r1) * (c2 - c1)

def calculate_distance(r1, c1, r2, c2):
    row_offset = r2 - r1
    col_offset = c2 - c1
    return [(row_offset, col_offset), (row_offset * -1, col_offset * -1)]


def count_antinode_locations(grid):
    antennas = []
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val != '.':
                antennas.append((r, c, val))  # Store row, col, and frequency

    rows = len(grid)
    cols = len(grid[0])
    grid_ = [row[:] for row in grid]
    grid__ = [row[:] for row in grid]
    for i, (r1, c1, freq1) in enumerate(antennas):
        for j, (r2, c2, freq2) in enumerate(antennas):
            if i == j or freq1 != freq2:
                continue
            if r1 != r2 and c1 != c2 and not is_on_same_diagonal(r1, c1, r2, c2):
                continue
            dist = calculate_distance(r1, c1, r2, c2)
            new_row, new_col = r1+dist[0][0], c1+dist[0][1]
            if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col, freq1) not in antennas:
                grid_[new_row][new_col] = "#"
            r, c = r1, c1
            row_step, col_step = new_row - r1, new_col - c1
            while 0 <= r < rows and 0 <= c < cols:
                grid__[r][c] = "#"  # Mark as antinode
                r += row_step
                c += col_step

            new_row, new_col = r1+dist[1][0], c1+dist[1][1]
            if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col, freq1) not in antennas:
                grid_[new_row][new_col] = "#"
            r, c = r1, c1
            row_step, col_step = new_row - r1, new_col - c1
            while 0 <= r < rows and 0 <= c < cols:
                grid__[r][c] = "#"  # Mark as antinode
                r += row_step
                c += col_step
    print()
    for line in grid__:
        for char in line:
            print(char,end="")
        print()
    return sum([line.count("#") for line in grid_]), sum([line.count("#") for line in grid__])

def run(data: str) -> Solution:
    grid = [list(line) for line in data.split("\n")]
    return (count_antinode_locations(grid))
