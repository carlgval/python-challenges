#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 08:16:59 2018

 You are in an infinite 2D grid where you can move in any of the 8 directions:

    (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)

You are given a sequence of points and the order in which you need to cover
the points. Give the minimum number of steps in which you can achieve it.
You start from the first point.

Example:

Input: [(0, 0), (1, 1), (1, 2)]
Output: 2

It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move
from (1, 1) to (1, 2).

@author: carlgval
"""


def calculate_steps(steps):
    out = 0
    for i in range(len(steps) - 1):
        out += recursive_step(steps[i], steps[i + 1])
    return out


def recursive_step(pos, target):
    x, y = pos
    x_target, y_target = target

    if x == x_target and y == y_target:
        return 0

    delta_x = x_target - x
    delta_y = y_target - y

    next_x = x + (delta_x // abs(delta_x)) if delta_x != 0 else x
    next_y = y + (delta_y // abs(delta_y)) if delta_y != 0 else y

    return recursive_step((next_x, next_y), target) + 1


if __name__ == '__main__':

    steps = [(0, 0), (1, 1), (1, 2)]
    print(calculate_steps(steps))

    steps = [(0, 0), (5, 3), (-7, 2)]
    print(calculate_steps(steps))
