#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keydel = [k for k, v in a_dictionary.items() if v == value]
    for key in keydel:
        del a_dictionary[key]
