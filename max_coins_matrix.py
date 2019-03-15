#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 08:17:37 2019

 You are given a 2-d matrix where each cell represents number of coins in that
 cell. Assuming we start at matrix[0][0], and can only move right or down,
 find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix

0 3 1 1
2 0 0 4
1 5 3 1

The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.

@author: carlgval
"""

import numpy as np


def count_max_coins(matrix):
    matrix = np.array(matrix)
    max_coins = np.zeros(matrix.shape)

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if i == 0:
                top = matrix[i, j]
            else:
                top = matrix[i, j] + max_coins[i - 1, j]
            if j == 0:
                left = matrix[i, j]
            else:
                left = matrix[i, j] + max_coins[i, j - 1]

            max_coins[i, j] = max((max_coins[i, j], top, left))

    return max_coins[-1, -1]


if __name__ == '__main__':
    matrix = [[0, 3, 1, 1],
              [2, 0, 0, 4],
              [1, 5, 3, 1]]
    print(count_max_coins(matrix))
