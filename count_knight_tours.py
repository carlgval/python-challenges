# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 09:11:35 2018


A knight's tour is a sequence of moves by a knight on a chessboard such that
all squares are visited once.

Given N, write a function to return the number of knight's tours on an N by N
chessboard.


@author: carlgval
"""


def count_tours(n):
    tours = 0
    for i in range(n):
        for j in range(n):
            board = [[0 for _ in range(n)] for _ in range(n)]
            board[i][j] = 1
            tours += _count_tours(board, i, j)
            print(tours)


def _count_tours(board, i, j, tours=0):
    if all([all([e > 0 for e in row]) for row in board]):
        return 1

    moves = check_moves(i, j, len(board))

    for i_next, j_next in moves:
        if board[i_next][j_next] > 0:
            continue
        board[i_next][j_next] = 1
        tours += _count_tours(board, i_next, j_next)
        board[i_next][j_next] = 0
    return tours


def check_moves(i, j, n):
    moves = []
    if (i > 0) and (j > 1):
        moves.append((i - 1, j - 2))
    if (i > 1) and (j > 0):
        moves.append((i - 2, j - 1))
    if (i > 0) and (j < (n-2)):
        moves.append((i - 1, j + 2))
    if (i > 1) and (j < (n-1)):
        moves.append((i - 2, j + 1))
    if (i < (n-2)) and (j > 0):
        moves.append((i + 2, j - 1))
    if (i < (n-1)) and (j > 1):
        moves.append((i + 1, j - 2))
    if (i < (n-2)) and (j < (n-1)):
        moves.append((i + 2, j + 1))
    if (i < (n-1)) and (j < (n-2)):
        moves.append((i + 1, j + 2))

    return moves


if __name__ == '__main__':
    print(count_tours(6))
