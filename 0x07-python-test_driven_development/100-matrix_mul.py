#!/usr/bin/python3
"""function program"""


def validate_matrix(matrix):
    """Check if matrix is a list"""
    if not isinstance(matrix, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    # Check if matrix is a list of lists
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("m_a must be a list of lists or m_b must \
                        be a list of lists")

    # Check if matrix is not empty
    if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
        raise ValueError("m_a can't be empty or m_b can't be empty")

    # Check if matrix contains only integers or floats
    for row in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("m_a should contain only integers or floats or \
                            m_b should contain only integers or floats")

    # Check if the matrix is a rectangle (all rows have the same size)
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise ValueError("each row of m_a must be of the same size or each \
                         row of m_b must be of the same size")


def matrix_mul(m_a, m_b):
    """Validate m_a and m_b"""
    validate_matrix(m_a)
    validate_matrix(m_b)

    # Check if the matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            dot_product = sum(m_a[i][k] * m_b[k][j]
                              for k in range(len(m_a[0])))
            row.append(dot_product)
        result.append(row)

    return result
