# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 09:23:42 2018
 Given an array of strictly the characters 'R', 'G', and 'B', segregate the
 values of the array so that all the Rs come first, the Gs come second, and
 the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should
become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
@author: carlgval
"""


def order_rgb(l):
    first = 0
    last = len(l) - 1
    i = 0
    while last > first:
        if l[i] == 'R':
            l[first], l[i] = l[i], l[first]
            first += 1
        elif l[i] == 'G':
            i += 1
        elif l[i] == 'B':
            l[last], l[i] = l[i], l[last]
            last -= 1
    return l

print(order_rgb(['G', 'B', 'R', 'R', 'B', 'R', 'G']))

