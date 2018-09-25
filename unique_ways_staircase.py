# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 08:12:28 2018
 There exists a staircase with N steps, and you can climb up either 1 or 2
 steps at a time. Given N, write a function that returns the number of unique
 ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could
climb any number from a set of positive integers X? For example, if X =
{1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

@author: carlosgonzalez
"""
import numpy as np
from timeit import timeit
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def asdf(stairs, steps={1, 2}):

    ways = 0
    for s in steps:
        if s == stairs:
            ways += 1
        elif s > stairs:
            ways += 0
        else:
            ways += asdf(stairs - s, steps)

    return ways

def count(n,steps={1,2}):
    steps = set(steps)
    return asdf(n, steps)

# %%
def fib(n, steps):
    if n <= 1:
        if n < 0:
            return 0
        else:
            return n
    count = 0
    for s in steps:
        count += fib(n-s,steps)
    return count

# returns no. of ways to reach s'th stair
def countWays(s,steps={1,2}):
    return fib(s + 1,steps)

# %%


times = []
orders = [10**x for x in range(2)]
for order in orders:

    number = order
    steps={1,3,5}
    assert count(number,steps) == countWays(number, steps)
    t = timeit(lambda: asdf(number), number=10) / 10
    times.append(t)

plt.semilogy(times)
