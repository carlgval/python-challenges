# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 12:26:36 2018


Given an unordered list of flights taken by someone, each represented as
(origin, destination) pairs, and a starting airport, compute the person's
itinerary. If no such itinerary exists, return null. If there are multiple
possible itineraries, return the lexicographically smallest one. All flights
must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'),
('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return
the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting
airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C']
even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the
first one is lexicographically smaller.
@author: carlgval
"""
from copy import deepcopy


def find_route(l, destine):
    origins, destines = zip(*l)

    if destine not in origins:
        return None
    elif len(destines) == 1:
        return list(destines)
    elif origins.count(destine) == 1:
        i = -1
        for _ in range(origins.count(destine)):
            l2 = deepcopy(l)
            i = origins.index(destine, i + 1)
            _, d = l2.pop(i)
            route = find_route(l2, d)
            if route is not None:
                return [str(d)] + route

    return None


def full_route(l):
    l = sorted(l)

    for i in range(len(l)):
        l2 = deepcopy(l)
        o, d = l2.pop(i)
        route = find_route(l2, d)
        if route is not None:
            return [str(o)] + [str(d)] + route

    return None


if __name__ is '__main__':
    print(full_route([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]))
    print(full_route([('SFO', 'HKO'), ('YYZ', 'SFO'),
                      ('YUL', 'YYZ'), ('HKO', 'ORD')]))
