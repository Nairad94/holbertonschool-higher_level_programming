#!/usr/bin/python3
""" Write a function that prints a text """


def text_indentation(text):
    """ prints a text with 2 new lines after each of these char: .?: """
    if (type(text)) != str:
        raise TypeError("text must be a string")
    text1 = ".".join([substring.strip() for substring in text.split(".")])
    text2 = ":".join([substring.strip() for substring in text1.split(":")])
    text3 = "?".join([substring.strip() for substring in text2.split("?")])

    for char in text3:
        if (char == '.' or char == '?' or char == ':'):
            print(char)
            print()
        else:
            print(char, end="")
# .split: permite dividir una cadena de texto en una lista de subcadenas,
# utilizando un separador especificado.
# .strip: permite eliminar los caracteres iniciales y finales de una cadena
# de texto que sean espacios en blanco o caracteres específicos
