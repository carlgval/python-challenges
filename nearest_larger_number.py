#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 14:56:22 2019

 Given an array of numbers and an index i, return the index of the nearest
 larger number of the number at index i, where distance is measured in array
 indices.

For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

If two distances to larger numbers are the equal, then return any one of them.
If the array at i doesn't have a nearest larger integer, then return null.

If you can preprocess the array, can you do this in constant time?

@author: carlgval
"""


class Next_number(object):
    def __init__(self, lst):
        self.map = {}
        self.lst = lst
        for i, l in enumerate(lst):
            if l not in self.map.keys():
                self.map[l] = [i]
            else:
                self.map[l] += [i]
        self.sorted = sorted(self.map.keys())

    def __call__(self, idx):
        if self.sorted[-1] <= self.lst[idx]:
            return None

        for i in self.sorted:
            if i > self.lst[idx]:
                break

        dist = float('inf')
        nearest = None
        for each in self.map[i]:
            if abs(each - idx) < dist:
                dist = abs(each - idx)
                nearest = each
        return nearest


if __name__ == '__main__':
    lst = [4, 1, 3, 5, 6]
    n = Next_number(lst)

    print(n(0))
