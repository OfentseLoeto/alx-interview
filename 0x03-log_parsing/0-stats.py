#!/usr/bin/python3
"""
Defining the sttus code to track
"""
import sys
import signal


# define the status code to track
STATUS_CODE = [200, 301, 400, 401, 403, 404, 405, 500]


def signal_handler(signal, frame):
    '''Handle Ctrl+C (SIGINT) to print statistics and exit'''
    print_statistics()
    sys.exit(0)


def print_stats():
    '''Print the acumulated statistics'''
    if total_file_size > 0:
        print(f"Total file size: {total_file_size}")
        for code in sorted(STATUS_CODE):
            if code in status_count:
                print(f"{code}: {status_count}")


total_file_size = 0
status_count = {}
line_count = 0

# Register the Ctrl+C signal handler
signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    line = line.strip()

    # Parse the line input
    parts = line.split()
    if len(parts) != 7:
        continue

    ip_address, _, _, status_code, file_size = parts

    try:
        status_code = int(status_code)
        file_size = int(file_size)
    except ValueError:
        continue

if status_code in STATUS_CODE:
    total_file_size += file_size
    if status_code in status_count:
        status_counts[status_code] += 1
    else:
        status_count[staus_code] = 1

    # Increment line count
    line_count += 1

    # Print statistics after every 10 lines
    if line_count % 10 == 0:
        print_statistics()
