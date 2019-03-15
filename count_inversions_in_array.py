# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 08:10:06 2018

 We can determine how "out of order" an array A is by counting the number of
 inversions it has. Two elements A[i] and A[j] form an inversion if
 A[i] > A[j] but i < j. That is, a smaller element appears after a larger
 element.

Given an array, count the number of inversions it has. Do this faster than
O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5]
has three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1]
has ten inversions: every distinct pair forms an inversion.

@author: carlgval
"""
import numpy as np
from timeit import timeit
import matplotlib.pyplot as plt


def merge(array1, array2):
    ordered = [None] * (len(array1) + len(array2))
    i = 0
    j = 0
    k = 0

    count = 0

    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            ordered[k] = array1[i]
            i += 1
            k += 1
        else:
            ordered[k] = array2[j]
            j += 1
            k += 1
            count += len(array1) - i

    while i < len(array1):
        ordered[k] = array1[i]
        i += 1
        k += 1
    while j < len(array2):
        ordered[k] = array2[j]
        j += 1
        k += 1

    return count, ordered


def count_inversions(array):
    if len(array) > 1:
        inversions = 0
        middle_point = len(array) // 2

        inv_left, left = count_inversions(array[:middle_point])
        inv_right, right = count_inversions(array[middle_point:])
        inv_merge, sorted_array = merge(left, right)

        inversions = inv_left + inv_right + inv_merge
        return inversions, sorted_array
    else:
        return 0, array

a = [2, 4, 1, 3, 5]
b = [5, 4, 3, 2, 1]
print(count_inversions(a))
print(count_inversions(b))

if __name__ == '__main__':

    times = []
    orders = [10*x for x in range(100)]

    for order in orders:
        a = np.arange(order)[::-1]
        print(count_inversions(a)[0])
        t = timeit(lambda: count_inversions(a), number=10) / 10
        times.append(t)

    plt.semilogy(times)
