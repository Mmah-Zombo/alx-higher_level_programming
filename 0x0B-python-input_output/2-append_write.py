#!/usr/bin/python3
'''a function that appends a string at the end of a text file (UTF8)
 and returns the number of characters added
 '''
def append_write(filename="", text=""):
    """Writes a string to a UTF8 text file
    """
    with open(filename, "a", encoding="utf8") as file:
        return file.write(text)