#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    TorF = []

    for each in my_list:
        if each % 2 == 0:
            TorF.append(True)
        else:
            TorF.append(False)
    return TorF
