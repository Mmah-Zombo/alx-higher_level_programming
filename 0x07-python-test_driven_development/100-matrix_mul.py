#!/usr/bin/python3
"""function program"""


def validate_matrix(matrix):
    """one of them"""
    if not isinstance(matrix, list):
        raise TypeError("Matrix must be a list")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("Matrix must be a list of lists")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must be of the same size")
    if not all(isinstance(element, (int, float))
               for row in matrix for element in row):
        raise TypeError("Matrix should contain only integers or floats")


def matrix_mul(m_a, m_b):
    """the other one"""
    validate_matrix(m_a)
    validate_matrix(m_b)

    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("Matrix cannot be empty")

    if len(m_a[0]) != len(m_b):
        raise ValueError("Matrices cannot be multiplied")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            value = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row.append(value)
        result.append(row)

    return result
