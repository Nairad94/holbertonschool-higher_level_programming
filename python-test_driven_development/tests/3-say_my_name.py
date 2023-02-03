#!/usr/bin/python3
""" Write a function that prints My name """


def say_my_name(first_name, last_name=""):
    print("My name is ", end="")
    for fn in range(len(first_name)):
        print(first_name[fn], end="")
    print(" ", end="")
    for ln in range(len(last_name)):
        print(last_name[ln], end="")
    print()
