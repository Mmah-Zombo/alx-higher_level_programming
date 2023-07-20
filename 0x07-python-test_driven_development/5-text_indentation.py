#!/usr/bin/python3
"""another program"""


def text_indentation(text):
    """the function"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = {'.', '?', ':'}
    current_line = ""

    for char in text:
        current_line += char
        if char in punctuation_marks:
            print(current_line.strip())
            print()
            current_line = ""

    if current_line:
        print(current_line.strip())
