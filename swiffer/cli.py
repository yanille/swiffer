import sys
from pathlib import Path
from .cleaner import clean


def format_size(num):
    for unit in ["B", "KB", "MB", "GB"]:
        if num < 1024:
            return f"{num:.1f} {unit}"
        num /= 1024
    return f"{num:.1f} TB"


def main():
    args = sys.argv[1:]

    size_mode = False

    # Only allowed argument is --size
    for arg in args:
        if arg == "--size":
            size_mode = True
        else:
            print(f"❌ Invalid argument: {arg}")
            print("Usage: swiffer [--size]")
            sys.exit(1)

    target = Path(".").resolve()

    removed, total_size = clean(target, dry_run=size_mode)

    if not removed:
        print("✨ Nothing to clean.")
        return

    for item in removed:
        print(item)

    size_str = format_size(total_size)

    if size_mode:
        print(f"\n💾 {size_str} would be freed.")
    else:
        print(f"\n🧹 Removed {len(removed)} items")
        print(f"💾 Freed {size_str}")
