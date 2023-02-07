#!/usr/bin/python3

'''Tests if an object is exactly an instance
of a specified class 
Args: 
    obj (object): the object to be tested
    a_class (class): the specified class '''
def is_same_class(obj, a_class):
        return type(obj) is a_class