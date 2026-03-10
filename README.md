# swiffer 🧹

Clean Python project junk instantly.

`swiffer` is a lightweight CLI tool that removes common Python build and
cache files from a project directory.

## Install

``` bash
pip install swiffer
```

## Usage

Clean the current directory:

``` bash
swiffer
```

Clean a specific directory:

``` bash
swiffer path/to/project
```

Preview what would be removed:

``` bash
swiffer --dry
```

## What it removes

-   `__pycache__/`
-   `.pytest_cache/`
-   `.mypy_cache/`
-   `.ruff_cache/`
-   `dist/`
-   `build/`
-   `*.egg-info/`
-   `*.pyc`
-   `.coverage`

## Example

``` bash
$ swiffer

./build
./dist
./swiffer.egg-info
./tests/__pycache__

🧹 Removed 4 items.
```