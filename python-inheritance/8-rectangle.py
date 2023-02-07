#!/usr/bin/python3
""" Class that defines a BaseGeometry """


class BaseGeometry:
    """ area of a BaseGeometry """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """  validator """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


""" class Rectangle that inherits from BaseGeometry """


class Rectangle(BaseGeometry):
    """ Instantiation """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
