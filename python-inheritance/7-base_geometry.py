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
