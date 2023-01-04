#!/usr/bin/python3
def uppercase(string):
    result = ""
    for ch in string:
        if ord(ch) >= 97 and ord(ch) <= 122:
            print(result)
        else:
            result += ch
    print("{}\n".format(result))
