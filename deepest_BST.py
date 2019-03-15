#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 08:57:08 2018

Given a tree, find the largest tree/subtree that is a BST.

Given a tree, return the size of the largest tree/subtree that is a BST.

@author: carlosgonzalez
"""


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

    def deeptest_BST(self):
        if self.is_searchable():
            return self.calculate_depth()[0]
        right = self.right.deeptest_BST()
        left = self.left.deeptest_BST()
        return max([right, left])

    def is_childless(self):
        if self.right is None and self.left is None:
            return True
        else:
            return False

    def is_searchable(self):
        status = True
        if self.right is not None and self.right.val >= self.val:
            status *= self.right.is_searchable()
        elif self.right is not None and self.right.val < self.val:
            status *= False
        if self.left is not None and self.left.val <= self.val:
            status *= self.left.is_searchable()
        elif self.left is not None and self.left.val > self.val:
            status *= False
        return bool(status)


if __name__ == '__main__':
    tree = Node(0,
                left=Node(-3,
                          left=Node(-5),
                          right=Node(-3)),
                right=Node(5,
                           left=Node(1),
                           right=Node(7)))
    print(tree)
    print('BST Depth: '),
    print(tree.deeptest_BST())

    tree = Node(0,
                left=Node(-3,
                          left=Node(-5),
                          right=Node(-3)),
                right=Node(5,
                           left=Node(6),
                           right=Node(7)))
    print(tree)
    print('BST Depth: '),
    print(tree.deeptest_BST())
