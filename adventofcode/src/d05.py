"""
Solution for day 5 of the 2024 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution 5` from the project root.
"""

from collections import defaultdict, deque
from adventofcode.types import Solution


def sort(update, graph):
    subgraph = defaultdict(list)
    in_degree = defaultdict(int)
    for x in update:
        for y in graph[x]:
            if y in update:
                subgraph[x].append(y)
                in_degree[y] += 1
        if x not in in_degree:
            in_degree[x] = 0
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_update = []
    while queue:
        node = queue.popleft()
        sorted_update.append(node)
        for neighbor in subgraph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return sorted_update


def check_order(update, graph):
    index = {page: i for i, page in enumerate(update)}
    for x in graph:
        for y in graph[x]:
            if x in index and y in index and index[x] > index[y]:
                return False
    return True


def run(data: str) -> Solution:
    ruleset = [
        tuple([int(i) for i in rule.split("|")])
        for rule in data.split("\n\n")[0].split("\n")
    ]
    dataset = [
        [int(i) for i in line.split(",")]
        for line in data.split("\n\n")[1].split("\n")
        if line
    ]
    graph = defaultdict(list)
    for x, y in ruleset:
        graph[x].append(y)

    valid_updates = []
    invalid_updates = []
    for update in dataset:
        (
            valid_updates.append(update)
            if check_order(update, graph)
            else invalid_updates.append(update)
        )
    middle_sum = sum([update[len(update) // 2] for update in valid_updates])
    corrected_updates = [sort(update, graph) for update in invalid_updates]
    middle_sum_corrected = sum(
        [update[len(update) // 2] for update in corrected_updates]
    )
    return (middle_sum, middle_sum_corrected)
