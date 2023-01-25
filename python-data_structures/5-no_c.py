#!/usr/bin/python3
def no_c(my_string):
    char = "cC"
    my_string = ''.join(letter for letter in my_string if letter not in char)
    return my_string
