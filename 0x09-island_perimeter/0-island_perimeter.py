#!/usr/bin/python3

def island_perimeter(grid):
    """
    Calculates the perimeter of an island.

    Args:
        grid (List[List[int]]): A 2D grid representing the island.

    Returns:
        int: The perimeter of the island.
    """
    count = 0
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    for i in range(rows):
        for j in range(cols):
            neighbors = [
                (i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)
            ]
            valid_neighbors = [
                1 if 0 <= k[0] < rows and 0 <= k[1] < cols else 0
                for k in neighbors
            ]

            if grid[i][j]:
                count += sum(
                    1 if not r or not grid[k[0]][k[1]] else 0
                    for r, k in zip(valid_neighbors, neighbors)
                )

    return count

