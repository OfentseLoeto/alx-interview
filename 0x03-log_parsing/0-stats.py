#!/usr/bin/python3
"""
Define a dictionary to store status code counts
"""


def status_code_counts = {
        200 : 0,
        301 : 0,
        400 : 0
        401 : 0
        403 : 0,
        404 : 0,
        405 : 0,
        500 : 0
        }

# Initialize the total file size
total_file_size = 0
# counter for line read
lines_read = 0

# Define a function to handle Ctrl+C (KeyboardInterruption)
def signal_handler(signal, frame):
    print_stats()

# Register signal handler Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

# Function to print statistics
def print_stats():
    print(f"Total file size: {file_size}")
    for status_code, count in sorted(status_code_counts.items()):
        if status_code > 0:
            print(f"{status_code}: {count}")

# Read input line by line from stdin
for line in sys.stdin:
    # split line into parts
    parts = line.split()

    # Check if line matches the expected format
    if len(parts) == 10 and parts[8].isdigit():
        # Extract status code and file size
        status_code = int(parts[8])
        file_size = int(parts[9])

        # update the total file size
        total_file_size += file_size

        # Update status code counts
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

            # Increment line-read count
            lines_read += 1

            # check if its time to print stats
            if lines_read % 10 == 0:
                prints_stats()

print_stats()
