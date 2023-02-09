#!/usr/bin/python3
""" class Square that inherits from Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Instantation """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
        self.__width = size
        self.__height = size

    def area(self):
        return self.__width ** 2

    def __str__(self):
        return (f"[Square] {self.__width}/{self.__height}")
