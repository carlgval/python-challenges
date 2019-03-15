#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 08:50:33 2018

 Given an even number (greater than 2), return two prime numbers whose sum
 will be equal to the given number.

A solution will always exist. See Goldbach’s conjecture.

Example:

Input: 4
Output: 2 + 2 = 4

If there are more than one solution possible, return the lexicographically
smaller solution.

If [a, b] is one solution with a <= b, and [c, d] is another solution with
c <= d, then

[a, b] < [c, d]

If a < c OR a==c AND b < d.

@author: carlgval
"""


def get_primes(end):
    primes = [2]
    for n in range(3, end, 2):
        if not primes or all([n % prime != 0 for prime in primes]):
            primes.append(n)

    return primes


def prime_sum(number):
    primes = set(get_primes(number))
    for p in primes:
        if (number - p) in primes:
            return (p, number - p)


if __name__ == '__main__':
    print(prime_sum(4))
    print(prime_sum(88))
    print(prime_sum(1116))
