#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Created on Tue Jan  8 08:24:28 2019

 Write a function that rotates a list by k elements. For example,
 [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2]. Try solving
 this without creating a copy of the list. How many swap or move operations
 do you need?

@author: carlgval
"""


def rotate_array(array, positions):

    positions = positions % len(array)

    for i in range(1, positions + 1):
        j = len(array) - i
        temp = array[positions - i]

        while j >= 0:
            array[j], temp = temp, array[j]
            j -= positions

    return array


if __name__ == '__main__':
    print(rotate_array(list(range(100)), 2))
    print(rotate_array(list(range(100)), 110))
