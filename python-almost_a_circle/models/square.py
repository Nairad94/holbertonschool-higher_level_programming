#!/usr/bin/python3
""" class square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ defines an initialization method """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id)
        self.size = size
        self.x = x
        self.y = y
        super().__init__(size, size)

    def __str__(self):
        """ method so that it returns [Square] """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")
