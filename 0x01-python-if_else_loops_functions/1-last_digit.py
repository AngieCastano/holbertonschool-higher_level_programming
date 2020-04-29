#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
l = number % 10
if number < 0:
    l = (number % 10) * -1
if n % 10 > 5:
    print("Last digit of {} is {} and is greater than 5".format(n, n % 10))
if n % 10 == 0:
    print("Last digit of {} is {} and is 0".format(n, n % 10))
if n % 10 < 6 and n % 10 != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(n, l))
