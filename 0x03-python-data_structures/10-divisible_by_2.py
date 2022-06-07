#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    y = []
    if my_list:
        for x in my_list:
            y.append(False if x % 2 else True)
    return y
