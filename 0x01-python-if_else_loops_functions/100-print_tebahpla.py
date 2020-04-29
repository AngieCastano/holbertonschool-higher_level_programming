#!/usr/bin/python3
for i in range(122, 96, -1):
    j = 0
    if i % 2:
        j = 32
    print("{:c}".format(i - j), end="")
