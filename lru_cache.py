# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 08:30:28 2018

 Implement an LRU (Least Recently Used) cache. It should be able to be
 initialized with a cache size n, and contain the following methods:

    set(key, value): sets key to value. If there are already n items in the
        cache and we are adding a new item, then it should also remove the
        least recently used item.

    get(key): gets the value at key. If no such key exists, return null.

@author: carlgval
"""


class LRU(object):
    def __init__(self, n):
        self.n = n
        self.values = {}
        self.keys = []

    def set(self, value, key):
        if len(self.keys) >= self.n:
            self.values.pop(self.keys.pop(-1))

        self.keys.insert(0, key)
        self.values[key] = value

    def get(self, key):
        if key in self.keys:
            self.keys.insert(0, self.keys.pop(self.keys.index(key)))
            return self.values[key]
        else:
            return None


if __name__ == '__main__':
    lru = LRU(5)
    for i in range(10):
        lru.set(i * 10, i)

    print(lru.values)
    print(lru.get(i))
