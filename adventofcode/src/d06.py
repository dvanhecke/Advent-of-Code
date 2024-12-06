from adventofcode.types import Solution
from concurrent.futures import ProcessPoolExecutor

DIRECTIONS = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1)
}

def move(grid, guard_row, guard_col, direction):
    offsets = DIRECTIONS[direction]
    new_row = guard_row + offsets[0]
    new_col = guard_col + offsets[1]
    
    # Check if the new position is within bounds
    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
        while grid[new_row][new_col] == "#":  # Obstacle encountered
            direction = rotate(direction)  # Rotate the direction
            offsets = DIRECTIONS[direction]
            new_row = guard_row + offsets[0]
            new_col = guard_col + offsets[1]
        # Mark the current position as visited
        grid[guard_row][guard_col] = "X"
        grid[new_row][new_col] = "^"
        return new_row, new_col, direction
    return None  # No valid move

def rotate(direction):
    # Rotate clockwise in the direction list
    keys = list(DIRECTIONS.keys())
    key_index = keys.index(direction)
    if key_index == 3:
        return keys[0]
    return keys[key_index + 1]

def find_guard(grid):
    for row, line in enumerate(grid):
        for col, element in enumerate(line):
            if element == "^":  # Find the starting position of the guard
                return row, col
    return None

def search_loops(params):
    """
    Optimized function to detect loops in a grid-based simulation.
    """
    grid, start_row, start_col, row_, col_ = params
    loop_points = 0

    # Place the obstacle at the specified position
    grid[row_][col_] = "#"

    # State tracking: use a set for O(1) lookup
    visited_states = set()
    start_direction = "up"
    direction = start_direction
    row, col = start_row, start_col

    while True:
        # Calculate the next move
        coords = move(grid, row, col, direction)
        if coords is None:
            break  # Exit simulation if no valid movement is possible

        # Unpack new position and direction
        row, col, direction = coords

        # Check for loops
        state = (row, col, direction)
        if state in visited_states:
            # Loop detected
            loop_points += 1
            break
        visited_states.add(state)

    # Restore the grid after search
    grid[row_][col_] = "."
    return loop_points

# Main function to parallelize across grid cells
def parallel_search_loops(grid, start_row, start_col):
    num_rows = len(grid)
    num_cols = len(grid[0])

    # Create tasks: each task corresponds to a grid cell
    tasks = [
        (grid, start_row, start_col, row_, col_)
        for row_ in range(num_rows)
        for col_ in range(num_cols)
    ]

    # Use ProcessPoolExecutor to parallelize
    with ProcessPoolExecutor() as executor:
        results = executor.map(search_loops, tasks)

    # Sum results from all tasks
    total_loop_points = sum(results)
    print(f"Total loop points: {total_loop_points}")
    return total_loop_points

def run(data: str) -> Solution:
    grid = [list(line) for line in data.split("\n")]
    grid_ = grid.copy()
    start_direction = "up"
    start_row, start_col = find_guard(grid_)

    # Part 1: Count distinct visited positions
    direction = start_direction
    row, col = start_row, start_col
    run_simulation = True

    while run_simulation:
        coords = move(grid_, row, col, direction)
        if coords is None:
            run_simulation = False
            continue
        row, col, direction = coords

    # Count visited positions
    count = sum(line.count("X") for line in grid) + 1  # Add 1 for the starting position
    total_loops = parallel_search_loops(grid, start_row, start_col)
    return (count, total_loops)
