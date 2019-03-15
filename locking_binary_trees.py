# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 08:12:28 2018

 Implement locking in a binary tree. A binary tree node can be locked or
 unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

    is_locked, which returns whether the node is locked
    lock, which attempts to lock the node. If it cannot be locked, then it
    should return false. Otherwise, it should lock it and return true.
    unlock, which unlocks the node. If it cannot be unlocked, then it should
    return false. Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers or any other property you
 would like. You may assume the class is used in a single-threaded program,
 so there is no need for actual locks or mutexes. Each method should run in
 O(h), where h is the height of the tree.


@author: carlosgonzalez
"""
import numpy as np


class Node(object):
    def __repr__(self):
        return '{}(value={!r}, left={!r}, right={!r}, locked={})'.format(
            self.__class__.__name__,
            self.val,
            self.left,
            self.right,
            self.locked)

    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        if left is not None:
            self.left.parent = self
        self.right = right
        if right is not None:
            self.right.parent = self
        self.parent = parent
        self.locked = False
        self.children_locked = 0

    def is_locked(self):
        return self.locked

    def lock(self):
        if self.can_be_locked() and not self.locked:
            self.locked = True
            self.child_has_locked(1)
            return True
        else:
            return False

    def unlock(self):
        if self.can_be_locked() and self.locked:
            self.locked = False
            self.child_has_locked(-1)
            return True
        else:
            return False

    def has_parent_locked(self):
        if self.parent:
            return self.parent.locked or self.parent.has_parent_locked()
        else:
            return False

    def can_be_locked(self):
        if self.children_locked > 0 or self.has_parent_locked():
            return False
        else:
            return True

    def child_has_locked(self, count):
        if self.parent:
            self.parent.children_locked += count
            self.parent.child_has_locked(count)

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
                    ends[0].right = Node(np.random.randint(min_val, max_val),
                                         parent=ends[0])
                    ends.append(ends[0].right)
                else:
                    ends[0].left = Node(np.random.randint(min_val, max_val),
                                        parent=ends[0])
                    ends.append(ends[0].left)
            elif ends[0].right is None:
                ends[0].right = Node(np.random.randint(min_val, max_val),
                                     parent=ends[0])
                ends.append(ends[0].right)
                _ = ends.pop(0)
            elif ends[0].left is None:
                ends[0].left = Node(np.random.randint(min_val, max_val),
                                    parent=ends[0])
                ends.append(ends[0].left)
                _ = ends.pop(0)
            node_count += 1
        else:
            ends.append(ends.pop(0))

    return root

if __name__ == '__main__':

    n = 20
    tree = random_tree(n, max_val=1)
    print(countUnivalTree(tree))
