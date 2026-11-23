"""Record study sessions and report progress toward a weekly goal."""

import argparse
import json
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parent.parent / "study_progress.json"


def load_minutes() -> int:
    if not DATA_FILE.exists():
        return 0

    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        return max(0, int(data.get("minutes", 0)))
    except (json.JSONDecodeError, OSError, TypeError, ValueError):
        return 0


def save_minutes(minutes: int) -> None:
    DATA_FILE.write_text(json.dumps({"minutes": minutes}, indent=2), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Track study time toward a weekly goal."
    )
    parser.add_argument(
        "--minutes",
        type=int,
        default=0,
        help="minutes studied in a session (default: 0)",
    )
    parser.add_argument(
        "--goal",
        type=float,
        default=10,
        help="weekly study goal in hours (default: 10)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.minutes < 0:
        raise SystemExit("Error: --minutes must be zero or greater.")
    if args.goal <= 0:
        raise SystemExit("Error: --goal must be greater than zero.")

    total_minutes = load_minutes()
    if args.minutes:
        total_minutes += args.minutes
        save_minutes(total_minutes)
        print(
            f"Added {args.minutes} minutes.",
            end=" ",
        )

    total_hours = total_minutes / 60
    percentage = min((total_hours / args.goal) * 100, 100)
    print(
        f"Total: {total_hours:.1f} hours / "
        f"{args.goal:.1f} hours ({percentage:.1f}%)"
    )


if __name__ == "__main__":
    main()
