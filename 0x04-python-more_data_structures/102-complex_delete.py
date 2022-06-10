#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    x = []
    for y in a_dictionary:
        if a_dictionary[y] == value:
            x.append(y)
    for y in x:
        del a_dictionary[y]
    return a_dictionary
