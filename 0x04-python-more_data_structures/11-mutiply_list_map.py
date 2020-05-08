#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    if my_list:
        def mul(my_list):
            return my_list * number
        return list(map(mul, my_list))
    return None
