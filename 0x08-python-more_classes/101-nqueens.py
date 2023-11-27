#!/usr/bin/python3
import sys


def Safe(board, row, colomn):
    """
    Check if it is safe to place a queen at board[row][colomn]
    """
    for i in range(colomn):
        if board[row][i] == 1:
            return False

    i = row
    j = colomn
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = row
    j = colomn
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def Solve(board, colomn, solutions):
    """
    Recursive function to solve the N queens problem using backtracking
    """
    if colomn >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for row in range(N):
        if Safe(board, row, colomn):
            board[row][colomn] = 1

            Solve(board, colomn + 1, solutions)

            board[row][colomn] = 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]

    solutions = []
    Solve(board, 0, solutions)

    for solution in solutions:
        print(solution)
