#!/usr/bin/python3
"""printing of an integers list"""

def safe_print_integer(value):
    """function that print integer or return false"""
    try:
        value = int(value)
    except ValueError:
        return False
    else:
        print ("{:d}".format(value)) #"{:d}" is used to print integers
        return True
