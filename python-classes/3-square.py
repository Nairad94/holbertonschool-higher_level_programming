#!/usr/bin/python3
""" class Square"""


class Square:
    """ Private instance attribute: size """
    def __init__(self, __size=0):
         self.__size = __size
    def area(self):
        area = self.__size * self.__size 
        return area
