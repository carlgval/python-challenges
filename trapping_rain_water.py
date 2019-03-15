# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 08:17:17 2018
 You are given an array of non-negative integers that represents a
 two-dimensional elevation map where each element is unit-width wall and the
 integer is the height. Suppose it will rain and all spots between two walls
 get filled up.

Compute how many units of water remain trapped on the map in O(N) time and
O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the
middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2
in the second, and 3 in the fourth index (we cannot hold 5 since it would run
off to the left), so we can trap 8 units of water.
@author: carlosgonzalez
"""

def holding_water(l):
    max_left = 0
    max_right = 0

    low = 0
    high = len(l) - 1
    out = 0

    while low <= high:
        if l[low] > l[high]:
            if l[high] > max_left:
                max_left = l[high]
            else:
                out += max_left - l[high]
            high -= 1
        else:
            if l[low] > max_right:
                max_right = l[low]
            else:
                out += max_right - l[low]
            low += 1

    return out




print(holding_water([5, 0, 1, 3, 0, 3]))