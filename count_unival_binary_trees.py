# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 08:12:28 2018

 Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all
nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1



@author: carlosgonzalez
"""
import numpy as np


class Node(object):
    def __repr__(self):
        return '{}(value={!r}, left={!r}, right={!r})'.format(
            self.__class__.__name__, self.val, self.left, self.right)

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
    def deserialize(cls, serial):
        def _walker(index):
            if serial[index] == '#':
                return None, index + 1

            value = serial[index]
            left, index = _walker(index + 1)
            right, index = _walker(index)

            return cls(value, left, right), index
        return _walker(0)[0]

    def is_childless(self):
        if self.right is None and self.left is None:
            return True
        else:
            return False

    def get_children(self):
        children = []
        if self.right is not None:
            children.append(self.right)
        if self.left is not None:
            children.append(self.left)
        return children


def find_branches(node, branches):
    if node.is_childless():
        branches.append(node)
    else:
        for n in node.get_children():
            _ = find_branches(n, branches)
    return branches


def get_branches(root):
    branches = []
    return find_branches(root, branches)


def countUnival(node, count):
    if node is None:
        return True
    right = countUnival(node.right, count)
    left = countUnival(node.left, count)

    if not(left and right):
        return False

    if node.right and node.right.val != node.val:
        return False

    if node.left and node.left.val != node.val:
        return False

    count[0] += 1
    return True


def countUnivalTree(root):
    count = [0]
    countUnival(root, count)
    return count[0]


def random_tree(n_nodes, max_val=10, min_val=0):
    max_val += 1
    node_count = 1
    ends = []
    root = Node(np.random.randint(min_val, max_val))
    ends.append(root)

    while (node_count < n_nodes):
        if np.random.choice(2):
            if ends[0].is_childless():
                if np.random.choice(2):
                    ends[0].right = Node(np.random.randint(min_val, max_val))
                    ends.append(ends[0].right)
                else:
                    ends[0].left = Node(np.random.randint(min_val, max_val))
                    ends.append(ends[0].left)
            elif ends[0].right is None:
                ends[0].right = Node(np.random.randint(min_val, max_val))
                ends.append(ends[0].right)
                _ = ends.pop(0)
            elif ends[0].left is None:
                ends[0].left = Node(np.random.randint(min_val, max_val))
                ends.append(ends[0].left)
                _ = ends.pop(0)
            node_count += 1
        else:
            ends.append(ends.pop(0))

    return root


from timeit import timeit
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

times = []
max_nodes = [10**x for x in range(1, 6)]
for n in max_nodes:

    tree = random_tree(n, max_val=1)
    print(countUnivalTree(tree))
    t = timeit(lambda: countUnivalTree(tree), number=10) / 10
    times.append(t)

plt.semilogy(times)
#plt.plot(times)
