#!/usr/bin/python3
''' function def pascal_triangle(n): that returns a list of lists of integers
representing the Pascal’s triangle of n'''


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
    - n: an integer representing the number of rows in Pascal's triangle.

    Returns:
    - A list of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
