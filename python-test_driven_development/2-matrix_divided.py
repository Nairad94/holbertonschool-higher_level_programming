#!/usr/bin/python3
""" Write a function that divides all elements of a matrix """

def matrix_divided(matrix, div):
    new_matrix = []
    for row in matrix:
        matrix = list(map(lambda value: value/div, row))
        new_matrix.append(matrix)
    return new_matrix
