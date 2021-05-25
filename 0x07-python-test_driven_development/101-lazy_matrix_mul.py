#!/usr/bin/python3
"""
Module to find the max integer in a list.
"""


def lazy_matrix_mul(m_a, m_b):
    """
    Function to find and return the max integer in a list of integers
    If the list is empty, the function returns None.
    """
    import numpy as np

    message_1 = "m_a must be a list"
    message_2 = "m_b must be a list"
    message_3 = "division by zero"
    message_4 = "Each row of the matrix must have the same size"


    if (isinstance(m_a, list) is not True):
        raise TypeError(message_1)
    for rows in matrix:
        if (isinstance(rows, list) is not True):
            raise TypeError(message_1)

    A = np.array(m_a)
    B = np.array(m_b)
    C = A.dot(B)
    return (C)
