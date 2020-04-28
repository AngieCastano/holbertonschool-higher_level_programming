#!/usr/bin/python3
def uppercase(str):
    for i in str:
        j = 0
        if i >= 'a' and i <= 'z':
            j = 32
        print("{:c}".format(ord(i) - j), end = "")
    print("")
