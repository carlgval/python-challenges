# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 08:31:17 2018

 Given an array of integers, write a function to determine whether the array
 could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can
modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any
one element to get a non-decreasing array.

@author: carlgval
"""


def count_non_decreasing(array):
    count = 0

    for i in range(len(array) - 1):
        count += 1 if array[i] > array[i + 1] else 0

    return count


def check_non_decreasing(array):
    if count_non_decreasing(array) <= 1:
        return True
    else:
        return False


if __name__ == '__main__':
    print(check_non_decreasing([10, 5, 7]))
    print(check_non_decreasing([10, 5, 1]))
