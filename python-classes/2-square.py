#!/usr/bin/python3
""" class Square"""


class Square:
    """ Private instance attribute: size """
    def __init__(self, __size=0):
        if (type(__size)) == int:
            self.__size = __size
        else:
            raise TypeError("size must be an integer")
        if (self.__size >= 0):
            self.__size = __size
        else:
            raise ValueError("size must be >= 0")
