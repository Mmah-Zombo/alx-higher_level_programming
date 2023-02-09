#!/usr/bin/env python
import sys

# Initialize the counters for each status code
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

# Total file size
total_size = 0

# Line counter
line_counter = 0

try:
    for line in sys.stdin:
        line_counter += 1
        parts = line.split()
        status = int(parts[3])
        size = int(parts[4])
        total_size += size
        status_codes[status] += 1

        if line_counter % 10 == 0:
            print("Total file size:", total_size)
            for status in sorted(status_codes.keys()):
                if status_codes[status] > 0:
                    print("{}: {}".format(status, status_codes[status]))
except KeyboardInterrupt:
    print("\nExiting program...")
    print("Total file size:", total_size)
    for status in sorted(status_codes.keys()):
        if status_codes[status] > 0:
            print("{}: {}".format(status, status_codes[status]))
