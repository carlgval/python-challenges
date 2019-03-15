# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 08:28:14 2018

 Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]

You should print out the following:

1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12


@author: carlgval
"""


def print_spiral(m):
    i = 0
    j = 0
    di = 0
    dj = 1
    si = 0
    sj = 0
    ei = len(m) - 1
    ej = len(m[0]) - 1

    while (si < ei + 1) and (sj < ej + 1):
        print(m[i][j])

        if i == si and j == ej and di != 1 and dj!= 0:
            di = 1
            dj = 0
            si += 1
        elif i == ei and j == ej and di != 0 and dj!= -1:
            di = 0
            dj = -1
            ej -= 1
        elif i == ei and j == sj and di != -1 and dj!= 0:
            di = -1
            dj = 0
            ei -= 1
        elif i == si and j == sj and di != 0 and dj!= 1:
            di = 0
            dj = 1
            sj += 1

        i += di
        j += dj


if __name__ == '__main__':
    m = [[1,  2,  3,  4,  5],
         [6,  7,  8,  9,  10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20]]
    print_spiral(m)