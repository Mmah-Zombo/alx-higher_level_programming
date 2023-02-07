#!/usr/bin/python3
'''Tests if an object is exactly an instance
of a specified class or an instance of the an inherited
class 
'''
def is_kind_of_class(obj, a_class):
    '''Checks if its an instance'''
    if isinstance(obj, a_class):
        return True
    else:
        return False