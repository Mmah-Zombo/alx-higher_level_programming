#!usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__nextNode = next_node

    '''This is where I become lazy to type a proper comment on the code
    and nobpdy cares.'''
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be integer")
        else:
            self.data = value

    @property
    def next_node(self):
        return self.nextNode

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value != None:
            raise TypeError("next_node must be a Node obect")
        else:
            nextNode = value
    

class SinglyLinkedList:
    def __init__(self):
        self.__head = None
    