# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 09:03:55 2018

 Given a multiset of integers, return whether it can be partitioned into two
 subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return
true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which
both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't
split it up into two subsets that add up to the same sum.
@author: carlgval
"""

from copy import deepcopy


def subset_is_sum(a, s):
    if sum(a) == s:
        return True, a

    elif sum(a) > s:
        for i in range(len(a)):
            temp = a.pop(i)
            result, a_2 = subset_is_sum(a, s)
            if result:
                return True, a_2
            a.append(temp)
    return False, a


def check_subsets(array):
    try:
        s = int(sum(array) / 2.)
    except:
        return False
    a_2 = deepcopy(array)
    r, a = subset_is_sum(array, s)
    if r:
        for each in a:
            a_2.remove(each)
        return a, a_2
    else:
        return False

if __name__ == '__main__':
    print(check_subsets([15, 5, 20, 10, 35]))
    print(check_subsets([15, 5, 20, 10, 35, 15, 10]))
