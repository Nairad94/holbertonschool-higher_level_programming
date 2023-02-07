#!/usr/bin/python3
""" function that returns True or False """


def is_same_class(obj, a_class):
    """ True if the object is a instance of the class, otherwise False """
    if type(obj) is a_class:
        return True
    else:
        return False
