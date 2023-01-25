#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for worth in row:
            print("{:d} ".format(worth), end="")
        print()
