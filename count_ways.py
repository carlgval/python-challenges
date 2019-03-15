# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 09:51:51 2018

 There is an N by M matrix of zeroes. Given N and M, write a function to count
 the number of ways of starting at the top-left corner and getting to the
 bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two
ways to get to the bottom-right:

    Right, then down
    Down, then right

Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

@author: carlgval
"""


def count_ways(n, m):
    matrix = [[0 for _ in range(n)] for _ in range(m)]
    matrix[0] = [1] * n
    for col in matrix:
        col[0] = 1

    for i in range(1, m):
        for j in range(1, n):
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
    return matrix[-1][-1]

if __name__ == '__main__':
    print(count_ways(5, 5))
