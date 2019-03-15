# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 08:52:16 2018

 Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with
 digits. The objective is to fill the grid with the constraint that every row,
 column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.

Implement an efficient sudoku solver.
@author: carlgval
"""

import matplotlib.pyplot as plt
from copy import deepcopy


class Sudoku(object):
    def __init__(self, board):
        self.start_board = deepcopy(board)
        self.solution = deepcopy(board)
        self.solved = is_complete(self.solution)

    def solve(self, plot_result=True):
        self.solution = new_number(self.solution, plot_each=-1)
        self.solved = is_complete(self.solution)
        if plot_result:
            plot_sudoku(self.solution)

    def hint(self, board=None):
        if board is None:
            board = self.start_board

        hinted = deepcopy(board)
        i, j = next_empty(board)

        hinted[i][j] = self.solution[i][j]
        plot_sudoku(hinted)

        print("The number at %d, %d is %d" % (i, j, self.solution[i][j]))


def plot_sudoku(board):
    fig, ax = plt.subplots()
    ax.matshow(board, cmap='gray', vmin=-10000)

    for i in range(len(board)):
        for j in range(len(board)):
            c = board[j][i]
            ax.text(i, j, str(c), va='center', ha='center')
    plt.show()


def new_number(board, iteration=[0], plot_each=1000):
    if is_complete(board):
        return board

    r, c = next_empty(board)
    for i in range(1, 10):
        iteration[0] += 1
        if plot_each >= 0 and iteration[0] % plot_each == 0:
            print(iteration[0])
            plot_sudoku(board)
        board[r][c] = i
        if check_board(board) == 0:
            n = new_number(board, iteration, plot_each)
            if is_complete(n):
                return n
        board[r][c] = 0
    return board


def next_empty(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 0:
                return (r, c)


def is_complete(board):
    if any(any(v == 0 for v in row) for row in board):
        return False
    else:
        return True


def check_board(board):
    if any(row.count(i) > 1 for i in range(1, 10) for row in board):
        return 1
    temp_board = [[row[i] for row in board] for i in range(len(board))]
    if any(row.count(i) > 1 for i in range(1, 10) for row in temp_board):
        return 2
    temp_board = [[board[(i // 3) * 3 + j // 3][(i % 3 * 3) + j % 3]
                   for j in range(len(board))]
                  for i in range(len(board))]
    if any(row.count(i) > 1 for i in range(1, 10) for row in temp_board):
        return 3
    return 0


if __name__ == '__main__':
    easy = [[2, 9, 0, 0, 0, 0, 0, 7, 0],
            [3, 0, 6, 0, 0, 8, 4, 0, 0],
            [8, 0, 0, 0, 4, 0, 0, 0, 2],
            [0, 2, 0, 0, 3, 1, 0, 0, 7],
            [0, 0, 0, 0, 8, 0, 0, 0, 0],
            [1, 0, 0, 9, 5, 0, 0, 6, 0],
            [7, 0, 0, 0, 9, 0, 0, 0, 1],
            [0, 0, 1, 2, 0, 0, 3, 0, 6],
            [0, 3, 0, 0, 0, 0, 0, 5, 9]]

    s = Sudoku(easy)
    s.solve(plot_result=True)
