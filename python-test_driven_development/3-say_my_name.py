#!/usr/bin/python3
""" Write a function that prints My name """


def say_my_name(first_name, last_name=""):
    """ print  first and laste name """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is ", end="")
        for fn in range(len(first_name)):
            print(first_name[fn], end="")
        print("", end="")
        for ln in range(len(last_name)):
            print(last_name[ln], end="")
        print()
