#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 08:54:24 2019

 Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

  10
 /  \
5    5
 \     \
   2    1
       /
     -1


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

    def path_to_leaves(self):
        if self.is_childless():
            return [[self.val]]
        solutions = []
        if self.left:
            solutions += self.left.path_to_leaves()
        if self.right:
            solutions += self.right.path_to_leaves()
        out = [[self.val] + solution for solution in solutions]
        return out

    def min_path_to_leave(self):
        if self.right is None and self.left is None:
            return self.val
        elif self.right is None:
            return self.val + self.left.min_path_to_leave()
        elif self.left is None:
            return self.val + self.right.min_path_to_leave()
        else:
            return self.val + min(self.left.min_path_to_leave(),
                                  self.right.min_path_to_leave())


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


def print_nice(tree, indent=40, std_sep=1):
    print(' ' * indent + str(tree.val))
    indents = [indent]
    curr_level = [tree]
    n_level = 0
    while curr_level:
        spacer = [' '] * 80
        level = [' '] * 80
        next_level = []
        next_indents = []
        sep = std_sep
        for i, node in enumerate(curr_level):
            if node.right:
                right_sep_pos = indents[i] + sep
                right_val_pos = indents[i] + 2 * sep
                right_sep = '\\'
                if (spacer[right_sep_pos] != ' ' or
                        level[right_val_pos] != ' ') and not node.left:
                    right_sep_pos = indents[i] - sep
                    right_val_pos = indents[i] - 2 * sep
                    right_sep = '/'
                elif spacer[right_sep_pos] != ' ' or \
                        level[right_val_pos] != ' ':
                    right_sep_pos = indents[i]
                    right_val_pos = indents[i]
                    right_sep = '\\'
                spacer[right_sep_pos] = right_sep
                level[right_val_pos] = str(node.right.val)
                next_level.append(node.right)
                next_indents.append(indents[i] + 2 * sep)
            if node.left:
                left_sep_pos = indents[i] - sep
                left_val_pos = indents[i] - 2 * sep
                left_sep = '/'
                if (spacer[left_sep_pos] != ' ' or
                        level[left_val_pos] != ' ') and not node.right:
                    left_sep_pos = indents[i] + sep
                    left_val_pos = indents[i] + 2 * sep
                    left_sep = '\\'
                elif spacer[left_sep_pos] != ' ' or \
                        level[left_val_pos] != ' ':
                    left_sep_pos = indents[i]
                    left_val_pos = indents[i]
                    left_sep = '/'
                spacer[left_sep_pos] = left_sep
                level[left_val_pos] = str(node.left.val)
                next_level.append(node.left)
                next_indents.append(indents[i] - 2 * sep)

        sep = std_sep
        n_level += 1
        curr_level = next_level
        indents = next_indents
        print(''.join(spacer))
        print(''.join(level))


if __name__ == '__main__':
    tree = random_tree(10)

    print_nice(tree)

    print(tree.min_path_to_leave())
