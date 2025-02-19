# CAT Test Framework - Python Version

This project implements the CAT (Continuous Alignment Testing) framework for Python, providing tools for recording and validating test experiments with confidence levels.

## Prerequisites

- Python 3.13 or higher
- [Poetry](https://python-poetry.org/) for dependency management

## Installation

1. Clone the repository

2. Install dependencies with Poetry:
   ```bash
   poetry install
   ```

## Development

### Running Tests

Run all tests:
```bash
poetry run pytest
```

Run tests with output:
```bash
poetry run pytest -v
```

### Code Quality

```bash
# Format code
poetry run black .

# Check style
poetry run flake8 src tests

# Type checking
poetry run mypy .
```

## Project Structure

- `src/cat_python/cat.py`: Main CAT implementation with core functionality
- `src/cat_python/db.py`: Database utilities and connection management
- `src/cat_python/types.py`: Shared type definitions and interfaces
- `tests/`: Test suite using pytest
  - `conftest.py`: Common test fixtures
  - `src/cat/test_cat.py`: Test implementations
- `pyproject.toml`: Project configuration and dependencies

## Implementation Notes

This is an alpha version converted from the TypeScript implementation. The main differences include:

- Use of Python's type hints instead of TypeScript types
- Async/await implementation using Python's native coroutines
- SQLite integration using Python's built-in sqlite3 module
- Testing with pytest instead of Jest
- Context managers for resource management
- Poetry for dependency management and project configuration


## How to Publish this Library

- set up your api key `poetry config pypi-token.pypi YOUR_PYPI_TOKEN`
- run `poetry publish --build`

## How to generate auto docs

- generate docs: `poetry run sphinx-apidoc -f -o source/ src/`
- build docs into github Pages jekyll: `poetry run sphinx-build -b html source ../../docs/api`