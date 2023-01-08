#!/usr/bin/python3
def multiple_returns(sentence):
    newTuple = ()
    if sentence == "":
        return 0, None
    else:
        newTuple = (len(sentence), sentence[0])
        return newTuple
