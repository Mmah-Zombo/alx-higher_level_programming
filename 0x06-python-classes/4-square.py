#!/bin/bash/python3
"""a class called square"""
class Square:
    def __init__(self, size=0):
        self.__size = size
    
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns the current area of the square""" 
        current_area = self.__size * self.__size
        return (current_area)