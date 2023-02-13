#!/usr/bin/python3
""" class Rectangule that inherits from Base """
from models.base import Base

class Rectangle(Base):
    """ defines an initialization method """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    super().__init__(id)

    @property
    def __width(self):
        """ width getter """
        return self.__width

    @property
    def __height(self):
        """ height getter """
        return self.__height

    @property
    def __x(self):
        """ x getter """
        return self.__x

    @property
    def __y(self):
        """ y getter """
        return self.__y

    @__height.setter
        """ height setter """
    def height(self, value):
    
    @__width.setter
        """ width setter """
    def width(self, value):

    @__x.setter
    """ x setter """
    def x(self, value):

    @__y.setter
    """ y setter """
    def y(self, value):
