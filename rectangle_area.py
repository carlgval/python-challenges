#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 09:09:48 2019

 Given two rectangles on a 2D graph, return the area of their intersection.
 If the rectangles don't intersect, return 0.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}

and

{
    "top_left": (0, 5),
    "dimensions" (4, 3) # width, height
}

return 6.

@author: carlgval
"""


def rectangle_intersection(rect_1, rect_2):
    ''' Method to calculate the intersection of two rectangles.

    Args:
        rect_1(:obj:`tuple` of :obj:`tuple` of int): Position and size of the
            firste rectangle. Shape: ((x, y), (x_size, y_size)).
        rect_1(:obj:`tuple` of :obj:`tuple` of int): Position and size of the
            firste rectangle. Shape: ((x, y), (x_size, y_size)).

    Returns:
        (int): Area of intersection
    '''
    x = max(rect_1[0][0], rect_2[0][0])
    y = max(rect_1[0][1], rect_2[0][1])
    x_2 = min(rect_1[0][0] + rect_1[1][0], rect_2[0][0] + rect_2[1][0])
    y_2 = min(rect_1[0][1] + rect_1[1][1], rect_2[0][1] + rect_2[1][1])
    return max((x - x_2) * (y - y_2), 0)


if __name__ == '__main__':
    rect_1 = ((1, 4), (3, 3))
    rect_2 = ((0, 5), (4, 3))
    print(rectangle_intersection(rect_1, rect_2))
