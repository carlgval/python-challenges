#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 17:07:11 2018

 Given a 2D board of characters and a word, find if the word exists in the
 grid.

The word can be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same
letter cell may not be used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

exists(board, "ABCCED") returns true, exists(board, "SEE") returns true,
exists(board, "ABCB") returns false.

@author: carlgval
"""

import numpy as np


def exist_word(board, word):
    board = np.array(board)

    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if next_step(board, word, (i, j)):
                return True

    return False


def next_step(board, string, pos):

    if not string:
        return True

    neighbours = get_neighbours(pos, board.shape)

    for neighbour in neighbours:
        x, y = neighbour
        if board[x, y] == string[0]:
            temp = board[x, y]
            board[x, y] = ''
            if next_step(board, string[1:], (x, y)):
                return True
            board[x, y] = temp

    return False


def get_neighbours(pos, board_shape):
    x, y = pos
    x_lim, y_lim = board_shape
    neighbours = []
    if x > 0:
        neighbours.append((x - 1, y))
    if x < (x_lim - 1):
        neighbours.append((x + 1, y))
    if y > 0:
        neighbours.append((x, y - 1))
    if y < (y_lim - 1):
        neighbours.append((x, y + 1))
    return neighbours


if __name__ == '__main__':
    board = [['A', 'B', 'C', 'E'],
             ['S', 'F', 'C', 'S'],
             ['A', 'D', 'E', 'E']]

    word = "ABCCED"
    print('%s: %s' % (word, exist_word(board, word)))

    word = "SEE"
    print('%s: %s' % (word, exist_word(board, word)))

    word = "ABCB"
    print('%s: %s' % (word, exist_word(board, word)))
