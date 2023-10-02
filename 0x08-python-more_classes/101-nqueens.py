#!/usr/bin/python3
"""Solves the N-queens puzzle"""


import sys


class Board:

    def __init__(self, n=0):
        self.n = n
        self.board = [[' ' for i in range(self.n)] for j in range(self.n)]

    def board_copy(self, board):
        return ([[i for i in j] for j in board])

    def get_solution(self, board):
        return ([[r, c] for r in range(self.n)
                for c in range(self.n) if board[r][c] == "Q"])

    def set_surrounding(self, board, row, col):
        for c in range(0, self.n):
            if (c != col):
                board[row][c] = "X"
        for r in range(0, self.n):
            if (r != row):
                board[r][col] = "X"
        c = col + 1
        for r in range(row+1, self.n):
            if c >= self.n:
                break
            board[r][c] = "X"
            c += 1
        c = col - 1
        for r in range(row-1, -1, -1):
            if c < 0:
                break
            board[r][c]
            c -= 1
        c = col + 1
        for r in range(row-1, -1, -1):
            if c >= self.n:
                break
            board[r][c] = "X"
            c += 1
        c = col - 1
        for r in range(row+1, self.n):
            if c < 0:
                break
            board[r][c] = "X"
            c -= 1

    def recursive_solve(self, board, row, queens, solutions):
        if queens == self.n:
            solutions.append(self.get_solution(board))
            return (solutions)

        for c in range(self.n):
            if board[row][c] == " ":
                temp_board = self.board_copy(board)
                temp_board[row][c] = "Q"
                self.set_surrounding(temp_board, row, c)
                solutions = self.recursive_solve(
                        temp_board, row + 1,
                        queens + 1, solutions
                        )
        return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = Board(int(sys.argv[1]))
    solutions = board.recursive_solve(board.board, 0, 0, [])
    for i in solutions:
        print(i)
