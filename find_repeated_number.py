#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 09:23:26 2019

You are given an array of length n + 1 whose elements belong to the set
{1, 2, ..., n}. By the pigeonhole principle, there must be a duplicate.
Find it in linear time and space.

@author: carlgval
"""


def find_repeated(array):
    """ Find repeated method

    This method takes an array of n elemnts whose values belong to the set
    {1-(n-1)}, and returns the repeated elements.

    Args:
        array (:obj:`list` of int): Array to be used.

    Returns:
        (:obj:`list` of int): Repeated elements.

    """
    repeated = []
    for i in range(len(array)):
        if array[abs(array[i])] > 0:
            array[abs(array[i])] *= -1
        else:
            repeated.append(abs(array[i]))
    return repeated


# Tests
if __name__ == '__main__':
    import random

    for i in range(10):
        n = random.randint(10**3, 10**6)
        array = list(range(1, n))

        repeated = [random.randint(0, n) for j in range(random.randint(1, 10))]
        array += repeated

        print('Testcase %i: n = %i, r = %s' % (i, n, str(repeated)))
        print(find_repeated(array))
