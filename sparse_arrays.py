#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 08:52:18 2019

 You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the
same interface:

    init(arr, size): initialize with the original large array and size.
    set(i, val): updates index at i with val.
    get(i): gets the value at index i.

@author: carlgval
"""

import random


class SparseArray(object):
    def __init__(self, array, size):
        self.size = size
        self.array = {}
        for i, el in enumerate(array):
            if el != 0:
                self.array[i] = el

    def __setitem__(self, key, val):
        if val != 0:
            self.array[key] = val

    def __getitem__(self, key):
        if key in self.array.keys():
            return self.array[key]
        else:
            return 0

    def __repr__(self):
        str_out = '['
        for i in range(self.size):
            if i in self.array.keys():
                str_out += str(self.array[i]) + ', '
            else:
                str_out += str(0) + ', '

        str_out += ']'
        return str_out

    def set(self, i, val):
        self.__setitem__(i, val)

    def get(self, i):
        self.__getitem__(i)


if __name__ == '__main__':
    array = [0 for i in range(100)]

    for i in range(10):
        array[random.randint(0, 99)] = random.randint(1, 99)

    print(array)
    sparse_array = SparseArray(array, len(array))
    print(sparse_array)

    for i in range(10):
        sparse_array[random.randint(0, 99)] = random.randint(1, 99)

    for i in range(10):
        print(sparse_array[random.randint(0, 99)])

    print(sparse_array)
