import importlib
import cProfile
import pstats
from adventofcode.util import (
    get_day_id,
    get_input,
    highlight,
)
from adventofcode.constants import YEAR


def run_profiler(args) -> None:
    day = args.day
    solution_module_path = f"adventofcode.src.{get_day_id(day)}"
    solution_module = importlib.import_module(solution_module_path)
    data = get_input(YEAR, day)
    print(
        f"Running profiler on the solution for year {highlight(YEAR)}, day {highlight(day)}."
    )
    print()
    profiler = cProfile.Profile()

    # Start profiling
    profiler.enable()

    # Solve the puzzle
    result = solution_module.run(data)

    # Stop profiling
    profiler.disable()
    print()
    print(highlight("Solutions found.", color="g"))
    print()
    print("Answer to puzzle 1:", highlight(result[0], color="g"))
    print("Answer to puzzle 2:", highlight(result[1], color="g"))
    stats = pstats.Stats(profiler)
    stats.sort_stats("time").print_stats(10)  # Adjust the number to show more/less
