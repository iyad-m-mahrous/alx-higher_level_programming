#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics"""
import sys
size = 0


def stats():
    """stats()"""

    count = 1
    global data
    for line in sys.stdin:
        data += (line.strip() + "\n")
        if count == 10:
            print_stats(data)
            count = 0
        count += 1


def print_stats(data):
    """def print_stats(data):"""

    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    global size
    data = data.split("\n")
    data = [row.split(" ") for row in data]
    for i in range(len(data)):
        if len(data[i]) > 1:
            size += int(data[i][-1])
    print(f"File size: {size}")
    stat_code = [
            row[-2] for row in data
            if len(row) > 1 and row[-2] in valid_codes
    ]
    new_dict = {ele: stat_code.count(ele) for ele in set(stat_code)}
    new_dict = dict(sorted(new_dict.items()))
    for i in new_dict:
        print(f"{i}: {new_dict[i]}")


if __name__ == "__main__":
    data = ""
    try:
        stats()
    except KeyboardInterrupt:
        print_stats(data)
        raise
