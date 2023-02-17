#!/usr/bin/python3
"""A module with a class that inherits from Base class"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """A squre class based on the rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the square class"""
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)
        
    def __str__(self):
        ID = self.id
        X = self.x
        Y = self.y
        sz = self.__width
        return  f"[Square] ({ID}) {X}/{Y} - {sz}"

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, value):
        self.__height = value
        self.__width = value

    def update(self, *args, **kwargs):
        if args and len(args) != 0:
            try:
                if args[0]:
                    self.id = args[0]
                if args[1]:
                    self.size = args[1]
                if args[2]:
                    self.x = args[2]
                if args[3]:
                    self.y = args[3]
            except:
                pass

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                if k == "size":
                    self.size = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v
    
    def to_dictionary(self):
        return self.__dict__