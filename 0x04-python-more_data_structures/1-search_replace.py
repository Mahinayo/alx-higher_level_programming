#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def x(y):
        return (y if y != search else replace)
    return list(map(x, my_list))
