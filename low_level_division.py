#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 08:23:36 2018


Implement division of two positive integers without using the division,
multiplication, or modulus operators. Return the quotient as an integer,
ignoring the remainder.

@author: carlosgonzalez
"""


def integer_division(divident, divisor, quotient=0):
    """Low-level division for integers.

    Perform a division using recurrent differences between the divident and
    the divisor.

    Args:
        divident (int): Divident of the division. a in the expresion a/b.
        divisor (int): Divisor of the division. b in the expresion a/b.
        quotient (int): Argument used for recursion.

    Returns:
        int: integer with the result of the division.

    """
    if divident >= divisor:
        return integer_division(divident - divisor,
                                divisor,
                                quotient + 1)
    else:
        return quotient


if __name__ == '__main__':
    print("Test: %i=%i" % (9//3, integer_division(9, 3)))
    print("Test: %i=%i" % (2//3, integer_division(2, 3)))
    print("Test: %i=%i" % (17//3, integer_division(17, 3)))
