#!/usr/bin/python3
"""A program that contains a rectangle class"""


class Rectangle:
    """Represent a rectangle."""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width != 0 and self.__height != 0:
            return 2 * (self.__width + self.__height)
        else:
            return (0)

    def __str__(self):
        """String presentation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += str(self.print_symbol) * self.__width + "\n"
        return rectangle_str.rstrip("\n")

    def __repr__(self):
        "representation of the class"
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """message for a deleted rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compares two rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        return rect_1 if area_1 >= area_2 else rect_2

    @classmethod
    def square(cls, size=0):
        """ returns a new Rectangle instance with width == height == size"""
        return cls(size, size)
