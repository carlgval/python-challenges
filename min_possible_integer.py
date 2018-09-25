# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 08:12:28 2018

Given an array of integers, find the first missing positive integer in linear
time and constant space. In other words, find the lowest positive integer that
does not exist in the array. The array can contain duplicates and negative
numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0]
should give 3.

You can modify the input array in-place.

@author: carlosgonzalez
"""
import numpy as np
from timeit import timeit
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



def asdf(array):
    l = len(array)

    index = 0
    for i in range(l):
        if array[i] < 0:
            temp = array[index]
            array[index] = array[i]
            array[i] = temp
            index +=1

    for i in range(index, l):
        if abs(array[i]) <= (l - index) and abs(array[i]) > 0:
            array[abs(array[i]) - 1 + index] = -abs(array[abs(array[i]) - 1 + index])

    for i in range(index, l):
        if array[i] > 0:
            return i - index + 1

    return (l - index + 1)

times = []
orders = [10**x for x in range(7)]

for order in orders:
    array = np.random.randint(-order, order, order*10)
    array2 = array.copy()
    assert(asdf(array) not in set(array2))
    t = timeit(lambda: asdf(array), number=10) / 10
    print(t)
    times.append(t)

plt.semilogy(times)
