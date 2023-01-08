#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    counter = 0
    for array in matrix:
        lastidx = len(array) - 1
        for element in array:
            if lastidx > counter:
                print("{:d} ".format(element))
            else:
                print("{:d}".format(element), end="\n")
            counter += 1
        counter = 0

