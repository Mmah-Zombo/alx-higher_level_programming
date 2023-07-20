#!/usr/bin/python3
"""Solves the N-queens puzzle."""
import sys


def is_safe(board, row, col, N):
    """Check if there is a queen in the same column"""
    for i in range(row):
        if board[i] == col or \
           board[i] + i == col + row or \
           board[i] - i == col - row:
            return False
    return True


def solve_nqueens(board, row, N):
    """solves it"""
    if row == N:
        print_solution(board, N)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens(board, row + 1, N)


def print_solution(board, N):
    """print sol"""
    solution = []
    for col in board:
        solution.append([i, col] for i, col in enumerate(board))
    print(solution)


def nqueens(N):
    """nqns"""
    try:
        N = int(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [0] * N
    solve_nqueens(board, 0, N)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
