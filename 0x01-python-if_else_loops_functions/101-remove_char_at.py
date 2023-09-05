#!/usr/bin/python3
def remove_char_at(str, n):
    for index in range(0, len(str)):
        if index == n:
            continue
        str2 += str[index]
