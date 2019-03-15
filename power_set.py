# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 08:37:30 2018

 The power set of a set is the set of all its subsets. Write a function that,
 given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return
{{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.

@author: carlgval
"""
import numpy as np


def power_set(s):
    numbers = np.array(list(s))
    l = range(2 ** len(s))
    return [list(numbers[to_bin(i, len(s))]) for i in l]


def to_bin(n, digits):
    return [int(x) == 1 for x in list(bin(n)[2:].zfill(digits))]


print(power_set({1, 2, 3}))
