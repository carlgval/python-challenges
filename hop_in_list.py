#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 08:31:14 2018


Given an integer list where each number represents the number of hops you can
make, determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns true while [1, 1, 0, 1] returns false.


@author: carlgval
"""


def hop(l, idx=0):
    i = l[idx]

    if idx == len(l) - 1:
        return True
    elif i == 0:
        return False

    l[idx] = 0

    if hop(l, idx + i) or hop(l, idx - i):
        return True

    l[idx] = i
    return False


if __name__ == '__main__':
    l = [2, 0, 1, 0]
    print(hop(l))
    l = [1, 1, 0, 1]
    print(hop(l))
