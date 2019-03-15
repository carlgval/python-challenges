# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 08:28:17 2018
 You are given an M by N matrix consisting of booleans that represents a
 board. Each True boolean represents a wall. Each False boolean represents a
 tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the
minimum number of steps required to reach the end coordinate from the start.
If there is no possible path, then return null. You can move up, left, down,
and right. You cannot move through walls. You cannot wrap around the edges of
the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]

and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum
number of steps required to reach the end is 7, since we would need to go
through (1, 2) because there is a wall everywhere else on the second row.

@author: carlosgonzalez
"""


def walk(pos, counts, board, movements=0):
    moves = valid_moves(pos, board)
    movements = movements + 1
    for move in moves:
        if counts[move[0]][move[1]] is None or \
                counts[move[0]][move[1]] > movements:
            counts[move[0]][move[1]] = movements
            walk(move, counts, board, movements)


def solve(start_position, end_position, board):
    counts = [[None for i in range(len(board[0]))] for j in range(len(board))]
    counts[start_position[0]][start_position[1]] = 0
    walk(start_position, counts, board)

    return counts[end_position[0]][end_position[1]]


def valid_moves(start_position, board):
    valid = []
    if start_position[0] > 0:
        valid.append((start_position[0] - 1, start_position[1]))
    if start_position[0] < (len(board) - 1):
        valid.append((start_position[0] + 1, start_position[1]))
    if start_position[1] > 0:
        valid.append((start_position[0], start_position[1] - 1))
    if start_position[1] < (len(board) - 1):
        valid.append((start_position[0], start_position[1] + 1))

    for num, pos in reversed(list(enumerate(valid))):
        i, j = pos
        if board[i][j]:
            valid.pop(num)
    return valid

if __name__ == '__main__':
    board = [[False, False, False, False],
             [True,  True,  False, True ],
             [False, False, False, False],
             [False, False, False, False]]

    start_position = (3, 0)
    end_position = (0, 0)

    print(solve(start_position, end_position, board))

