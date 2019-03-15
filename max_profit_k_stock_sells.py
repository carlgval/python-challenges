#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 08:22:52 2019

 Given an array of numbers representing the stock prices of a company in
 chronological order and an integer k, return the maximum profit you can make
 from k buys and sells. You must buy the stock before you can sell it, and
 you must sell the stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.

@author: carlgval
"""


def max_profit(array, k):
    n = len(array)
    profit = [[0 for _ in range(n + 1)] for i in range(k + 1)]

    for i in range(1, k + 1):
        difference = float('-inf')
        for j in range(1, n):
            difference = max(difference, profit[i - 1][j - 1] - array[j - 1])
            profit[i][j] = max(difference + array[j], profit[i][j - 1])
    return profit[k][n - 1]


if __name__ == '__main__':
    print(max_profit([5, 2, 4, 0, 1], 2))
