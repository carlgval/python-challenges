#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 08:37:17 2019

Given a circular array, compute its maximum subarray sum in O(n) time.

For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4,
and 8 where the 8 is obtained from wrapping around.

Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.

@author: carlgval
"""


def kadane(array):
    '''Kadane's algorithm

    Method to find the maximum subarray in an array in linear time.

    Args:
        array (:obj:`list` or :obj:`iterable`): array where to search

    Returns:
        int: max sum of subarray.
    '''
    # Init variables
    absolute_max = 0
    max_to_this_point = 0
    for el in array:
        # Add elements up to this point
        max_to_this_point += el
        # Do not count negative sums
        max_to_this_point = max(max_to_this_point, 0)
        # Get the max
        if max_to_this_point > absolute_max:
            absolute_max = max_to_this_point
    return absolute_max


def max_subarray_circular_array(array):
    ''' Method to find the max subarray in circular arrays.

    This method executes kadanes algorithm on the array and on the inverted
    array, thus calculating the min subarray and adding it to the sum of the
    array, to compensate the negative numbers.

    Args:
        array (:obj:`list` or :obj:`iterable`): array where to search

    Returns:
        int: max sum of subarray.
    '''
    # Execute one pass of Kadane's algorithm.
    absolute_max = kadane(array)
    # Execute anotrhe pass on the inverted array and add the sum of the array
    reversed_max = kadane([-a for a in array]) + sum(array)

    return max(absolute_max, reversed_max)


if __name__ == '__main__':
    array = [8, -1, 3, 4]
    print(max_subarray_circular_array(array))

    array = [-4, 5, 1, 0]
    print(max_subarray_circular_array(array))
