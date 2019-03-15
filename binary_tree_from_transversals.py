# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 09:50:32 2018

 Given pre-order and in-order traversals of a binary tree, write a function
 to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g


@author: carlgval
"""


class Node(object):
    def __repr__(self):
        return '{}(value={!r}, left={!r}, right={!r})'.format(
            self.__class__.__name__, self.value, self.left, self.right)

    def __init__(self, value, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left

    @classmethod
    def from_inorder(cls, inorder, preorder):
        root = cls(preorder[0])

        if len(preorder) == 1:
            return root

        left_nodes_i = inorder[:inorder.index(root.value)]
        if len(left_nodes_i) > 0:
            left_nodes_p = preorder[:]
            for n in preorder:
                if n not in left_nodes_i:
                    left_nodes_p.remove(n)
            root.left = cls.from_inorder(left_nodes_i, left_nodes_p)

        right_nodes_i = inorder[inorder.index(root.value)+1:]
        if len(right_nodes_i) > 0:
            right_nodes_p = preorder[:]
            for n in preorder:
                if n not in right_nodes_i:
                    right_nodes_p.remove(n)
            root.right = cls.from_inorder(right_nodes_i, right_nodes_p)

        return root

tree = Node.from_inorder(['d', 'b', 'e', 'a', 'f', 'c', 'g'],
                         ['a', 'b', 'd', 'e', 'c', 'f', 'g'])
print(tree)
