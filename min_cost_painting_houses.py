# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 08:35:31 2018


A builder is looking to build a row of N houses that can be of K different
colors. He has a goal of minimizing cost while ensuring that no two
neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost
to build the nth house with kth color, return the minimum cost which achieves
this goal.

@author: carlgval
"""


def min_cost(price_matrix):
    min_prices = []
    for n, color_prices in enumerate(price_matrix):

        min_prices.append([])

        for color, price in enumerate(color_prices):
            if n == 0:
                min_prices[n].append(price)
            else:
                min_prices[n].append(price + min(min_prices[n-1][:color] +
                                                 min_prices[n-1][(color+1):]))

    return min(min_prices[-1])

if __name__ == "__main__":
    import numpy as np

    colors = np.random.randint(1, 10)
    houses = np.random.randint(3, 20)

    prices = np.random.randint(0, 100, size=(houses, colors))
    print(prices)
    print(min_cost(prices))
