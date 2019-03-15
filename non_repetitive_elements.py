#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:14:57 2019

 Given an array of integers in which two elements appear exactly once and all
 other elements appear exactly twice, find the two elements that appear only
 once.


For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The
order does not matter.

@author: carlgval
"""


def non_repetive_elements(array):
    xor = 0

    for el in array:
        xor ^= el

    set_bit = 0
    i = 1
    print(xor)
    while set_bit == 0:
        if xor % (2 ** i) != 0:
            set_bit = 2 ** (i - 1)
        i += 1

    x, y = 0, 0
    for el in array:
        if el & set_bit:
            x ^= el
        else:
            y ^= el

    return x, y


if __name__ == '__main__':
    array = [2, 4, 6, 8, 10, 2, 6, 10]

    print((8, 4), non_repetive_elements(array))

    array = [2, 4, 3, 8, 10, 2, 8, 6, 10, 4]

    print((6, 3), non_repetive_elements(array))

    array = [2, 4, 6, 11, 8, 8, 10, 2, 6, 15, 10, 4]

    print((11, 15), non_repetive_elements(array))
