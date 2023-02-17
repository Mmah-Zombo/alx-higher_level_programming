#!/usr/bin/python3
"""A module with a base class"""

import json
class Base:
    """The base for all other classes created"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries == None or list_dictionaries == "[]":
            return "[]"
        else:
            return json.__dict__