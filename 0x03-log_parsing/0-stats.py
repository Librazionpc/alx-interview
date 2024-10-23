#!/usr/bin/python3
"""
0-minoperations.py
"""
import sys
import re
from collections import defaultdict


def main():
    """Reads from stdin and computes statistics"""
    total_file_size = 0
    status_counts = defaultdict(int)
    line_count = 0

    # Define a regex pattern to match the log format
    log_pattern = re.compile(
        r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - \[(?P<date>[^\]]+)\] '
        r'"GET /projects/260 HTTP/1.1" (?P<status_code>\d{3}) '
        r'(?P<file_size>\d+)'
    )

    try:
        for line in sys.stdin:
            line_count += 1
            match = log_pattern.match(line)
            if match:
                # Extract file size and status code
                file_size = int(match.group('file_size'))
                status_code = match.group('status_code')

                # Update total file size
                total_file_size += file_size
                # Update status code count
                status_counts[status_code] += 1

                # Print statistics every 10 lines
                if line_count % 10 == 0:
                    print_stats(total_file_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_file_size, status_counts)


def print_stats(total_file_size, status_counts):
    print(f"File size: {total_file_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")
    print()  # New line for separation


if __name__ == "__main__":
    main()
