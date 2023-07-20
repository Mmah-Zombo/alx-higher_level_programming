#!/usr/bin/python3
"""matrix division program"""


def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix."""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if not all(isinstance(r, list) and all(isinstance
                                           (n, (int, float)) for n in r)
               for r in matrix):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    # Check if each row of the matrix has the same size
    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform the division and round the result to 2 decimal places
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return new_matrix
