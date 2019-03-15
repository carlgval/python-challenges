# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 08:15:44 2018

You have an N by N board. Write a function that, given N, returns the number
of possible arrangements of the board where N queens can be placed on the
board without threatening each other, i.e. no two queens share the same row,
column, or diagonal.

@author: carlgval
"""


def count_solution():
    pass

def print_board(board):
    for col in board:
        print(col)
    print('')

def solveNQUtil(board, col):
    if (col == len(board)):
        print_board(board)
        return True

    res = False
    for j, row in enumerate(board[col]):
        if check_pos(board, (col, j)):
            board[col][j] = 1
            res = solveNQUtil(board, col + 1) or res
            board[col][j] = 0
    return res


def check_pos(board, pos):
    try:
        i, j = pos
        if any(board[i]):
            return False
        if any([col[j] for col in board]):
            return False
        if any([board[i+a][j+a] for a in range(-min(i, j),
                                               min(len(board)-i, len(board)-j))]):
            return False
        if any([board[i-a][j+a] for a in range(-min(len(board)-i-1, j),
                                               min(i+1, len(board)-j))]):
            return False

        return True
    except:
        print(board)
        print(pos)
        raise Exception('')


if __name__ =='__main__':
    N = 5
    board = [[0 for i in range(N)] for j in range(N)]

    print(solveNQUtil(board, 0))
