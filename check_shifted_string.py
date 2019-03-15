#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 08:53:14 2018

Given two strings A and B, return whether or not A can be shifted some number
of times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is
acb, return false.

@author: carlgval
"""


def check_shifted(s1, s2):
    temp_s = s1 + s1
    if len(s1) != len(s2) or s2 in temp_s:
        return True
    else:
        return False


if __name__ == '__main__':
    s1 = 'abc'
    s2 = 'cdeab'
    print(s1, s2, check_shifted(s1, s2))
