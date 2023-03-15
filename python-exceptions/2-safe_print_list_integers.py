#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    cont = 0
    for item in range(x):
        try:
            print("{:d}".format(my_list[item]), end="")
            cont += 1
        except(ValueError, TypeError):
            False
    print()
    return cont
