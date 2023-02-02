#!/usr/bin/python3
""" Write a function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """ divides all elements of a matrix by div """
    new_matrix = []
    for row in matrix:
        for value in row:
            if (type(value)) != int and (type(value)) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    if (type(div)) != int and (type(div)) != float:
        raise TypeError("div must be a number")
    if div <= 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        matrix = list(map(lambda value: round(value/div, 2), row))
        new_matrix.append(matrix)
    return new_matrix
