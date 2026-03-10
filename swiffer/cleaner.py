from pathlib import Path
import shutil

DIR_PATTERNS = {
    "__pycache__",
    ".pytest_cache",
    "dist",
    "build",
    ".mypy_cache",
    ".ruff_cache",
    "htmlcov",
}

FILE_PATTERNS = (
    "*.pyc",
    "*.pyo",
    ".coverage",
)


def clean(path: Path, dry_run: bool = False):
    removed = []

    for p in path.rglob("*"):

        if p.is_dir() and (p.name in DIR_PATTERNS or p.name.endswith(".egg-info")):
            removed.append(p)

            if not dry_run:
                shutil.rmtree(p, ignore_errors=True)

        elif p.is_file():
            for pattern in FILE_PATTERNS:
                if p.match(pattern):
                    removed.append(p)

                    if not dry_run:
                        p.unlink(missing_ok=True)

                    break

    return removed
