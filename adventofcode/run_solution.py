import importlib
from adventofcode.util import (
    get_day_id,
    get_input,
    highlight,
)
from adventofcode.constants import YEAR


def run_solution(args) -> None:
    day = args.day
    solution_module_path = f"adventofcode.src.{get_day_id(day)}"
    solution_module = importlib.import_module(solution_module_path)
    data = get_input(YEAR, day)
    print(f"Running solution for year {highlight(YEAR)}, day {highlight(day)}.")
    print()
    answer1, answer2 = solution_module.run(data)
    print()
    print(highlight("Solutions found.", color="g"))
    print()
    print("Answer to puzzle 1:", highlight(answer1, color="g"))
    print("Answer to puzzle 2:", highlight(answer2, color="g"))
