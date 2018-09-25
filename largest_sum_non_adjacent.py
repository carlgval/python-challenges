# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 08:12:28 2018

 Given a list of integers, write a function that returns the largest sum of
 non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
@author: carlosgonzalez
"""
import numpy as np
from timeit import timeit
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def asdf(list_values):
    incl = list_values[0]
    excl = 0

    for value in list_values[1:]:
        prev_incl = incl
        incl = excl + value
        excl = max(prev_incl, excl)

    return max(incl, excl)

times = []
orders = [10**x for x in range(8)]
for order in orders:
    array = np.random.randint(-10, 10, order)
    largest_sum = asdf(array)
    print(largest_sum)
    t = timeit(lambda: asdf(array), number=10) / 10
    times.append(t)

plt.semilogy(times)
