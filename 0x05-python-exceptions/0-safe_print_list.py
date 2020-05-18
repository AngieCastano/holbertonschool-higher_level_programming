#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    iter = 0
    for item in my_list:
        if iter >= x:
            break
        try:
            item
        except:
            pass
        print("{}".format(item), end="")
        iter = iter + 1
    print("")
    return (iter)
