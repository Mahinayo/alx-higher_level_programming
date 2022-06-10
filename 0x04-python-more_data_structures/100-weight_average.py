#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        x = 0
        y = 0
        for z in my_list:
            x += (z[0] * z[1])
            y += z[1]
        return (x / y)
    return 0
