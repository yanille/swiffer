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

Show how much space would be freed without deleting anything:

``` bash
swiffer --size
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

🧹 Removed 4 items
💾 Freed 42.3 MB
```

## Size preview example

``` bash
$ swiffer --size

./build
./dist
./tests/__pycache__

💾 42.3 MB would be freed.
```