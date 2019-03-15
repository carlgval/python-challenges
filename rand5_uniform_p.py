# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 10:10:46 2018

Using a function rand7() that returns an integer from 1 to 7 (inclusive) with
uniform probability, implement a function rand5() that returns an integer from
1 to 5 (inclusive).

@author: carlgval
"""


import numpy as np
import matplotlib.pyplot as plt


def rand7():
    return int(np.random.randint(1, 8, 1))


def rand5():
    n = 6
    while n > 5:
        n = rand7()
    return n


if __name__ == '__main__':
    results = []
    for i in range(1000000):
        results.append(rand5())

    plt.hist(results)
