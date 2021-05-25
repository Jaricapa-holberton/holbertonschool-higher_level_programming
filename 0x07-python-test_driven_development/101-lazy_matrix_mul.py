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

    message_1 = "new m_a must be a list"
    message_2 = "new m_b must be a list"
    message_3 = "new m_a must be a list of lists"
    message_4 = "new m_b must be a list of lists"
    message_5 = "new m_a can't be empty"
    message_6 = "new m_b can't be empty"
    message_7 = "new m_a should contain only integers or floats"
    message_8 = "new m_b should contain only integers or floats"
    message_9 = "new each row of m_a must be of the same size"
    message_10 = "new each row of m_b must be of the same size"
    message_11 = "new m_a and m_b can't be multiplied"

    if (isinstance(m_a, list) is not True):
        raise IndexError(message_1)
    if (isinstance(m_b, list) is not True):
        raise IndexError(message_2)
    for rows in m_a:
        if (isinstance(rows, list) is not True):
            raise IndexError(message_3)
    for rows in m_b:
        if (isinstance(rows, list) is not True):
            raise IndexError(message_4)
    if (m_a == [[]]):
        raise IndexError(message_5)
    if (m_b == [[]]):
        raise IndexError(message_6)
    elements = []
    [elements.extend(i) for i in m_a]
    if not all(type(num) in (int, float) for num in elements):
        raise IndexError(message_7)
    elements = []
    [elements.extend(j) for j in m_b]
    if not all(type(num) in (int, float) for num in elements):
        raise IndexError(message_8)
    for rows in m_a:
        if (len(rows) != len(m_a[0])):
            raise IndexError(message_9)
    for rows in m_b:
        if (len(rows) != len(m_b[0])):
            raise IndexError(message_9)
    if ((len(m_a) == 1) and (len(m_b) == 1)):
        raise IndexError(message_11)

    A = np.array(m_a)
    B = np.array(m_b)
    C = A.dot(B)
    return (C)
