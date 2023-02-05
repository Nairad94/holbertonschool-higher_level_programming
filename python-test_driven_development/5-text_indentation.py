#!/usr/bin/python3
""" Write a function that prints a text """


def text_indentation(text):
    if (type(text)) != str:
            raise TypeError("text must be a string")
    else:
        for char in text:
            if (char == '.' or char == '?' or char == ':'):
                print(char)
                print()
            else: 
                print(char, end="")
