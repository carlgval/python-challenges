# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 08:36:03 2018

 Given an array of numbers, find the length of the longest increasing
 subsequence in the array. The subsequence does not necessarily have to be
 contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11,
7, 15], the longest increasing subsequence has length 6:
it is 0, 2, 6, 9, 11, 15.

@author: carlgval
"""


def count_longest(array):
    subsequences = [[]]
    subsequences.append([array[0]])

    for el in array[1:]:
        for i in range(len(subsequences)):
            subsequence = subsequences[i]
            if not subsequence or subsequence[-1] < el:
                subsequence_t = subsequence + [el]
                subsequences.append(subsequence_t)

    lenghts = [len(s) if s else 0 for s in subsequences]
    return subsequences[lenghts.index(max(lenghts))]


if __name__ == '__main__':
    array = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    print(count_longest(array))
