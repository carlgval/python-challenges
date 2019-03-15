# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 08:33:48 2018

 Given a array of numbers representing the stock prices of a company in
 chronological order, write a function that calculates the maximum profit
 you could have made from buying and selling that stock once. You must buy
 before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could
buy the stock at 5 dollars and sell it at 10 dollars.

@author: carlgval
"""


def max_profit(array):
    max_profit = 0
    profit = 0
    min_a = float('inf')

    for i in range(len(array) - 1):
        min_a = min(array[i], min_a)

        if min_a < array[i + 1]:
            profit = array[i + 1] - min_a
            if profit > max_profit:
                max_profit = profit
    return max_profit

print(max_profit([9, 11, 8, 5, 7, 10]))
