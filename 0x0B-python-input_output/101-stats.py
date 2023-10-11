#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics"""
import sys


def stats():
    """stats()"""

    try:
        count = 0
        data = {}
        size = 0
        valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
        for line in sys.stdin:
            line = line.strip().split()
            size += int(line[-1])
            if line[-2] in valid_codes:
                data[line[-2]] = 1 if not data.get(line[-2]) \
                        else data[line[-2]] + 1
            count += 1
            if count == 10:
                print_stats(data, size)
                count = 0
        print_stats(data, size)
    except KeyboardInterrupt:
        print_stats(data, size)
        raise
    except (IndexError, ValueError):
        pass


def print_stats(data, size):
    """def print_stats(data):"""

    print(f"File size: {size}")
    for i in sorted(data):
        print(f"{i}: {data[i]}")


if __name__ == "__main__":
    stats()
