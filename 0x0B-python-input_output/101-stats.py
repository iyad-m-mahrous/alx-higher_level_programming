#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics"""
import sys


def stats():
    """stats()"""

    count = 1
    data = ""
    for line in sys.stdin:
        data += (line.strip() + "\n")
        if count == 10:
            print_stats(data)
            data = ""
            count = 0
        count += 1


def print_stats(data):
    """def print_stats(data):"""

    size = 0
    data = data.split("\n")
    data = [row.split(" ") for row in data]
    for i in range(len(data)):
        if len(data[i]) > 1:
            size += int(data[i][-1])
    print(f"File size: {size}")
    stat_code = [row[-2] for row in data if len(row) > 1]
    new_dict = {ele: stat_code.count(ele) for ele in set(stat_code)}
    new_dict = dict(sorted(new_dict.items()))
    for i in new_dict:
        print(f"{i}: {new_dict[i]}")


if __name__ == "__main__":
    stats()
