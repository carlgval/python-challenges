# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 09:34:47 2018

 Implement integer exponentiation. That is, implement the pow(x, y) function,
 where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
@author: carlgval
"""
import numpy as np
from timeit import timeit
import matplotlib.pyplot as plt


def power(x, y):
    if y == 0:
        return 1
    elif y % 2 == 0:
        temp = power(x, y/2)
        return temp * temp
    else:
        temp = power(x, y/2)
        return temp * temp * x


if __name__ == '__main__':
    print(power(2, 10))

    times = []
    orders = [10*x for x in range(1, 1000)]

    for order in orders:
        n = 2
        t = timeit(lambda: power(n, order), number=10) / 10
        times.append(t)

    plt.semilogy(times)
