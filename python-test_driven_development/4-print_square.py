#!/usr/bin/python3
""" Write a function that prints a square """


def print_square(size):
    if (type(size)) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    else:
        for x in range (size):
            for y in range (size -1):
                print("#", end="")
            print("#")
