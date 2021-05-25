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
    message_1 = "matrix must be a matrix (list of lists) of integers/floats"
    message_2 = "div must be a number"
    message_3 = "division by zero"
    message_4 = "Each row of the matrix must have the same size"
    if (isinstance(matrix, list) is not True):
        raise TypeError(message_1)
    for rows in matrix:
        if (isinstance(rows, list) is not True):
            raise TypeError(message_1)
    elements = []
    [elements.extend(l) for l in matrix]
    if not all(type(num) in (int, float) for num in elements):
        raise TypeError(message_1)
    if (matrix is None):
        raise TypeError(message_1)
    if (div is None):
        raise TypeError(message_2)
    if ((matrix is None) and (div is None)):
        raise TypeError(message_1)
    if (div == 0):
        raise ZeroDivisionError(message_3)
    for rows in matrix:
        if ((len(rows)) is not (len(matrix[0]))):
            raise TypeError(message_4)

    new_matrix = []
    for l in matrix:
        list_2 = []
        for num in l:
            number = round(num / div, 2)
            list_2.append(number)
        new_matrix.append(list_2)

    return new_matrix
