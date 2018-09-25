# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 08:12:28 2018


 You run an e-commerce website and want to record the last N order ids in a
 log. Implement a data structure to accomplish this, with the following API:

    record(order_id): adds the order_id to the log
    get_last(i): gets the ith last element from the log. i is guaranteed
        to be smaller than or equal to N.


@author: carlosgonzalez
"""
import numpy as np
from timeit import timeit
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

class circular_buffer(object):
    def __init__(self, size):
        self.index = 0
        self.items = [None] * size
        self.size = size

    def record(self, item):
        self.items[self.index] = item
        self.index += 1
        self.index = 0 if self.index >= self.size else self.index

    def get_last(self, i=1):
        out = []
        start_index = self.index - i
        if start_index < 0:
            out = self.items[start_index:] + self.items[:self.index]
        else:
            out = self.items[start_index:self.index]
        return out

'''
times = []
orders = [10**x for x in range(8)]
for order in orders:
    array = np.random.randint(0, 10*order, order)

    number = 42
    print(asdf(number, array))
    t = timeit(lambda: asdf(number, array), number=10) / 10
    times.append(t)

plt.semilogy(times)'''
