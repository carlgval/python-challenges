#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 08:43:18 2019

 You have 100 fair coins and you flip them all at the same time. Any that
 come up tails you set aside. The ones that come up heads you flip again. How
 many rounds do you expect to play before only one coin remains?

Write a function that, given n, returns the number of rounds you'd expect to
play until one coin remains.

@author: carlgval
"""


def coins_flip(n):
    import math

    return int(round(math.log(n, 2)))


def test_coins_flip(n):
    import random

    rounds = 0

    while n > 1:
        results = [random.choice([0, 1]) for _ in range(n)]
        n = sum(results)
        rounds += 1

    return rounds


if __name__ == '__main__ ':
    import random

    for i in range(10):
        k = random.randint(10, 1000)
        print(k, coins_flip(k), test_coins_flip(k))

    for i in range(10):
        k = 100
        print(k, coins_flip(k), test_coins_flip(k))
