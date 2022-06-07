#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    x = 0
    for y in argv[1:]:
        x += int(y)
    print("{:d}".format(x))
