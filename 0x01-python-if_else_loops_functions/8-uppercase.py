#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord('a') <= ord(c) <= ord('z'):
            i = chr(ord(c) - (ord('a') - ord('A')))
        print("{:s}".format(i), end='')
    print("")
