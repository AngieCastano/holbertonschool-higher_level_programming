#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printing = -1
    for iter in range(x):
        printing = printing + 1
        try:
            print("{}".format(my_list[iter]), end="")
        except:
            printing = printing - 1
    print("")
    return (printing + 1)
