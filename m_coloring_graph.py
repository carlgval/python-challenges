# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 16:21:44 2018

Given an undirected graph represented as an adjacency matrix and an integer
k, write a function to determine whether each vertex in the graph can be
colored such that no two adjacent vertices share the same color using at
most k colors.

@author: carlgval
"""

from copy import deepcopy


def can_be_colored(m, k):
    colors = [0 for i in range(len(m))]
    if coloring(m, colors, k):
        return True, colors
    return False


def check_neighbours(n, k, c):
    for i, each in enumerate(n):
        if each == 1 and k[i] == c:
            return False
    return True


def coloring(m, colors, k, v=0):
    if v == len(m):
        return True

    for color in range(1, k + 1):
        if check_neighbours(m[v], colors, color):
            colors[v] = color
            if coloring(m, colors, k, v+1):
                return True
            colors[v] = 0

if __name__ == '__main__':
    m = [[0,1,1,1], [1,0,1,0], [1,1,0,1], [1,0,1,0]]
    k = 3
    print(can_be_colored(m, k))
