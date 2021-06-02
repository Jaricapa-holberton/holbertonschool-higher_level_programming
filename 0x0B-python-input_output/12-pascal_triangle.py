#!/usr/bin/python3
"""Define class_to_json function"""


def pascal_triangle(n):
    """
    Do a list of lists of integers representing the Pascal’s The_triangle of n

    parametters:
    *n: a integrer number

    return:
    *returns a list of lists of integers
    """

    The_triangle = []

    if n <= 0:
        return The_triangle
    if n == 1:
        The_triangle.append([1])
        return The_triangle
    if n == 2:
        The_triangle.extend([[1], [1, 1]])
        return The_triangle

    if n > 2:
        The_triangle.extend([[1], [1, 1]])
        for new_Row in range(3, n+1):
            row = [1]
            for i in range(new_Row-3):
                row.append(sum(The_triangle[-1][0 + i:2 + i]))
            row.extend([new_Row-1, 1])
            The_triangle.append(row)

    return The_triangle
