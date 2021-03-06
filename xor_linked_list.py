# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 08:12:28 2018

 An XOR linked list is a more memory efficient doubly linked list. Instead of
 each node holding next and prev fields, it holds a field named both, which is
 an XOR of the next node and the previous node. Implement an XOR linked list;
 it has an add(element) which adds the element to the end, and a get(index)
 which returns the node at index.

If using a language that has no pointers (such as Python), you can assume
you have access to get_pointer and dereference_pointer functions that
converts between nodes and memory addresses.


@author: carlosgonzalez
"""
def likes(names):
    if len(names) <= 0:
        s = 'no one '
    if len(names) == 1:

class Node:
    "ASDFASDFASDF"
    def __repr__(self):
        return '{}(value={!r}, left={!r}, right={!r})'.format(self.__class__.__name__, self.val, self.left, self.right)

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def serialize(self):
        serial = [self.val]

        if self.left is not None:
            serial += self.left.serialize()
        else:
            serial += ['#']

        if self.right is not None:
            serial += self.right.serialize()
        else:
            serial += ['#']

        return serial

    @classmethod
    def deserialize(cls,serial):
        def _walker(index):
            if serial[index] == '#':
                return None, index + 1

            value = serial[index]
            left, index = _walker(index + 1)
            right, index = _walker(index)

            return cls(value,left,right), index
        return _walker(0)[0]

import numpy as np
from timeit import timeit
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


np.prod

times = []
max_nodes = [x for x in range(2,50)]

for n_nodes in max_nodes:
    node_count = 0
    #TODO
    array = np.random.randint(1, 10, order)
    prod = asdf(array)
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'

plt.plot(times)
