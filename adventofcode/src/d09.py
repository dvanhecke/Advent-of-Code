"""
Solution for day 9 of the 2024 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution 9` from the project root.
"""

from adventofcode.types import Solution
from tqdm import tqdm

def parse_disk(disk):
    disk_ = []
    file_counter = 0
    for idx, val in enumerate(disk):
        if idx % 2 == 0:
            for _ in range(int(val)):
                disk_.append(str(file_counter))
            file_counter += 1
        else:
            for _ in range(int(val)):
                disk_.append(".")
    return disk_

def sort_disk(disk):
    original_disk = disk
    last_non_dot_index = len(original_disk) - 1

    for idx, char in enumerate(original_disk):
        if idx >= last_non_dot_index:  # If the index reaches or passes the last non-dot index, break
                    break
        if char != ".":
            continue
        while last_non_dot_index > idx and original_disk[last_non_dot_index] == ".":
            last_non_dot_index -= 1
        if last_non_dot_index > idx:
            original_disk[idx], original_disk[last_non_dot_index] = (
                original_disk[last_non_dot_index],
                original_disk[idx],
            )
    return original_disk

def calculate_checksum(disk):
    sum = 0
    for idx, val in enumerate(disk):
        if val == ".":
            continue
        sum += (int(idx) * int(val))

    return sum

def mv_file(file, disk):
    size_map = {}
    free_space_map = []
    free_space_index = None
    free_space_size = 0

    for idx, char in enumerate(disk):
        if char == ".":
            free_space_index = idx if free_space_index is None else free_space_index
            free_space_size +=1
            continue
        if free_space_index is not None:
            free_space_map.append((free_space_index, free_space_size))
            free_space_index = None
            free_space_size = 0

        if size_map.get(char) is None:
            size_map[char] = (disk.count(char), idx)

    for (idx, space) in free_space_map:
        if space >= size_map[file][0] and idx < size_map[file][1]:
            for i in range (idx, idx+size_map[file][0]):
                disk[i] = file
            for i in range(size_map[file][1], size_map[file][1]+size_map[file][0]):
                disk[i] = "."
            break

def defragment_disk(disk):
    disk_ = list(set(disk) - {"."})
    disk_.sort()
    for file in tqdm(disk_[::-1], desc="compacting", unit="file"):
        mv_file(file, disk)
    
    return disk

def run(data: str) -> Solution:
    disk = "".join([line for line in data.split("\n")])
    disk2 = "".join([line for line in data.split("\n")])
    disk = parse_disk(disk)
    disk2 = parse_disk(disk2)
    disk = sort_disk(disk)
    disk2 = defragment_disk(disk2)
    sum = calculate_checksum(disk)
    sum2 = calculate_checksum(disk2)
    return (sum, sum2)
