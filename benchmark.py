import pytest
import importlib
from adventofcode.util import get_day_id, get_input, highlight
from adventofcode.constants import YEAR

# Load input data dynamically for each day
@pytest.mark.parametrize("day", range(1, 11))  # Parametrize for all days from 1 to 25
def test_benchmark_solution(benchmark, day):
    # Get the actual input data for the given day
    data = get_input(YEAR, day)
    
    solution_module_path = f"adventofcode.src.{get_day_id(day)}"
    solution_module = importlib.import_module(solution_module_path)
    
    print(f"Benchmarking solution for year {highlight(YEAR)}, day {highlight(day)}.")
    
    # Define the function to be benchmarked
    def run_solution():
        return solution_module.run(data)
    
    # Run the benchmark
    result = benchmark(run_solution)

    # Print the results
    print("\nBenchmark completed.")
    print(highlight("Solutions found.", color="g"))
    print(f"Answer to puzzle 1: {highlight(result[0], color='g')}")
    print(f"Answer to puzzle 2: {highlight(result[1], color='g')}")

