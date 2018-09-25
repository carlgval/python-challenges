# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 08:12:28 2018

 Given an array of integers, return a new array such that each element at
 index i of the new array is the product of all the numbers in the original
 array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output
would be [2, 3, 6].

Follow-up: what if you can't use division?

@author: carlosgonzalez
"""
import numpy as np
from timeit import timeit
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def asdf_test(array):

    prod = np.prod(array, dtype=np.float128)
    temp = np.repeat(prod, len(array))

    return temp / array


def asdf(array):

    left = np.insert(np.cumprod(array)[:-1], 0, 1)
    right = np.append(np.flip(np.cumprod(np.flip(array, 0)), 0)[1:], 1)

    return right * left

times = []
orders = [x for x in range(2,50)]

for order in orders:
    array = np.random.randint(1, 10, order)
    prod = asdf(array)
    prod_test = asdf_test(array)
    print(all(prod == prod_test))
    t = timeit(lambda: asdf(array), number=100) / 100
    times.append(t)

plt.plot(times)
