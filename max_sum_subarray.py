# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 12:13:06 2018

 Given an array of numbers, find the maximum sum of any contiguous subarray
 of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would
be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would
not take any elements.

Do this in O(N) time.

@author: carlgval
"""


def max_sum_subarray(array):
    max_sum = 0
    curr_sum = 0
    for e in array:
        curr_sum += e

        if curr_sum > max_sum:
            max_sum = curr_sum
        elif curr_sum < 0:
            curr_sum = 0

    return max_sum


print(max_sum_subarray([34, -50, 42, 14, -5, 86]))
print(max_sum_subarray([-5, -1, -8, -9]))
