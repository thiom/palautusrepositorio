# AGENTS.md

A test-driven development (TDD) exercise: the `Ostoskori` (shopping cart) class is implemented one test at a time.

## Commands

The project is a uv project. Run all commands from the project root as `uv run ...`.

- Install dependencies: `uv sync`
- Run tests: `uv run pytest`
- Run a single test: `uv run pytest src/tests/ostoskori_test.py -k <test_name>`

## Structure

- `src/ostoskori.py`: the `Ostoskori` class being implemented; its methods are initially empty stubs
- `src/ostos.py`: `Ostos`, a single purchase of one product (product, quantity, price)
- `src/tuote.py`: `Tuote`, a product with a name and a price
- `src/tests/ostoskori_test.py`: unittest-style tests, run with pytest
- `src/index.py`: free scratch file for manual experiments

## Rules

- Tests executed with `uv run pytest`
- Code of `ostos.py` and `tuote.py` should not be changed
- Tests should not be edited unless explicitly asked
- Always implement absolutely minimal code that makes the tests pass
