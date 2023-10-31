#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def print_solution(board):
    solution = []
    for i in range(len(board)):
        solution.append([i, board[i]])
    print(solution)


def solve(board, row, size):
    if row == size:
        print_solution(board)
        return
    for col in range(size):
        if is_safe(board, row, col):
            board[row] = col
            solve(board, row + 1, size)


def nqueens(size):
    if not size.isdigit():
        print("N must be a number")
        sys.exit(1)
    size = int(size)
    if size < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [-1] * size
    solve(board, 0, size)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    nqueens(sys.argv[1])
