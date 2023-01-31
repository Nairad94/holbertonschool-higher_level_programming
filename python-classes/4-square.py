#!/usr/bin/python3
""" class square """


class Square:
    def __init__(self, __size=0):
        self.__size = __size

    def area(self):
        area = self.__size * self.__size
        return area

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value)) != int:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
