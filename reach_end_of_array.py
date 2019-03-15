#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 08:36:55 2019

 You are given an array of nonnegative integers. Let's say you start at the
 beginning of the array and are trying to advance to the end. You can advance
 at most, the number of steps that you're currently on. Determine whether you
 can get to the end of the array.

For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices
0 -> 1 -> 3 -> 5, so return true.

Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.

@author: carlgval
"""


# Method 1: recursive
def reachable_end(array):
    dead_ends = [False] * len(array)
    return _step(array, dead_ends, 0)


def _step(array, dead_ends, index):
    ''' Recursive method to test all cases

    Given an index, this method tries to advance [1, ..., n] steps in the
    array. If any of these movements leads to a solution.

    Args:
        array (:obj:`list` of int): The array being tested.
        dead_ends (:obj:`list` of bool): Already tested positions.
        index (int): The current index.

    Returns:
        (bool): If the end is reachable.
    '''
    # If the end is reached, return true
    if len(array) == (index + 1):
        return True
    # If it has been tried already or it is out of bounds, return false
    elif index >= len(array) or dead_ends[index]:
        return False
    # No more points: nowhere to go
    elif array[index] == 0:
        dead_ends[index] = True
        return False
    # Test all movements in array[index]
    else:
        for i in range(1, array[index] + 1):
            nex_index = index + i
            if _step(array, dead_ends, nex_index):
                return True
        dead_ends[index] = True
        return False


# Test
if __name__ == '__main__':
    array = [1, 3, 1, 2, 0, 1]
    print(reachable_end(array))

    array = [1, 2, 1, 0, 0]
    print(reachable_end(array))
