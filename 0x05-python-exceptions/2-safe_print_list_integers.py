#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printing = 0
    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end="")
        except (ValueError, TypeError):
            pass
        else:
            printing = printing + 1
    print("")
    return (printing)
