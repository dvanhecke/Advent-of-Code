"""
Solution for day 9 of the 2024 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution 9` from the project root.
"""

from adventofcode.types import Solution
import sys
from heapq import heapify, heappop, heappush
from itertools import repeat


def part1(arr):
    disk = []
    is_file = True
    file_id = 0
    for size in arr:
        if is_file:
            disk.extend(repeat(file_id, size))
            file_id += 1
        else:
            disk.extend(repeat(-1, size))
        is_file = not is_file

    i, j = 0, len(disk) - 1

    while True:
        while disk[i] != -1:
            i += 1
        while disk[j] == -1:
            j -= 1
        if not i < j:
            break
        disk[i], disk[j] = disk[j], disk[i]
        i += 1
        j -= 1

    checksum = 0

    for file_position, file_id in enumerate(disk):
        if file_id != -1:
            checksum += file_position * file_id

    return checksum


def part2(arr):
    MAX_FREE_SIZE = 10

    files = []
    frees = [[] for _ in range(MAX_FREE_SIZE)]

    is_file = True
    file_id = 0
    position = 0
    for size in arr:
        if is_file:
            files.append((file_id, position, size))
            file_id += 1
        else:
            frees[size].append(position)
        is_file = not is_file
        position += int(size)

    for i in range(MAX_FREE_SIZE):
        frees[i].append(sys.maxsize)  # sentinel, make frees[i] always non-empty
        heapify(frees[i])

    compacted: list[tuple[int, int, int]] = []

    for file_id, file_position, file_size in reversed(files):
        first_fit: int | None = None

        for free_size in range(file_size, MAX_FREE_SIZE):
            if frees[free_size][0] < file_position and (
                first_fit is None or frees[free_size][0] < frees[first_fit][0]
            ):
                first_fit = free_size

        if first_fit is None:
            compacted.append((file_id, file_position, file_size))
            continue

        free_position = heappop(frees[first_fit])
        size_diff = first_fit - file_size
        compacted.append((file_id, free_position, file_size))
        heappush(frees[size_diff], free_position + file_size)

    checksum = 0

    for file_id, file_position, file_size in compacted:
        for position in range(file_position, file_position + file_size):
            checksum += position * file_id

    return checksum


def run(data: str) -> Solution:
    disk = part1([int(j) for j in "".join([i for i in data.splitlines()])])
    disk2 = part2([int(j) for j in "".join([i for i in data.splitlines()])])
    return disk, disk2
