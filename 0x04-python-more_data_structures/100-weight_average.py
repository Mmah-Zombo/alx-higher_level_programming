#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    wght_sum = sum([score * wght for score, wght in my_list])
    ttl_wght = sum([wght for _, wght in my_list])
    return wght_sum/ttl_wght
