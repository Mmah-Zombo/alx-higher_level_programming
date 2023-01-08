#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        biggest = 0
        for number in my_list:
            if number > biggest:
                biggest = number
        return biggest
