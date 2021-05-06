#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = []
    for row in matrix:
        matrix2.append(list(map(lambda x: x ** 2, row)))
    return matrix2
