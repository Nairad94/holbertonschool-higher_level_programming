#!/usr/bin/python3
""" class Rectangule that inherits from Base """
from models.base import Base


class Rectangle(Base):
    """defines an initialization method """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
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
        self.height = value

    @width.setter
    def width(self, value):
        """ setter """
        self.width = value

    @x.setter
    def x(self, value):
        """ setter """
        self.x = value

    @y.setter
    def y(self, value):
        """ setter """
        self.y = value
