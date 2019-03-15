#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 08:14:54 2019

 Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd
 bit should be swapped, the 3rd and 4th bit should be swapped, and so on.

For example, 10101010 should be 01010101. 11100010 should be 11010001.

Bonus: Can you do this in one line?

@author: carlgval
"""


def swap_bits(binary_string):
    l = list(binary_string)
    l = [l[(i//2 * 2):((i//2 + 1) * 2)][::-1][i % 2] for i in range(len(l))]
    return l


if __name__ == '__main__':
    l = '10101010'
    print(l, swap_bits(l))

    l = '11100010'
    print(l, swap_bits(l))
