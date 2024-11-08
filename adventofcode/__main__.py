import argparse
from adventofcode.constants import COMMAND_RUN_SOLUTION, COMMAND_MAKE_NEW_YEAR
from adventofcode.run_solution import run_solution
from adventofcode.run_make_new_year import run_make_new_year


parser = argparse.ArgumentParser(
    prog="python -m adventofcode",
    description="run Advent of Code solutions and utilities",
)
subparsers = parser.add_subparsers()

parser_run = subparsers.add_parser(
    COMMAND_RUN_SOLUTION,
    aliases=["run"],
    description="Run a solution.",
    help="Run a solution.",
)

parser_init = subparsers.add_parser(
    COMMAND_MAKE_NEW_YEAR,
    aliases=["init"],
    description="Set up input, solution, and test directories for a new year of solutions.",
    help="Set up input, solution, and test directories for a new year of solutions.",
)
parser_init.set_defaults(func=run_make_new_year)

parser_run.add_argument("day", type=int, help="Day of the solution.")
parser_run.set_defaults(func=run_solution)

args = parser.parse_args()
args.func(args)