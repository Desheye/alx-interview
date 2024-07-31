#!/usr/bin/python3
"""N Queens Problem Solver"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])


def find_queen_positions(n, row=0, columns=[], diagonals1=[], diagonals2=[]):
    """Finds all valid positions for the queens."""
    if row < n:
        for col in range(n):
            if col not in columns and row + col not in diagonals1 and row - col not in diagonals2:
                yield from find_queen_positions(n, row + 1, columns + [col], diagonals1 + [row + col], diagonals2 + [row - col])
    else:
        yield columns


def solve_n_queens(n):
    """Solves the N Queens problem and prints all solutions."""
    solutions = []
    row_index = 0
    for solution in find_queen_positions(n):
        for col in solution:
            solutions.append([row_index, col])
            row_index += 1
        print(solutions)
        solutions = []
        row_index = 0


solve_n_queens(n)

