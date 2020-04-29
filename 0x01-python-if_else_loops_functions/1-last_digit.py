#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = abs(number)
mod = n % 10
if number < 0:
        mod *= -1
        n = number
if mod > 5:
    print("Last digit of {} is {} and is greater than 5".format(n, n % 10))
if mod == 0:
    print("Last digit of {} is {} and is 0".format(n, n % 10))
if mod < 6 and n % 10 != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(n, mod))
