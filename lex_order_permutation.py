#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 08:39:50 2018

 Given a number represented by a list of digits, find the next greater
 permutation of a number, in terms of lexicographic ordering. If there is
 not greater permutation possible, return the permutation with the lowest
 value/ordering.

For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should
return [2,1,3]. The list [3,2,1] should return [1,2,3].

Can you perform the operation without allocating extra memory (disregarding
the input memory)?

@author: carlgval
"""


def next_lex_permutation(array):
    ''' Method to calculate the next lexicographic permutation of an array.

    This method takes an array and returns its next lexicographic permutation.
    Note than the permutation is done in-place.

    Args:
        array (`list`): list of elements capable of comparison.

    Returns:
        `list`: same list with one permutation applied.'''

    for i in range(len(array) - 1, -1, -1):
        if array[i] > array[i-1]:
            break

    if i == 0:
        array.reverse()
        return array

    smallest_index = i
    for j in range(i+1, len(array)):
        if array[j] > array[i-1]:
            if array[j] < array[smallest_index]:
                smallest_index = j

    array[i-1], array[smallest_index] = array[smallest_index], array[i-1]

    for h, el in enumerate(sorted(array[i:])):
        array[i + h] = el

    return array


if __name__ == '__main__':
    array = [0, 1, 2, 3]

    for _ in range(30):
        print(next_lex_permutation(array))
