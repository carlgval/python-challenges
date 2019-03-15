#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 09:13:11 2019

 Given a real number n, find the square root of n. For example, given n = 9,
 return 3.

@author: carlgval
"""

import numpy as np
import math


def sqrt(n, max_digits=16):

    s = str(float(n))
    if s.rfind('.') % 2 != 0:
        s = '0' + s
    point_pos = s.rfind('.') / 2

    digits = list(s.replace('.', ''))

    remainder = int(''.join(digits[:2]))
    digits = digits[2:]
    digits_out = []

    while True:
        if not digits_out:
            front = 0
        else:
            front = int(''.join(digits_out)) * 20
        powers = (np.arange(0, 11) + front) * np.arange(0, 11)
        next_digit = str(max(np.argmax(powers > remainder) - 1, 0))
        digits_out.append(next_digit)
        remainder = remainder - (int(digits_out[-1]) + front)\
            * int(digits_out[-1])

        if len(digits) < 2:
            digits += ['0', '0']

        remainder = remainder * 100 + int(''.join(digits[:2]))
        digits = digits[2:]

        if (remainder == 0 and len(digits_out) >= point_pos) or \
                len(digits_out) >= (max_digits):
            break

    digits_out.insert(point_pos, '.')
    return ''.join(digits_out)


if __name__ == '__main__':
    def test(n):
        print(n, sqrt(n), math.sqrt(n))

    test_numbers = np.random.random(100) * 10000 + 1

    for n in test_numbers:
        test(n)
