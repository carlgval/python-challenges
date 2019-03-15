#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 08:59:01 2018

 Given a list of integers and a number K, return which contiguous elements
 of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should
return [2, 3, 4].

@author: carlgval
"""


def contiguous_sum(l, objective):
    '''Method to find contiguous elements of a list that sum to n.

    Given a list and a integer n, this method iterates over the list,
    to find a subset of contiguous elements that sum n. If no subset is found,
    the method returns None.
    Args:
        l (`list` of int): list of elements to search.
        objective (int): value of the sum
    Returns:
        (`list` of int or None): subset of l that sums objective, or None if
            no subset is found.
    '''
    start = 0
    end = 0
    total_sum = 0

    while start != len(l):
        # print(start, end, total_sum)
        if total_sum == objective:
            return l[start:end]
        elif total_sum < objective and end != len(l):
            total_sum += l[end]
            end += 1
        else:
            total_sum -= l[start]
            start += 1

    return None


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    objective = 10

    print(contiguous_sum(l, objective))
