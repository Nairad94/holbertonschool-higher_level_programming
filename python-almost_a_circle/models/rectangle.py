#!/usr/bin/python3
""" class Rectangule that inherits from Base """
from models.base import Base


class Rectangle(Base):
    """defines an initialization method """
    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be >= 0")
        else:
            self.width = width
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be >= 0")
        else:
            self.height = height
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be > 0")
        else:
            self.x = x
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be > 0")
        else:
            self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter """
        return self.__width

    @property
    def height(self):
        """ getter """
        return self.__height

    @property
    def x(self):
        """ getter """
        return self.__x

    @property
    def y(self):
        """ getter """
        return self.__y

    @height.setter
    def height(self, value):
        """ setter """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """ setter """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @x.setter
    def x(self, value):
        """ setter """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ setter """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value
