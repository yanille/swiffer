import sys
from pathlib import Path
from .cleaner import clean


def main():
    args = sys.argv[1:]

    path = "."
    dry_run = False

    for arg in args:
        if arg == "--dry":
            dry_run = True
        else:
            path = arg

    target = Path(path).resolve()

    removed = clean(target, dry_run=dry_run)

    if not removed:
        print("✨ Nothing to clean.")
        return

    for item in removed:
        print(item)

    if dry_run:
        print(f"\n{len(removed)} items would be removed.")
    else:
        print(f"\n🧹 Removed {len(removed)} items.")
