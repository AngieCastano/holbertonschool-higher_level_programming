#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_set = set(my_list)
    unique_list = (list(list_set))
    sum = 0
    for item in unique_list:
        sum += item
    return sum
