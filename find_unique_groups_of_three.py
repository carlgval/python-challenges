# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 10:58:48 2018
 Given an array of integers where every integer occurs three times except for
 one integer, which only occurs once, find and return the non-duplicated
 integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13],
return 19.

Do this in O(N) time and O(1) space.
@author: carlgval
"""

def find_unique(l):
    odd_times_bits = 0
    even_times_bits = 0

    for each in l:
        even_times_bits = even_times_bits | (odd_times_bits & each)
        odd_times_bits = odd_times_bits ^ each
        common_bit_mask = ~(odd_times_bits & even_times_bits)
        odd_times_bits &= common_bit_mask
        even_times_bits &= common_bit_mask

    return odd_times_bits