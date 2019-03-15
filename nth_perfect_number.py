# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 09:57:24 2018

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.

@author: carlgval
"""


def perfect_number(n):
    count = 1
    number = 19
    while count < n:
        number += 9
        if sum(int(i) for i in str(number)) == 10:
            count += 1
    return number


if __name__ == '__main__':

    for n in range(1, 100):
        pn = str(perfect_number(n))
        print(pn)
        assert sum(int(i) for i in pn) == 10
