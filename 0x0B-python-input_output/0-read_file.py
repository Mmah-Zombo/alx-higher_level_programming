#!/usr/bin/python3
'''a function that reads a text file (UTF8) and 
prints it to stdout
'''
def read_file(filename=""):
    """Prints the contents of a UTF8 text file"""
    with open(filename, "r", encoding="utf8") as f:
        print(f.read())