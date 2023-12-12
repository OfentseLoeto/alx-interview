#!/usr/bin/python3

import sys
import signal

def print_stats(total_size, status_counts):
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")
    print()

def process_line(line, total_size, status_counts):
    try:
        parts = line.strip().split()
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        total_size += file_size

        if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
            if status_code not in status_counts:
                status_counts[status_code] = 0
            status_counts[status_code] += 1

    except (ValueError, IndexError):
        pass

    return total_size, status_counts

def main():
    total_size = 0
    status_counts = {}
    line_count = 0

    def signal_handler(sig, frame):
        nonlocal total_size, status_counts
        print_stats(total_size, status_counts)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            total_size, status_counts = process_line(line, total_size, status_counts)
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()
