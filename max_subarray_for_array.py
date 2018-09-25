# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 08:12:28 2018

 Given an array of integers and a number k, where 1 <= k <= length of the
 array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get:
10, 7, 8, 8], since:

    10 = max(10, 5, 2)
    7 =  max(5, 2, 7)
    8 =  max(2, 7, 8)
    8 =  max(7, 8, 7)

Do this in O(n) time and O(k) space. You can modify the input array in-place
and you do not need to store the results. You can simply print them out as
you compute them.


@author: carlosgonzalez
"""

import numpy as np
from timeit import timeit
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from collections import deque


def asdf(list_values, k):
    q = deque()
    l = len(list_values)

    for i in range(k):
        while q and list_values[i] >= list_values[q[-1]]:
            q.pop()
        q.append(i)

    for i in range(k, l):
        yield list_values[q[0]]

        while q and q[0] <= (i - k):
            q.popleft()

        while q and list_values[i] >= list_values[q[-1]]:
            q.pop()

        q.append(i)

    yield list_values[q[0]]

    raise StopIteration()


if __name__=="__main__":
    arr = [12, 1, 78, 90, 57, 89, 56]
    k = 3
    print(list(asdf(arr, k)))

