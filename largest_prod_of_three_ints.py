# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 09:40:15 2018

 Given a list of integers, return the largest product that can be made by
 multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since
that's -10 * -10 * 5.

You can assume the list has at least three integers.
@author: carlgval
"""

def largest_product(l):
    l = sorted(l)
    positive = sum(i >= 0 for i in l)
    negative = len(l) - positive

    max_s = []

    if negative >= 2 and positive > 0:
        max_s.append(l[0]*l[1]*l[-1])
    else:
        max_s.append(l[-3]*l[-2]*l[-1])

    return max(max_s)


if __name__ == '__main__':
    l = [-10, -10, 5, 2]

    print(largest_product(l))
