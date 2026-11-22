import argparse
import sys
from pathlib import Path

from report import generate_report


def parse_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Print a summary report for a sales CSV.")
    parser.add_argument("csv_path", type=Path, help="Path to the sales CSV file")
    return parser.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    if not args.csv_path.is_file():
        print(f"Error: file not found: {args.csv_path}", file=sys.stderr)
        return 1
    print(generate_report(args.csv_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
    