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
    if (not isinstance(div, float) and not isinstance(div, int)):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    row_len = len(matrix[0])
    for row in matrix:
        if (len(row) != row_len):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if (not isinstance(element, float)
                    and not isinstance(element, int)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")

        return ([[round(float(x)/div, 2) for x in row] for row in matrix])
