# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 16:23:02 2018


 An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster
than linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8,
return 4 (the index of 8 in the array).

@author: carlgval
"""

import numpy as np
from timeit import timeit
import matplotlib.pyplot as plt


def find_element(array, value):
    if array[len(array) // 2] == value:
        return len(array) // 2
    if array[0] < array[len(array) // 2]:
        if (array[len(array) // 2] > value) and array[0] < value:
            return find_element(array[:len(array) // 2], value)
        else:
            return find_element(array[len(array) // 2:], value) + len(array) // 2
    else:
        if (array[len(array) // 2] < value) and array[-1] > value:
            return find_element(array[len(array) // 2:], value) + len(array) // 2
        else:
            return find_element(array[:len(array) // 2], value)


if __name__ == '__main__':
    print(find_element([13, 18, 25, 2, 8, 10], 8))

    times = []
    orders = [10**x for x in range(1, 9)]

    for order in orders:
        a = np.arange(order)
        n = np.random.randint(0, order, 1)

        a = np.roll(a, n)

        assert find_element(a, 0) == int(n)
        t = timeit(lambda: find_element(a, 0), number=10) / 10
        times.append(t)

    plt.semilogy(times)
