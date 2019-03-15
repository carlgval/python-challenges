# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 09:44:48 2018

Using a function rand5() that returns an integer from 1 to 5 (inclusive) with
uniform probability, implement a function rand7() that returns an integer from
1 to 7 (inclusive).

@author: carlgval
"""
import numpy as np
import matplotlib.pyplot as plt


def rand5():
    return int(np.random.randint(1, 6, 1))

def rand7():
    x = rand5() * 5 + rand5() - 5
    if x < 22:
        return (x % 7) + 1
    else:
        return rand7()

results = []
for i in range(1000000):
    results.append(rand7())

plt.hist(results)