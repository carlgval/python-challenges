# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 08:24:53 2018

Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0,
using only mathematical or bit operations. You can assume b can only be
1 or 0.

@author: carlgval
"""


def switch(b, x, y):
    '''Method to selct one of two variables depending on a boolean (T/F/0/1)

    Using a switch variable (b), and two option variables, select one one of
    the two variables depending of the value of b.

    Args:
        b (bool/int): variable used as switch.
        x (int): option true or 1.
        y (int): option false or 0.
    Returns:
        int: x if b and y if not b

    '''
    b = int(b)
    out = x * b
    b = int(not(b))
    out += y * b
    return out


if __name__ == '__main__':
    print(switch(True, 1, 1), 1)
    print(switch(False, 1, 2), 2)
    print(switch(1, 1, 1), 1)
    print(switch(0, 1, 2), 2)
