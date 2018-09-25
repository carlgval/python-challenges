# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 08:12:28 2018

@author: carlosgonzalez
"""
import numpy as np
from timeit import timeit
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def asdf(k, list_values):
    s = set()
    for each in list_values:
        temp = k - each
        if (temp > 0) and temp in s:
            return("The a pair %i and %i that sums %i" % (each, temp, k))
        s.add(temp)
    return("No pair found")

times = []
orders = [10**x for x in range(8)]
for order in orders:
    array = np.random.randint(0, 10*order, order)

    number = 42
    print(asdf(number, array))
    t = timeit(lambda: asdf(number, array), number=10) / 10
    times.append(t)

plt.semilogy(times)
