#!/usr/bin/env python3

def print_fibonacci(length):

    if length==0:
        print([])
    elif length==1:
        print([0])
    else:
        newList = [0,1]
        for i in range(2, length):
            newList.append(newList[i-1]+newList[i-2])
        print(newList)

