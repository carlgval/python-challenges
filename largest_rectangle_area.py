#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 08:36:55 2019

 Given an N by M matrix consisting only of 1's and 0's, find the largest
 rectangle containing only 1's and return its area.

For example, given the following matrix:

[[1, 0, 0, 0],
 [1, 0, 1, 1],
 [1, 0, 1, 1],
 [0, 1, 0, 0]]

Return 4.

@author: carlgval
"""

import numpy as np


def largest_rectangle(matrix):

    matrix = np.array(matrix)

    out = 0

    for k in range(2, len(matrix)):
        for i in range(0, len(matrix) - k + 1):
            for j in range(0, len(matrix) - k + 1):
                print(matrix[i:(i + k), j:(j + k)])
                out = max(out, check_rectangle(matrix[i:(i + k), j:(j + k)]))

    return out


def check_rectangle(matrix):
    if matrix.all():
        return len(matrix) ** 2
    else:
        return 0


if __name__ == '__main__':
    matrix = [[1, 0, 0, 0],
              [1, 0, 1, 1],
              [1, 0, 1, 1],
              [0, 1, 0, 0]]
    print(largest_rectangle(matrix))
