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


def get_size(path: Path):
    if path.is_file():
        return path.stat().st_size

    total = 0
    for p in path.rglob("*"):
        if p.is_file():
            total += p.stat().st_size
    return total


def clean(path: Path, dry_run=False):
    removed = []
    total_size = 0
    skipped_dirs = []

    for p in path.rglob("*"):

        if any(parent in p.parents for parent in skipped_dirs):
            continue

        if p.is_dir() and (p.name in DIR_PATTERNS or p.name.endswith(".egg-info")):
            size = get_size(p)

            removed.append(p)
            total_size += size
            skipped_dirs.append(p)

            if not dry_run:
                shutil.rmtree(p, ignore_errors=True)

        elif p.is_file():
            for pattern in FILE_PATTERNS:
                if p.match(pattern):
                    size = p.stat().st_size

                    removed.append(p)
                    total_size += size

                    if not dry_run:
                        p.unlink(missing_ok=True)

                    break

    return removed, total_size
