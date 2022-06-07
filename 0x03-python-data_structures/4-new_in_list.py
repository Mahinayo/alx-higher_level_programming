#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    x = my_list[:]
    if 0 <= idx < len(x):
        x[idx] = element
        return (x)
    return (my_list)
