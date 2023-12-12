#!/usr/bin/env python3
import sys
import signal


def print_stats(total_size, status_counts):
    """
    Prints statistics based on the accumulated metrics.

    Args:
        total_size (int): Total file size accumulated.
        status_counts (dict): Dictionary with status codes
                              as keys and their counts as values.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")
    print()


def process_line(line, total_size, status_counts):
    """
    Processes a line from stdin, extracts relevant information,
    and updates metrics.

    Args:
        line (str): Input line from stdin.
        total_size (int): Total file size accumulated.
        status_counts (dict): Dictionary with status codes
                              as keys and their counts as values.

    Returns:
        tuple: Updated total_size and status_counts.
    """
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
    """
    Main function to read stdin line by line, compute metrics,
    and print statistics.
    """
    total_size = 0
    status_counts = {}
    line_count = 0

    def signal_handler(sig, frame):
        """
        Handles the interrupt signal (SIGINT) and prints
        statistics before exiting.
        """
        nonlocal total_size, status_counts
        print_stats(total_size, status_counts)
        sys.exit(0)

    # Register the signal handler for SIGINT (Ctrl+C)
    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            total_size, status_counts = process_line(line, total_size,
                                                     status_counts)
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        # Handle manual interruption (Ctrl+C)
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
