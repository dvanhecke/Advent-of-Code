from collections import defaultdict
import os

# for downloading puzzle inputs
AOC_URL = "https://adventofcode.com"
USER_AGENT = "advent_of_code_python_input_downloader_dvanhecke"

SRC_DIR_NAME = "src"
PROJECT_ROOT = os.path.dirname(__file__)
TESTS_ROOT = os.path.join(PROJECT_ROOT, "tests")
SOLUTIONS_ROOT = os.path.join(PROJECT_ROOT, SRC_DIR_NAME)
INPUTS_ROOT = os.path.join(PROJECT_ROOT, "inputs")
USER_SESSION_ID_FILE_PATH = os.path.join(PROJECT_ROOT, ".USER_SESSION_ID")

COMMAND_RUN_SOLUTION = "run_solution"
COMMAND_MAKE_NEW_YEAR = "run_make_new_year"

DAY_PREFIX = "d"

YEAR = os.getenv("YEAR")

# starter file templates
SOLUTION_FILE_TEMPLATE = f'''"""
Solution for day {{day}} of the {{year}} Advent of Code calendar.
Run it with the command `python -m adventofcode {COMMAND_RUN_SOLUTION} {{day}}` from the project root.
"""
from adventofcode.types import Solution

def run(data: str) -> Solution:
  # not yet implemented!
  return (None, None)
'''

TEST_FILE_TEMPLATE = f'''"""
Test for year {{year}}, day {{day}} solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
"""
import pytest
from adventofcode.{SRC_DIR_NAME}.{DAY_PREFIX}{{zero_padded_day}} import run

def test_run() -> None:
  # not yet implemented!
  assert benchmark(run, test_data) == (None, None)
'''

# for highlighting sections of printed text
MARKS = defaultdict(
    lambda: "\033[1;34m",
    {"b": "\033[1;34m", "g": "\033[1;32m", "y": "\033[1;33m", "r": "\033[1;31m"},
)
END_MARK = "\033[0m"
