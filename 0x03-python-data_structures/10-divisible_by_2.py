#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        new = []
        for i in my_list:
            new.append(i % 2 - 1)
        print(new)
        return new
