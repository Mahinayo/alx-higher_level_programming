#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    m = number % -10
else:
    m = number % 10
print('Last digit of', number, 'is', m, end=' ')
if m > 5:
    print('and is greater than 5')
elif m == 0:
    print('and is 0')
else:
    print('and is less than 6 and not 0')
