#!/bin/bash/python3

"""a square class"""
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
    
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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(self.__position, tuple) and len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
            
    def area(self):
        """returns the current area of the square""" 
        current_area = self.__size * self.__size
        return (current_area)

    def my_print(self):
        if self.__size <= 0:
            print("")
        else:
            length = self.__size
            for i in range(length):
                print(" " * self.__position[0])
                print("#" * length)