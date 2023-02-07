#!/usr/bin/python3
'''MyList is a class that inherits from (list)'''
class MyList(list):
    '''Prints a sorted list'''
    def print_sorted(self):
        newlist = []
        for each in self:
            newlist.append(each)
        newlist.sort()
        print(newlist)