#!/usr/bin/python3
""" class square """


class Square:
    """ Private instance attribute: size """
    def __init__(self, __size=0):
        self.__size = __size
    """ area of a square """
    def area(self):
        area = self.__size * self.__size
        return area
    """ Print a square """    
    def my_print(self):
        x = 0
        y = 0
        for x in range(self.__size):
            for y in range(self.__size - 1):
                print("#", end="")
            print("#")
        if (self.__size == 0):
            print()
    """ Devolver un atributo de propiedad """
    @property
    def size(self):
        return self.__size
    """ permite establecer o mutar el valor de un atributo en una clase """
    @size.setter
    def size(self, value):
        if (type(value)) != int:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
    