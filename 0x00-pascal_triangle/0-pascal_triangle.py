def pascal_triangle(n):
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Generate each row of Pascal's Triangle
    for i in range(1, n):
        # Start each row with a 1
        row = [1]
        # Use a list comprehension to create the middle elements of the row
        row.extend([triangle[i-1][j-1] + triangle[i-1][j] for j in range(1, i)])
        # End each row with a 1
        row.append(1)
        # Add the completed row to the triangle
        triangle.append(row)

    return triangle

# Testing the function with the provided main code
if __name__ == "__main__":
    def print_triangle(triangle):
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))
