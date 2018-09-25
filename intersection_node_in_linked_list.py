# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 09:15:26 2018

 Given two singly linked lists that intersect at some point, find the
 intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return
the node with value 8.

In this example, assume nodes with the same value are the exact same node
objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and
constant space.

@author: carlgval
"""

import numpy as np
from timeit import timeit
import matplotlib.pyplot as plt
import sys


class Node(object):
    def __init__(self, value, next_node):
        self.next_node = next_node
        self.value = value

    def count(self):
        if self.next_node is not None:
            return self.next_node.count() + 1
        else:
            return 1


def asdf(node_list_1, node_list_2):
    c = node_list_1.count() - node_list_2.count()

    for _ in range(abs(c)):
        if c > 0:
            node_list_1 = node_list_1.next_node
        else:
            node_list_2 = node_list_2.next_node

    while True:
        if node_list_1.value == node_list_2.value:
            return node_list_1.value
        else:
            node_list_1 = node_list_1.next_node
            node_list_2 = node_list_2.next_node


def linked_list(values):
    node = Node(values[-1], None)
    for i in values[:0:-1]:
        node = Node(i, node)
    return node


def test_case(order):

    array_1 = np.arange(order)
    np.random.shuffle(array_1)
    array_1 = array_1[:np.random.randint(0, order)]

    array_2 = np.arange(order, 2 * order)
    np.random.shuffle(array_2)
    array_2 = array_2[:np.random.randint(0, order)]

    array_3 = np.arange(2 * order, 3 * order)
    np.random.shuffle(array_3)
    array_3 = array_3[:np.random.randint(1, order)]

    intersection_node = array_3[0]

    list_1 = np.concatenate((array_1, array_3))
    list_2 = np.concatenate((array_2, array_3))

    return list_1, list_2, intersection_node


if __name__=="__main__":
    sys.setrecursionlimit(20000)
    times = []
    orders = [10**x for x in range(1, 5)]

    for order in orders:

        list_1, list_2 ,intersection = test_case(order)

        node_1 = linked_list(list_1)
        node_2 = linked_list(list_2)

        print(asdf(node_1, node_2), intersection)

        t = timeit(lambda: asdf(node_1, node_2), number=10) / 10
        times.append(t)

    plt.semilogy(times)