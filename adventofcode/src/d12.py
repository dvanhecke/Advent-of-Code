"""
Solution for day 12 of the 2024 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution 12` from the project root.
"""

from adventofcode.types import Solution
from collections import defaultdict


def parse_input(input_string):
    return [list(row) for row in input_string.split("\n")]


def find_regions(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    regions = []

    def flood_fill(r, c, plant_type):
        # DFS or BFS to explore a region
        stack = [(r, c)]
        region_cells = []
        while stack:
            x, y = stack.pop()
            if visited[x][y]:
                continue
            visited[x][y] = True
            region_cells.append((x, y))
            # Check neighbors
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < rows
                    and 0 <= ny < cols
                    and not visited[nx][ny]
                    and grid[nx][ny] == plant_type
                ):
                    stack.append((nx, ny))
        return region_cells

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                plant_type = grid[r][c]
                region_cells = flood_fill(r, c, plant_type)
                regions.append(region_cells)

    return regions


def find_sides(region: set[tuple[int, int]]):
    # a dict that holds all region points at the edge of the region
    # for each possible x or y value
    # for each possible side (left = 0, right = 1, up = 2, down = 3)
    sides: dict[tuple[int, int], set[tuple[int, int]]] = defaultdict(set)
    # for all points in the region
    for x, y in region:
        # check all neighbours
        vertical_left = (x - 1, y)
        vertical_right = (x + 1, y)
        horizontal_up = (x, y - 1)
        horizontal_down = (x, y + 1)
        # if the neighbour is not in the region, this point is part of the edge
        # and we add it to the sides dict
        # in this case, it is the left side, so the key is (x, 0)
        if vertical_left not in region:
            sides[(x, 0)].add((x, y))
        # in this case, it is the right side, so the key is (x, 1)
        if vertical_right not in region:
            sides[(x, 1)].add((x, y))
        # in this case, it is the up side, so the key is (y, 2)
        if horizontal_up not in region:
            sides[(y, 2)].add((x, y))
        # in this case, it is the down side, so the key is (y, 3)
        if horizontal_down not in region:
            sides[(y, 3)].add((x, y))
    # count the number of sides
    side_count = 0
    # for each possible x or y value and side direction that sides exist (left, right, up, down)
    for section in sides.values():
        # holds all visited points in this section
        visited: set[tuple[int, int]] = set()
        # for each point in the section
        for x, y in section:
            # if the point was not visited yet, we start a bfs from this point
            # to add all connected points to the visited set
            if (x, y) not in visited:
                grow_section(x, y, section, visited)
                # and increase the side count
                side_count += 1
    return side_count


def grow_section(
    x: int, y: int, section: set[tuple[int, int]], visited: set[tuple[int, int]]
):
    # normal bfs start from the current point
    stack: list[tuple[int, int]] = [(x, y)]
    # while there are points to visit
    while stack:
        # get the next point
        x, y = stack.pop()
        # check all neighbours
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            new_x, new_y = x + dx, y + dy
            # if the point is out of bounds, skip it
            if (new_x, new_y) not in section:
                continue
            # if the point was already visited, skip it
            if (new_x, new_y) in visited:
                continue
            # add the point to the stack and the visited points
            stack.append((new_x, new_y))
            visited.add((new_x, new_y))


def expand_region(
    grid: list[list[str]], x: int, y: int, visited_points: set[tuple[int, int]]
):
    # normal bfs start from the current point
    stack: list[tuple[int, int]] = [(x, y)]
    # later used to determine the number of sides
    region: set[tuple[int, int]] = set([(x, y)])
    # identifing flower type, that needs to be the same in the region
    region_flower = grid[y][x]
    # we annoted this point as being visited
    visited_points.add((x, y))
    # while there are points to visit
    while stack:
        # get the next point
        x, y = stack.pop()
        # check all neighbours
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            new_x, new_y = x + dx, y + dy
            # if the point is out of bounds, skip it
            if new_x < 0 or new_x >= len(grid[0]) or new_y < 0 or new_y >= len(grid):
                continue
            # if the point is not the same flower type, skip it
            if grid[new_y][new_x] != region_flower:
                continue
            # if the point was already visited, skip it
            if (new_x, new_y) in visited_points:
                continue
            # add the point to the stack and the visited points
            stack.append((new_x, new_y))
            visited_points.add((new_x, new_y))
            region.add((new_x, new_y))
    # return the size of the region and the number of sides
    return len(region), find_sides(region)


def calculate_area_and_perimeter(region, grid):
    area = len(region)
    perimeter = 0
    for x, y in region:
        # Check all 4 sides
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (
                not (0 <= nx < len(grid) and 0 <= ny < len(grid[0]))
                or grid[nx][ny] != grid[x][y]
            ):
                perimeter += 1
    return area, perimeter


def calculate_total_price(grid):
    regions = find_regions(grid)
    total_price = 0
    for region in regions:
        area, perimeter = calculate_area_and_perimeter(region, grid)
        total_price += area * perimeter
    return total_price


def calculate_price_bulk(grid):
    width = len(grid[0])
    height = len(grid)

    visited_points: set[tuple[int, int]] = set()
    total = 0
    # for all points in the grid
    for y in range(height):
        for x in range(width):
            # if we already used this point in a region, there needs to be no bfs from this point
            if (x, y) in visited_points:
                continue
            # get the side count and size of the region
            side_count, size = expand_region(grid, x, y, visited_points)
            total += side_count * size
    return total


def run(data: str) -> Solution:
    grid = parse_input(data)
    return (calculate_total_price(grid), calculate_price_bulk(grid))
