#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:17:16 2018

Given an integer n and a list of integers l, write a function that randomly
generates a number from 0 to n-1 that isn't in l (uniform).

Assumptions:
    + all(l) in range(1, n)
    + all(l) are unique
    + l is sorted
@author: carlgval

"""


from random import randint


def new_number(l, n):
    index = randint(0, n - len(l) - 1)

    return not_in(l, index)

def not_in(l, index):
    search_point = len(l) // 2
    not_picked_behind = l[search_point] - search_point
    if not_picked_behind <= index:
        if len(l[search_point:]) <= 2:
            return list(range(l[search_point] + 1, l[search_point + 1]))[index - not_picked_behind - 1]
        else:
            return not_in(l[search_point:], index - not_picked_behind)
    else:
        if len(l[:search_point]) <= 2:
            return list(range(l[0], l[1]))[index]
        else:
            return not_in(l[:search_point], index)

if __name__ =='__main__':
    l = [1, 4, 7]
    n = 10

    print(new_number(l, n))
