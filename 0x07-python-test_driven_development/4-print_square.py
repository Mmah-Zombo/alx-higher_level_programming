#!/usr/bin/python3
"""some function in here"""


def print_square(size):
    """function"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is a positive integer or zero
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for _ in range(size):
        print("#" * size)
