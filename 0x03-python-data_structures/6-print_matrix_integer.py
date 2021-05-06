#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for fila in matrix:
        end = ""
        for col in fila:
            print("{}{:d}".format(end, col), end="")
            end = " "
        print("")
