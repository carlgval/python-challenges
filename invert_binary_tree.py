# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 08:38:21 2018
 Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f

should become:

  a
 / \
 c  b
 \  / \
  f e  d

@author: carlgval
"""


import numpy as np


class Node(object):
    def __repr__(self, tab=0):
        out = '{} value={} \n'.format(self.__class__.__name__, self.val)
        if self.left:
            out += (tab + 1) * '  ' + \
                'left={}'.format(self.left.__repr__(tab + 1))
        if self.right:
            out += (tab + 1) * '  ' + \
                'right={}'.format(self.right.__repr__(tab + 1))
        return out

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def calculate_depth(self):
        depths = [(0, self)]
        if self.left:
            depths.append(self.left.calculate_depth())
        if self.right:
            depths.append(self.right.calculate_depth())

        depth, node = max(depths)
        return (depth + 1, node)

    def is_childless(self):
        if self.right is None and self.left is None:
            return True
        else:
            return False


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


def invert(tree):
    if tree.right:
        invert(tree.right)
    if tree.left:
        invert(tree.left)

    temp = tree.right
    tree.right = tree.left
    tree.left = temp

if __name__ == '__main__':
    t = random_tree(10)
    print(t)
    invert(t)
    print(t)
