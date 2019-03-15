#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 15:15:49 2019


Given the head of a singly linked list, swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.

@author: carlgval
"""


class Single_Linked_List(object):
    def __init__(self, value=None):
        self.head = Node(value)
        self.tail = self.head

    def _append(self, node):
        self.tail.next_node = node
        self.tail = node

    def append(self, value):
        node = Node(value)
        self._append(node)


class Node(object):
    def __repr__(self, i=0):
        if self.next_node is not None:
            return '' * i + 'Node %i: %s \n' % (i, str(self.value)) \
                + self.next_node.__repr__(i+1)
        else:
            return ' ' * i + 'Node %i: %s \n' % (i, str(self.value))

    def __init__(self, value):
        self.next_node = None
        self.value = value

    def _disconect(self):
        self.next_node = None

    def swap(self):
        if self is not None and self.next_node is not None:
            temp = self.next_node
            self.next_node = self.next_node.next_node
            temp.next_node = self

            self.next_node = self.next_node.swap()

            return temp
        else:
            return self


if __name__ == '__main__':
    sll = Single_Linked_List()

    for i in range(100):
        sll.append(i)
    s = sll.head.swap()
    print(s)
