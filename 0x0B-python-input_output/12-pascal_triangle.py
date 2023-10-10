#!/usr/bin/python3
"""a function that returns a list of lists of integers
representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """def pascal_triangle(n):"""

    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    out = [[1], [1, 1]]
    new_row = []
    for i in range(2, n):
        temp = [1]
        new_row = [(out[i-1][j+1])+(out[i-1][j]) for j in range(0, i-1)]
        temp.extend(new_row)
        temp.append(1)
        out.append(temp)
    return out
