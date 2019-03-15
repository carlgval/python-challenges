#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 08:22:49 2018

 A rule looks like this:

A NE B

This means this means point A is located northeast of point B.

A SW C

means that point A is southwest of C.

Given a list of rules, check if the sum of the rules validate. For example:

A N B
B NE C
C N A

does not validate, since A cannot be both north and south of C.

A NW B
A N B

is considered valid.

@author: carlosgonzalez

"""

import math


directions = {'N': [1, 0],
              'NE': [1, 1],
              'NW': [1, -1],
              'E': [0, 1],
              'W': [0, -1],
              'S': [1, 0],
              'SE': [-1, 1],
              'SW': [-1, -1],
              }


def validate_coordinates(rules):
    points = {}
    try:
        for rule in rules:
            rule = rule.split()
            p1 = rule[0]
            p2 = rule[2]
            d = directions[rule[1]]

            if not points:
                points[p1] = [0, 0]
            if p1 not in points and p2 not in points:
                rules.append(rule)
                continue
            if p1 not in points and p2 in points:
                p1, p2 = p2, p1
                d = [-i for i in d]
            if p1 in points and p2 not in points:
                points[p2] = [points[p1][0] - d[0],
                              points[p1][1] - d[1]]
            elif p1 in points and p2 in points:
                d2 = [points[p1][0] - points[p2][0],
                      points[p1][1] - points[p2][1]]
                for a, b in zip(d, d2):
                    assert (a == 0 and b == 0) or \
                        math.copysign(1, a) == math.copysign(1, b)
            else:
                raise Exception()
    except AssertionError:
        return False
    return True


if __name__ == '__main__':
    coords = ['A N B',
              'B NE C',
              'C N A']
    print('Test 1: %r = %r' % (validate_coordinates(coords), False))

    coords = ['A N B',
              'B NE C',
              'C S D',
              'D SW A']
    print('Test 2: %r = %r' % (validate_coordinates(coords), True))
