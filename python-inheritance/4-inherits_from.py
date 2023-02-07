#!/usr/bin/python3
""" Write a function that returns True otherwise False """


def inherits_from(obj, a_class):
    """ if it is a class, it returns false, otherwise it checks /
    if it is a subclass, if so it returns true """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
