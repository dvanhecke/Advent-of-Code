from adventofcode.types import Solution
from concurrent.futures import ProcessPoolExecutor, as_completed
from rich.table import Table
from rich.live import Live
from tqdm import tqdm

DIRECTIONS = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}

DIRECTION_SYMBOLS = {"up": "^", "right": ">", "down": "v", "left": "<"}


def get_zoomed_region(grid, bot_row, bot_col, size=50):
    start_row = max(0, bot_row - size // 2)
    start_col = max(0, bot_col - size // 2)
    end_row = min(len(grid), bot_row + size // 2 + 1)
    end_col = min(len(grid[0]), bot_col + size // 2 + 1)

    # Ensure the region is exactly `size` x `size`
    if end_row - start_row < size:
        start_row = max(0, end_row - size)
    if end_col - start_col < size:
        start_col = max(0, end_col - size)

    # Extract the region from the grid
    zoomed_region = [row[start_col:end_col] for row in grid[start_row:end_row]]
    return zoomed_region


def visualize_grid_in_cli(grid, bot_row, bot_col):
    zoomed_region = get_zoomed_region(grid, bot_row, bot_col)
    table = Table(title="Guard patrolling the lab", box=None, pad_edge=False)
    for row in zoomed_region:
        cells = []
        for col, cell in enumerate(row):
            if cell == ".":
                cells.append(" ")  # Free cell
            elif cell == "#":
                cells.append("[bold red]󰝤[/]")  # Obstacle
            elif cell in DIRECTION_SYMBOLS.values():
                cells.append(f"[green]{cell}[/]")  # Bot
            elif cell == "X":
                cells.append("[yellow]X[/]")  # Trail
        table.add_row(*cells)
    return table


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
        grid[new_row][new_col] = DIRECTION_SYMBOLS[direction]
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
    total_loop_points = 0
    with ProcessPoolExecutor() as executor:
        # Use submit to submit each task to the executor
        futures = {executor.submit(search_loops, task): task for task in tasks}

        # Initialize the progress bar
        with tqdm(
            total=len(futures), desc="Checking infinite loops", unit="grid checks"
        ) as pbar:
            for future in as_completed(futures):
                loop_points = future.result()
                total_loop_points += loop_points
                pbar.update(1)  # Update the progress bar as tasks complete

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

    with Live(visualize_grid_in_cli(grid_, row, col), refresh_per_second=1000) as live:
        while run_simulation:
            coords = move(grid_, row, col, direction)
            if coords is None:
                run_simulation = False  # Exit the loop when no valid move is possible
                continue
            row, col, direction = coords
            # Visualize the zoomed-in grid
            current_table = visualize_grid_in_cli(grid_, row, col)
            live.update(current_table)

    # Count visited positions
    count = sum(line.count("X") for line in grid) + 1  # Add 1 for the starting position
    total_loops = parallel_search_loops(grid, start_row, start_col)
    return (count, total_loops)
