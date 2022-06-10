#!/usr/bin/python3
def uniq_add(my_list=[]):
    x = 0
    for y in set(my_list):
        x += y
    return x
