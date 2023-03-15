#!/usr/bin/python3
"""printing of an integers list"""

def safe_print_integer(value):
    """function that print integer or return false"""
    try:
        print ("{:d}".format(value))
    except(ValueError, TypeError):
        return False
    else:
        return True
