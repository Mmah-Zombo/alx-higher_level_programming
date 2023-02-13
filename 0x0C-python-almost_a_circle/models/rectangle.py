#!/usr/bin/python3
"""A module with a class that inherits from Base class"""
from models.base import Base

class Rectangle(Base):
    """Initialization of the class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a rectanlge to a given value"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a rectanlge to a given value"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @x.setter
    def y(self, value):
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates and returns the area of the rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """Print the rectangle with the # character."""
        for y in range(self.y):
            print("")
        for row in range(self.__height):
            [print(" ", end="")for x in range(self.x)]
            [print("#", end="") for j in range(self.__width)]
            print("")
        
        if self.__height == 0:
            print("")

    def __str__(self) -> str:
        ID = self.id
        h = self.__height
        w = self.__width
        X = self.__x
        Y = self.__y
        return f"[Rectangle] ({ID}) {X}/{Y} - {w}/{h}"


    def update(self, *args):
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]