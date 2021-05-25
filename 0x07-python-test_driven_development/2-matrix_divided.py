#!/usr/bin/python3
"""Define function matrix_divided."""


def matrix_divided(matrix, div):
    """
    Add two numbers
    Parameters:
        a (int or float)
        b (int or float) for default = 98
    Return: Integer addition of a and b.
    Raises:
        TypeError: When a or b is a non-integer and non-float.
    """
    if (isinstance(matrix, list) != True):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for rows in matrix:
        if (isinstance(rows, list) != True):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elements = []
    [elements.extend(l) for l in matrix]
    if not all(type(num) in (int, float) for num in elements):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if (matrix == None):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if (div == None):
        raise TypeError("div must be a number")
    if ((matrix == None) and (div == None)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    for rows in matrix:
        if ((len(rows)) != (len(matrix[0]))):
            raise TypeError("Each row of the matrix must have the same size")
    
    new_matrix = []
    for l in matrix:
        list_2 = []
        for num in l:
            number = round(num / div, 2)
            list_2.append(number)
        new_matrix.append(list_2)
    
    return new_matrix
