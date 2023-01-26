#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for worth in row:
            print("{:d}".format(worth), end="")
            if row[0] <= worth:
                print(" ", end="")
        print()
