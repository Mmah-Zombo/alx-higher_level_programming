#!/usr/bin/python3
'''a file containing a function that uses JSON'''
import json
def load_from_json_file(filename):
    ''' creates an Object from a “JSON file”'''
    with open(filename, 'r') as f:
        return json.load(f)