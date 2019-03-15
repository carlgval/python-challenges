# -*- coding: utf-8 -*-
"""

 Given a singly linked list and an integer k, remove the kth last element from
 the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.

@author: carlgval
"""
import random


class Item(object):
    def __repr__(self):
        if self.child is not None:
            return ("Node_value = %d, Node Child = \n" % self.value) \
                + self.child.__repr__()
        else:
            return ("Node_value = %d, No children" % self.value)

    def __init__(self, value, child=None):
        self.value = value
        self.child = child

    @classmethod
    def new_item(cls, value, child=None):
        return cls(value, child)

    def new_child(self, child_value, childs_child=None):
        self.child = self.new_item(child_value, childs_child)


def random_list(items=20):
    root = Item(random.randint(1, 100))
    node = root
    for i in range(items - 1):
        node.new_child(random.randint(1, 100))
        node = node.child
    return root


def delete_index(root, index):
    if index == 0:
        root = root.child
    else:
        node = root
        while index >= 1:
            if index == 1:
                node.child = node.child.child
            index -= 1
            node = node.child
    return root


from timeit import timeit
import matplotlib.pyplot as plt

times = []
max_nodes = [10**x for x in range(2, 8)]
for n in max_nodes:
    l = random_list(n)

    index = n/2

    t = timeit(lambda: delete_index(l, index), number=10) / 10
    times.append(t)
    print(t)

plt.semilogy(times)
#plt.plot(times)
