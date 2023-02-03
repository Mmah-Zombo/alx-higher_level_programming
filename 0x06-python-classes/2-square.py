#!/bin/bash/python3
# 3-square.py

"""A class that defines a square 
based on the previous file"""

class Square:
    """an initiialization of the class is created"""
    def __init__(self, size=0):
        """Checks if the size is an integer and if the size in greater 
        than 0"""
        if not size.isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
