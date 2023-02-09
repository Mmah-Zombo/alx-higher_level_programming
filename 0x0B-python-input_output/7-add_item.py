#!/usr/bin/python3
'''a script that adds all arguments to a 
Python list, and then save them to a file
'''
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
    
args_list = []

# Add each argument to the list
for arg in sys.argv[1:]:
    args_list.append(arg)

# Try to load the list from the file
try:
    args_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    pass

# Add each argument to the list
for arg in sys.argv[1:]:
    args_list.append(arg)

# Save the list to the file
save_to_json_file(args_list, 'add_item.json')
