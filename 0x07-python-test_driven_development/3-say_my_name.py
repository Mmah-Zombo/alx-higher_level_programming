#!/usr/bin/python3
"""contains a function that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """the function"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the name
    full_name = first_name + " " + last_name
    print("My name is {}".format(full_name))
