#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 09:12:22 2019

Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢,
and a 1¢.

@author: carlgval
"""

import numpy as np


def min_number_of_coins(cents, valid_coins=[1, 5, 10, 25]):
    '''Method to return the min number of coins used for n cents.

    Given an integer n and a list of valid coins, this method returns the
    minimun number of coins needed to represent the quntity n.
    To do this, it creates an array that contains the min. number of coins to
    get 1 to n coins, calculating new values using the minimun of the old ones.

    Args:
        cent (int): number of cents to represent in coins.
        valid_coins (:obj:`list` of int): value of the valid coins.

    Returns:
        (int) number of coins used.
    '''

    table = np.array([float('inf') for i in range(cents + 1)])
    table[0] = 0

    valid_coins = np.array(valid_coins)

    for i in range(len(table)):
        for coin in valid_coins[valid_coins <= i]:
            if table[i - coin] != float('inf') and \
                    table[i] > (table[i - coin] + 1):
                table[i] = (table[i - coin] + 1)

    return int(table[-1])


if __name__ == '__main__':
    print(min_number_of_coins(100))
    print(min_number_of_coins(16))
    print(min_number_of_coins(52))
    print(min_number_of_coins(52))
