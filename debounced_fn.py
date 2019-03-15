#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 08:24:22 2018
 Given a function f, and N return a debounced f of N milliseconds.

That is, as long as the debounced f continues to be invoked, f itself will
not be called for N milliseconds.

@author: carlgval
"""


from time import time, sleep


class debounce(object):
    def __init__(self, fn, miliseconds):
        self.last_call = float(0)
        self.fn = fn
        self.timeout = float(miliseconds) / 1000

    def __call__(self, *args):
        if (time() - self.last_call) > self.timeout:
            out = self.fn(*args)
            self.last_call = time()
            return out
        else:
            return None


if __name__ == '__main__':

    fn = lambda x, y: x + y

    debounced_fn = debounce(fn, 20)

    print(debounced_fn(3, 4))
    print(debounced_fn(3, 4))
    sleep(0.020)
    print(debounced_fn(3, 4))
