#!/usr/bin/python3

for i in range(10):
    for j in range(10):
        if i < j:
            if (i, j) == (8, 9):
                print(f"{i:01d}{j:01d}")
            else:
                print(f"{i:01d}{j:01d}, ", end="")
