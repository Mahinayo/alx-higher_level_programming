#!/usr/bin/python3
import hidden_4


def principal():
    for x in dir(hidden_4):
        if not (x[0] == '_' and x[1] == '_'):
            print(x)


if __name__ == "__main__":
    principal()
