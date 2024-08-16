#!/usr/bin/python3

""" Rotate 2D Matrix 90 Degrees Clockwise"""


def rotate_2d_matrix(matrix):
    """
    Rotate a square 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (List[List[int]]): The input square matrix.

    Notes:
        - The function modifies the input matrix directly.
        - Assumes the matrix has 2 dimensions and is not empty.
    """

    n = len(matrix[0])

    for i in range(n - 1, -1, -1):
        for j in range(0, n):
            matrix[j].append(matrix[i].pop(0))
