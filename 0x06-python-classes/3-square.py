#!/bin/bash/python3

"""A square class based on the previous file"""
class Square:
    """initialization of a square"""
    def __init__(self, size=0):
        """some value and size checks"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """returns the current area of the square""" 
        current_area = self.__size * self.__size
        return (current_area)