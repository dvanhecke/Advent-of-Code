"""
Solution for day 15 of the 2024 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution 15` from the project root.
"""

from adventofcode.types import Solution
from collections import defaultdict

DIRECTIONS = {
    "<": (0, -1),
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
}

BOX_SYMBOL = "O"
WALL_SYMBOL = "#"
BOT_SYMBOL = "@"

def parse_input(data) -> (list, list):
    grid = [[char for char in line] for line in data.split("\n\n")[0].splitlines()]
    moves = [char for char in data.split("\n\n")[1].replace("\n", "")]
    return grid, moves

def calc_sum(grid):
    total = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != BOX_SYMBOL:
                continue
            total += 100 * row + col
    return total


def find_bot(grid):
    for idx, row in enumerate(grid):
        try:
            col = row.index(BOT_SYMBOL)
            return idx, col
        except ValueError:
            continue


def move_bot(grid, moves):
    row, col = find_bot(grid)
    _grid = [row[:] for row in grid]

    for move in moves:
        dr, dc = DIRECTIONS[move]
        if _grid[row + dr][col + dc] == WALL_SYMBOL:
            continue
        if _grid[row + dr][col + dc] == BOX_SYMBOL:
            chain_positions = [(row + dr, col + dc)]
            while True:
                next_r, next_c = chain_positions[-1][0] + dr, chain_positions[-1][1] + dc
                if _grid[next_r][next_c] == WALL_SYMBOL:
                    valid_chain = False
                    break
                elif _grid[next_r][next_c] == BOX_SYMBOL:
                    chain_positions.append((next_r, next_c))
                else:
                    valid_chain = True
                    break
            if not valid_chain:
                continue
            chain_positions.reverse()
            for r_box, c_box in chain_positions:
                _grid[r_box + dr][c_box + dc] = BOX_SYMBOL
                _grid[r_box][c_box] = '.'
            _grid[row][col] = '.'
            _grid[row +dr][col + dc] = BOT_SYMBOL
            row, col = row + dr, col + dc
        else:
            _grid[row][col] = '.'
            _grid[row + dr][col + dc] = BOT_SYMBOL
            row, col = row + dr, col + dc

    return _grid


def move_bot2(grid, bot_moves):
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in reversed(range(n)):
            if grid[i][j] == '#':
                grid[i].insert(j, '#')
            if grid[i][j] == '.':
                grid[i].insert(j, '.')
            if grid[i][j] == '@':
                robot = (i, j*2)
                grid[i][j:j+1] = ['.', '.']
            if grid[i][j] == 'O':
                grid[i][j:j+1] = ['[', ']']

    for d in bot_moves[:]:
        i, j = robot
        
        if d == '<':
            k = j-1
            while grid[i][k] == ']':
                k -= 2
            if grid[i][k] == '.':
                for l in range(k, j):
                    grid[i][l] = grid[i][l+1]
                robot = (i, j-1)

        elif d == '>':
            k = j+1
            while grid[i][k] == '[':
                k += 2
            if grid[i][k] == '.':
                for l in reversed(range(j+1, k+1)):
                    grid[i][l] = grid[i][l-1]
                robot = (i, j+1)

        elif d == '^':
            queue = {(i-1, j)}
            rows = defaultdict(set)
            while queue:
                x, y = queue.pop()
                match grid[x][y]:
                    case '#':
                        break
                    case ']':
                        rows[x] |= {y-1, y}
                        queue |= {(x-1, y), (x-1, y-1)}
                    case '[':
                        rows[x] |= {y, y+1}
                        queue |= {(x-1, y), (x-1, y+1)}
                    case '.':
                        rows[x].add(y)
            else:
                for x in sorted(rows):
                    for y in rows[x]:
                        grid[x][y] = grid[x+1][y] if y in rows[x+1] else '.'
                robot = (i-1, j)

        elif d== 'v':
            queue = {(i+1, j)}
            rows = defaultdict(set)
            while queue:
                x, y = queue.pop()
                match grid[x][y]:
                    case '#':
                        break
                    case ']':
                        rows[x] |= {y-1, y}
                        queue |= {(x+1, y), (x+1, y-1)}
                    case '[':
                        rows[x] |= {y, y+1}
                        queue |= {(x+1, y), (x+1, y+1)}
                    case '.':
                        rows[x].add(y)
            else:
                for x in sorted(rows, reverse=True):
                    for y in rows[x]:
                        grid[x][y] = grid[x-1][y] if y in rows[x-1] else '.'
                robot = (i+1, j)

    total = 0
    for i in range(m):
        for j in range(n*2):
            if grid[i][j] == '[':
                total += 100*i + j

    return total


def run(data: str) -> Solution:
    grid, moves = parse_input(data)
    new_grid = move_bot(grid, moves)
    return (calc_sum(new_grid), move_bot2(grid, moves))
