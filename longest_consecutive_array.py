#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 08:16:26 2018

Given an unsorted array of integers, find the length of the longest
consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element
sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

@author: carlgval
"""


def longest_consecutive_sequence(array):
    ''' Method to return the longest consecutive sequence length in an array

    This method creates a set of values from the array and iterates over the
    array, checking for an element if its subsequent elements are present.

    TODO: Improve performance droping values once visited. Recursive?

    Args:
        array (list): list of integers.

    Returns:
        int: length of the longest sequence.

    '''
    s = set(array)
    out = 0

    for el in array:
        consec_el = el + 1
        sequence = 0
        while (consec_el not in s):
            sequence += 1
            consec_el += 1

        out = max(out, sequence)

    return out


if __name__ == '__main__':

    array = [100, 4, 200, 1, 3, 2]

    print(longest_consecutive_sequence(array))
