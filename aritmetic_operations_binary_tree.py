# -*- coding: utf-8 -*-
"""

 Suppose an arithmetic expression is given as a binary tree. Each leaf is an
 integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5

You should return 45, as it is (3 + 2) * (4 + 5).

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

    def aritmetic_operations(self):
        if self.val == '*':
            return self.right.aritmetic_operations() * \
                self.left.aritmetic_operations()
        elif self.val == '+':
            return self.right.aritmetic_operations() + \
                self.left.aritmetic_operations()
        elif self.val == '-':
            return self.right.aritmetic_operations() - \
                self.left.aritmetic_operations()
        elif self.val == '/':
            return self.right.aritmetic_operations() / \
                self.left.aritmetic_operations()
        else:
            return int(self.val)


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


if __name__ == '__main__':
    root = Node('*', Node('+', Node(3), Node(2)), Node('+', Node(4), Node(5)))
    print(root.aritmetic_operations())
