#!/usr/bin/python3
"""another program"""


def text_indentation(text):
    """the function"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_chars = {'.', '?', ':'}
    new_line_chars = {'\n', '\r'}

    in_punctuation = False

    for char in text:
        if char in punctuation_chars:
            if in_punctuation:
                print(char, end='')
            else:
                print('\n' + char, end='')
                in_punctuation = True
        elif char in new_line_chars:
            continue
        else:
            if in_punctuation:
                print()
                in_punctuation = False
            print(char, end='')

    # Make sure there are two new lines after the last sentence.
    print()
