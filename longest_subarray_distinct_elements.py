#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 08:18:49 2019


Given an array of elements, return the length of the longest subarray where
all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the
longest subarray of distinct elements is [5, 2, 3, 4, 1].

@author: carlgval
"""


def longest_subarray(array):
    ''' Method to find the longest subarray of distinct elements in an array

    This method iterates over the array, storing the elements in two data
    structures: a set, to check if an element belongs to the subarray, and a
    list, to store the order of the elements.

    Time complexity: O(1)
    Space complexity: O(2)

    Args:
        array (:obj:`list`): array where the subarray will be searched

    Returns:
        int: length of the longest subarray where all its elements are
            distinct.
    '''
    # Init data structures
    subarray_s = set()
    subarray_l = list()
    max_subarray = 0

    # For each new element
    for el in array:
        # Discard elements in order until it is not present in the array
        while el in subarray_s:
            subarray_s.remove(subarray_l.pop(0))

        # Add the element to the data structures
        subarray_s.add(el)
        subarray_l.append(el)

        # If the subarray is longer than the previous, update the value.
        if len(subarray_s) > max_subarray:
            max_subarray = len(subarray_s)

    return max_subarray, subarray_l


if __name__ == '__main__':
    array = [5, 1, 3, 5, 2, 3, 4, 1]
    print(longest_subarray(array))
