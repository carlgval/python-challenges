# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 09:15:26 2018

 Given an array of time intervals (start, end) for classroom lectures
 (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

@author: carlgval
"""

import numpy as np
from timeit import timeit
import matplotlib.pyplot as plt
import sys


def asdf(times):
    starts, ends = zip(*times)

    max_rooms = 0
    starts = sorted(starts)
    ends = sorted(ends)
    rooms = 0

    for i in range(len(starts) + len(ends)):
        if starts and starts[0] <= ends[0]:
            rooms += 1
            starts.pop(0)
        else:
            rooms -= 1
            ends.pop(0)

        max_rooms = max(max_rooms, rooms)

    return max_rooms

if __name__=="__main__":
    l = [(30, 75), (0, 50), (60, 150)]
    print(asdf(l))