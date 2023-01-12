#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for each in set(my_list):
        sum  += each
    return sum
