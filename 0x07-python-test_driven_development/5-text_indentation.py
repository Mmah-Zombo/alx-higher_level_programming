#!/usr/bin/python3
"""function program"""


def text_indentation(text):
    """the function"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars_to_newline = ['.', '?', ':']
    result = []
    line = ""

    for char in text:
        line += char
        if char in chars_to_newline:
            result.append(line.strip())
            line = ""

    if line:
        result.append(line.strip())

    print("\n".join(result))
