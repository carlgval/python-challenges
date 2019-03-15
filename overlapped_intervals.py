# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 08:35:03 2018

 Given a list of possibly overlapping intervals, return a new list of
 intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return
[(1, 3), (4, 10), (20, 25)].

@author: carlgval
"""


def overlap_intervals(array):
    stack = []
    array = sorted(array)
    for el in array:
        if not stack or el[0] > stack[-1][-1]:
            stack.append(el)
        elif el[-1] > stack[-1][-1]:
            stack[-1] = (stack[-1][0], el[-1])

    return stack


if __name__ == '__main__':
    i = [(1, 3), (5, 8), (4, 10), (20, 25)]
    print(overlap_intervals(i))
