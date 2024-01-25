#!/usr/bin/python3
"""2D matrix, rotate it 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise.

    Args:
        matrix (List[List[int]]): The input n x n 2D matrix.

    Returns:
        None: The matrix is edited in-place.
    """
    if not matrix or not all(isinstance(row, list)
                             and len(row) == len(matrix) for row in matrix):
        return

    n = len(matrix)

    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rotate_2d_matrix(matrix)
    print(matrix)
