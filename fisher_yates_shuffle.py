# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 08:27:43 2018
 Given a function that generates perfectly random numbers between 1 and k
 (inclusive), where k is an input, write a function that shuffles a deck of
 cards represented as an array using only swaps.

It should run in O(N) time.

@author: carlgval
"""

import numpy as np
from timeit import timeit
import matplotlib.pyplot as plt

def rand(max_, min_=0):
    return int(np.random.randint(min_, max_ + 1, 1))


def shuffle(array):
    for i in range(len(array) - 1, -1, -1):
        swap_with = rand(i)

        temp = array[swap_with]

        array[swap_with] = array[i]
        array[i] = temp

    return array

if __name__ == '__main__':
    print(shuffle(list(range(10))))

    times = []
    orders = [10**x for x in range(7)]

    for order in orders:
        a = np.random.randint(0, 100, order)
        t = timeit(lambda: shuffle(a), number=10) / 10
        times.append(t)

    plt.semilogy(times)
