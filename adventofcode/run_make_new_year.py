import os
import shutil
import subprocess
from datetime import date
from typing import Tuple
from adventofcode.constants import (
    SOLUTIONS_ROOT,
    TESTS_ROOT,
    SOLUTION_FILE_TEMPLATE,
    TEST_FILE_TEMPLATE,
    YEAR,
)
from adventofcode.util import get_day_id, pad_day, highlight


def make_new_year(year: int) -> Tuple[str, str]:
    """
    Sets up solution and test directories for a new year of puzzle solutions.
    Only fails if the files already exist. Pre-existing directories are A-OK.
    """
    solutions_year_dir_path = SOLUTIONS_ROOT
    tests_year_dir_path = TESTS_ROOT
    os.makedirs(solutions_year_dir_path, exist_ok=True)
    os.makedirs(tests_year_dir_path, exist_ok=True)

    for day in range(1, 26):
        day_id = get_day_id(day)
        solution_file_path = os.path.join(solutions_year_dir_path, f"{day_id}.py")
        with open(solution_file_path, "x") as solution_file:
            solution_file.write(SOLUTION_FILE_TEMPLATE.format(day=day, year=year))

        # test file names must be unique for pytest to run them correctly
        test_file_path = os.path.join(
            tests_year_dir_path, f"test_{year}_{pad_day(day)}.py"
        )
        with open(test_file_path, "x") as test_file:
            test_file.write(
                TEST_FILE_TEMPLATE.format(
                    day=day, year=year, zero_padded_day=pad_day(day)
                )
            )
    return (solutions_year_dir_path, tests_year_dir_path)


def run_make_new_year(args) -> None:
    paths = make_new_year(YEAR)

    print(highlight("Success.", color="g"))
    if shutil.which("tree") is not None:
        trees = "\n".join(
            subprocess.check_output(["tree", "-C", "--noreport", path]).decode("utf8")
            for path in paths
        )
        print("Created the following directories and files:")
        print(trees)
    else:
        solutions_year_dir_path, tests_year_dir_path = paths
        print(
            f"Created solution directory {highlight(solutions_year_dir_path)} and starter solution files."
        )
        print(
            f"Created test directory {highlight(tests_year_dir_path)} and starter test files."
        )
