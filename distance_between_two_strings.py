# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 08:14:08 2018

 The edit distance between two strings refers to the minimum number of
 character insertions, deletions, and substitutions required to change one
 string to the other. For example, the edit distance between “kitten” and
 “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”,
 and append a “g”.

Given two strings, compute the edit distance between them.

@author: carlgval
"""


def compute_distance(s1, s2):
    i = 0
    j = 0

    distance = 0

    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
            j += 1

        else:
            a = compute_distance(s1[i:], s2[(j+1):])
            b = compute_distance(s1[(i+1):], s2[j:])
            c = compute_distance(s1[(i+1):], s2[(j+1):])

            distance += min(a, b, c) + 1
            return distance

    if i < len(s1):
        distance += len(s1) - i

    if j < len(s2):
        distance += len(s2) - j

    return distance

assert(compute_distance("sitting", "kitten") == 3)
assert(compute_distance("qwerasdf", "aqwerastf") == 2)
assert(compute_distance("zxcvft", "qwerat") == 5)
assert(compute_distance("qpwboeiruty", "añsldkfjbgh") == 10)
assert(compute_distance("asdf", "asdf") == 0)
