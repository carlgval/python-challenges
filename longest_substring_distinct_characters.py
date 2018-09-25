# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 08:12:28 2018

 Given an integer k and a string s, find the length of the longest substring
 that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k
distinct characters is "bcb".

@author: carlosgonzalez
"""
import numpy as np
from timeit import timeit
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def asdf(k, s):
    window = []
    longest = ''
    longest_count = 0

    i = 0

    while i < len(s):
        c = s[i]

        if (c in window) or (len(set(window)) < k):
            window.append(c)
            i += 1

        else:
            window.pop(0)

        if len(window) > longest_count:
            longest_count = len(window)
            longest = ''.join(window)

    return longest

print(asdf(2,"abcba"))
