#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 08:31:53 2019

 You're given a string consisting solely of (, ), and *. * can represent
 either a (, ), or an empty string. Determine whether the parentheses are
 balanced.

For example, (()* and (*) are balanced. )*( is not balanced.

@author: carlgval
"""


def is_balanced(string, char='*'):
    if not string or string.count(char) == len(string):
        return True

    out = False

    if string[0] == char:
        out |= is_balanced(string[1:])

    if string[-1] == char:
        out |= is_balanced(string[:-1])

    if string[0] != ')' and string[-1] != '(':
        out |= is_balanced(string[1:-1])

    return out


if __name__ == '__main__':
    s = '(()*'
    print(s, is_balanced(s))

    s = '(*)'
    print(s, is_balanced(s))

    s = ')*('
    print(s, is_balanced(s))
