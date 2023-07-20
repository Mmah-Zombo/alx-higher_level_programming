#!/usr/bin/python3
"""function program"""


def text_indentation(text):
    """the function"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Skip initial whitespace
    char_index = 0
    while char_index < len(text) and text[char_index] == ' ':
        char_index += 1

    for char_index in range(char_index, len(text)):
        print(text[char_index], end="")

        if text[char_index] in "\n.?:":
            if text[char_index] in ".?:":
                print("\n")

            # Skip following whitespace
            char_index += 1
            while char_index < len(text) and text[char_index] == ' ':
                char_index += 1
