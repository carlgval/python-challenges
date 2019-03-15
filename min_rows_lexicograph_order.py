# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 08:14:36 2018
 You are given an N by M 2D matrix of lowercase letters. Determine the minimum
 number of columns that can be removed to ensure that each row is ordered from
 top to bottom lexicographically. That is, the letter at each column is
 lexicographically later as you go down each row. It does not matter whether
 each row itself is ordered lexicographically.

For example, given the following table:

cba
daf
ghi

This is not ordered because of the a in the center. We can remove the second
column to make it ordered:

ca
df
gi

So your function should return 1, since we only needed to remove 1 column.

As another example, given the following table:

abcdef

Your function should return 0, since the rows are already ordered (there's
only one row).

As another example, given the following table:

zyx
wvu
tsr

Your function should return 3, since we would need to remove all the columns
to order it.
@author: carlgval
"""


def count_rows(matrix):
    columns = [1 for _ in range(len(matrix[0]))]

    for i_row in range(len(matrix) - 1):
        columns = [columns[j] * int(matrix[i_row][j] < matrix[i_row + 1][j])
                   for j in range(len(columns))]

    return columns.count(0)


if __name__ == '__main__':
    m = [['c', 'b', 'a'],
         ['d', 'a', 'f'],
         ['g', 'h', 'i']]
    print(count_rows(m))

    m = [['a', 'b', 'c', 'd', 'f']]
    print(count_rows(m))

    m = [['z', 'y', 'x'],
         ['w', 'v', 'u'],
         ['t', 's', 'r']]
    print(count_rows(m))
