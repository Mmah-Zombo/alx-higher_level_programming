#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for arrayIdx in range(len(matrix)):
        for itemIdx in range(len(matrix[arrayIdx])):
            if itemIdx != 0:
                print(" ", end='')
            print("{:d}".format(matrix[arrayIdx][itemIdx], end=''))
        print()
