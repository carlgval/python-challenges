# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 08:23:17 2018


 Assume you have access to a function toss_biased() which returns 0 or 1 with
 a probability that's not 50-50 (but also not 0-100 or 100-0). You do not know
 the bias of the coin.

Write a function to simulate an unbiased coin toss.

@author: carlgval
"""

import numpy as np


def toss_biased():
    a = np.random.random()
    return True if a > 0.6 else False


def toss_unbiased():
    a, b = False, False
    while a == b:
        a = toss_biased()
        b = toss_biased()
    return True if a else False


if __name__ == '__main__':
    results = [toss_unbiased() for i in range(100000)]

    print(np.sum(results))
