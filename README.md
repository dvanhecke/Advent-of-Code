# Advent of Code solutions

this project holds python solutions + utilities for [Advent of Code](https://adventofcode.com) puzzles over the years.
Organized in branches

## Run it

This project uses pipenv as a virtual environment to start using:

* edit `.env` `YEAR`key to the current year
* run:
    ```sh
    pipenv install # install the environment
    pipenv shell # starts a new shell within the environment, can be exited normally, with `exit` or Ctrl-D.
    python -m adventofcode init
    ```

Once that's done, run solutions like:

```sh
python -m adventofcode run <day>
```

## Test it

Assuming you've installed dependencies as described above, you can run tests with the following:

```sh
# run all tests
PYTHONPATH=$(pwd) py.test
# run a specific test
PYTHONPATH=$(pwd) py.test path/to/test.py
```

