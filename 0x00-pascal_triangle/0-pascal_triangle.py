#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the n-th row.

    Args:
        n (int): The number of rows of Pascal's Triangle
                 to generate.

    Returns:
        list of lists of int: Pascal's Triangle represented
                              as a list of lists of integers.
        Returns an empty list if n <= 0.
    """
    # Initialize the list to store Pascal's Triangle
    triangle = []

    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return triangle

    # The first row of Pascal's Triangle is always [1]
    triangle = [[1]]

    # Generate each row of Pascal's Triangle
    for row_num in range(1, n):
        # Start each row with a 1
        row = [1]

        # Compute the middle values of the row
        for col_num in range(len(triangle[row_num - 1]) - 1):
            # Add the two values from the previous row
            row.append(triangle[row_num - 1][col_num] +
                       triangle[row_num - 1][col_num + 1])

        # End each row with a 1
        row.append(1)

        # Append the completed row to the triangle
        triangle.append(row)

    return triangle
