#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 08:12:10 2019

 Given a string, return whether it represents a number. Here are the different
 kinds of numbers:

    "10", a positive integer
    "-10", a negative integer
    "10.1", a positive real number
    "-10.1", a negative real number
    "1e5", a number in scientific notation

And here are examples of non-numbers:

    "a"
    "x 1"
    "a -2"
    "-"

@author: carlgval
"""


def is_number(string):
    import re
    if re.match('^-.*[^=0-9\.].*', string):
        if re.match('[0-9]+e[0-9]+', string):
            return True
        return False
    return True


if __name__ == '__main__':
    print(is_number("10"))
    print(is_number("-10"))
    print(is_number("10.1"))
    print(is_number("-10.1"))
    print(is_number("1e5"))
