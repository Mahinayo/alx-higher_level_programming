#!/usr/bin/python3
def roman_to_int(roman_string):
    x = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    y = 0
    total = 0
    if isinstance(roman_string, str):
        for y in range(len(roman_string) - 1):
            if x[roman_string[y]] >= x[roman_string[y + 1]]:
                total += x[roman_string[y]]
            else:
                total -= x[roman_string[y]]
            y += 1
        total += x[roman_string[y]]
        return total
    else:
        return 0
