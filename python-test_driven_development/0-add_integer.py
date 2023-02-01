#!/usr/bin/python3
""" Write a function that adds 2 integers """


def add_integer(a, b=98):
    """ the addition of a and b, must be integers or floats """
    if (type(a)) != int and (type(a)) != float:
        raise TypeError("a must be an integer")
    if (type(b)) != int and (type(b)) != float:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
