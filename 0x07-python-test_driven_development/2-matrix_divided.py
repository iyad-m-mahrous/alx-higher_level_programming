#!/usr/bin/python3
"""a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """matrix_divided(matrix, div)

    Returns:
        A new matrix with all elemets divided by div,
        rounded to 2 decimal places

    Raises:
        TypeError: if div not integer or float
        ZeroDivisionError: if div equals 0
    """
    if (
            not isinstance(matrix, list) or
            matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(
                isinstance(x, int) or isinstance(x, float)
                for row in matrix
                for x in row
            )
    ):
        raise TypeError(
                "matrix must be a matrix (list of lists)"
                " of integers/floats"
                )
    if (not all(len(row) == len(matrix[0]) for row in matrix)):
        raise TypeError("Each row of the matrix must have the same size")
    if (not isinstance(div, float) and not isinstance(div, int)):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")

    return ([[round(float(x)/div, 2) for x in row] for row in matrix])
