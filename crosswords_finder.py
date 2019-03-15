# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:09:46 2018
 Given a 2D matrix of characters and a target word, write a function that
 returns whether the word can be found in the matrix by going left-to-right,
 or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

and the target word 'FOAM', you should return true, since it's the leftmost
column. Similarly, given the target word 'MASS', you should return true,
since it's the last row.


@author: carlgval
"""


def solve_crosswords(m, word):
    word = word.lower()
    for row in m:
        if word in ''.join(row).lower():
            return True

    m2 = [[m[i][j] for i in range(len(m))] for j in range(len(m[0]))]
    for row in m2:
        if word in ''.join(row).lower():
            return True

    return False

if __name__ == '__main__':
    m = [['F', 'A', 'C', 'I'],
         ['O', 'B', 'Q', 'P'],
         ['A', 'N', 'O', 'B'],
         ['M', 'A', 'S', 'S']]
    word = 'FOAM'
    print(solve_crosswords(m, word))
    word = 'MASS'
    print(solve_crosswords(m, word))