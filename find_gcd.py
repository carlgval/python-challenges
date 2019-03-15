#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 08:25:47 2019

 Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14.

@author: carlgval
"""


def common_denominator(iterator):
    ''' Method to apply gcd to all items in an iterator

    Args:
        iterator(:obj:`list`): Numbers to search

    Returns:
        (int): Greatest common denominator
    '''
    out = iterator[0]
    for i in iterator[1:]:
        out = gcd(out, i)
    return out


def gcd(a, b):
    ''' Recursive method to calculate the gcd of two numbers '''
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def common_denominator2(iterator):
    ''' Method to find the denominators of item 0 and then test the rest of
    number for them

    Args:
        iterator(:obj:`list`): Numbers to search

    Returns:
        (int): Greatest common denominator
    '''
    denominators = [i for i in range(1, iterator[0]) if iterator[0] % i == 0]

    for i in iterator[1:]:
        denominators = [d for d in denominators if i % d == 0]
    return max(denominators)


# TESTs
if __name__ == '__main__':
    import random

    n = 1000
    test_gcd = random.randint(10, 100)
    iterator = [random.randint(1, n) * test_gcd for _ in range(n)]

    print('Test value: %i, out: %i' % (test_gcd,
                                       common_denominator(iterator)))
    print('Test value: %i, out: %i' % (test_gcd,
                                       common_denominator2(iterator)))

    # Timing
    from timeit import timeit
    import matplotlib.pyplot as plt
    times, times2 = [], []
    orders = [10**x for x in range(1, 7)]

    for order in orders:
        test_gcd = random.randint(10, 100)
        iterator = [random.randint(1, order) * test_gcd for _ in range(order)]

        t = timeit(lambda: common_denominator(iterator), number=10) / 10
        t2 = timeit(lambda: common_denominator2(iterator), number=10) / 10

        times.append(t)
        times2.append(t2)

    plt.semilogy(times, label='Method 1')
    plt.semilogy(times2, label='Method 1')
    plt.legend()
