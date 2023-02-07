#!/usr/bin/python3

'''Tests if an object is exactly an instance
of a specified class or an instance of the an inherited
class

Args: 
    obj (object): the object to be tested
    a_class (class): the specified class 
'''
def is_same_class(obj, a_class):
    '''Checks if its an instance'''
    if isinstance(obj, a_class):
        return True
    else:
        return False