#!/usr/bin/python3
import sys
import signal
import datetime

# Initialize variables to store statistics
file_sizes = []
status_code_counts = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
        }

line_count = 0


def print_statistics():
    """
    Print computed statistics including total file size
    and status code counts.

    This function is responsible for printing the total
    file size and the count for each status code in
    ascending order.
    """

    total_size = sum(file_sizes)

    print(f"File size: {total_size}")

    # Print status codes in ascending order
    if total_size > 0:
        print(f"{File size}: {total_size}")

    for status_code in sorted(status_code_counts.keys()):
        count = status_code_counts[status_code]
        if count > 0:
            print(f"status_code: {count}")


def handle_interrupt(signum, frame):
    """
    Handles the SIGINT (Ctrl + C) signal and print stats
    before exiting.

    The function is called when the program receives a SIGINT
    (Ctrl + C).

    It prints stats and exit gracefully
    """
    print_statistics()
    sys.exit(0)


# Register the signal handler for SIGINT
signal.signal(signal.SIGINT, handle_interrupt)

# Read input line by line from stdin
for line in sys.stdin:
    line = line.strip()

    # Parse the input line using space as a separator
    parts = line.split()

    if len(parts) != 10:
        # Skip lines that do not match the expected format
        continue

    # Extract the status code and file size from the line
    status_code = int(parts[-2])
    file_size = int(parts[-1])

    # Update statistics
    file_sizes.append(file_size)
    if status_code in status_code_counts:
        status_code_counts[status_code] += 1

    line_count += 1

    # Print statistics after every 10 lines
    if line_count % 10 == 0:
        print_statistics()

print statistics()
