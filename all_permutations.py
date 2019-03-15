#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 09:49:09 2018

 Given a number in the form of a list of digits, return all possible
 permutations.

For example, given [1,2,3], return
[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].

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


def factor(number):
    if number == 1:
        return number
    else:
        return number * factor(number - 1)


def all_permutations(array):
    out = [list(array)]
    for _ in range(factor(len(array)) - 1):
        array = next_lex_permutation(array)
        out.append(list(array))
    return out


if __name__ == '__main__':
    array = [0, 1, 2, 3]

    print(all_permutations(array))
