# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 08:46:27 2018

 On our special chessboard, two bishops attack each other if they share the
 same diagonal. This includes bishops that have another bishop located
 between them, i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M
chessboard. Write a function to count the number of pairs of bishops that
attack each other. The ordering of the pair doesn't matter: (1, 2) is
considered the same as (2, 1).

For example, given M = 5 and the list of bishops:

    (0, 0)
    (1, 2)
    (2, 2)
    (4, 0)

The board would look like this:

[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]

You should return 2, since bishops 1 and 3 attack each other, as well as
bishops 3 and 4.

@author: carlgval
"""


from math import factorial


def count_bishops(bishops):
    counts = 0

    # Count top_left_ to bottom_right
    bishops_temp = [a - b for a, b in bishops]
    c = {x: bishops_temp.count(x) for x in bishops_temp}

    for v in c.values():
        if v > 1:
            counts += factorial(v) / 2

    # Count bottom_left_ to top_right
    bishops_temp = [a + b for a, b in bishops]
    c = {x: bishops_temp.count(x) for x in bishops_temp}

    for v in c.values():
        if v > 1:
            counts += factorial(v) / 2

    return counts


if __name__ == '__main__':
    bishops = [(0, 0),
               (1, 2),
               (2, 2),
               (4, 0)]
    print(count_bishops(bishops))
