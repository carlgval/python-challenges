# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 09:08:48 2018

Given the head of a singly linked list, reverse it in-place.

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

    def reverse(self):
        prev_node = self.head
        node = prev_node.next_node
        prev_node.next_node = None

        while node.next_node is not None:
            n_node = node.next_node
            node.next_node = prev_node
            prev_node = node
            node = n_node

        node.next_node = prev_node
        self.tail = self.head
        self.head = node


class Node(object):
    def __repr__(self, i=0):
        if self.next_node:
            return '' * i + 'Node %i: %s \n' % (i, str(self.value)) \
                + self.next_node.__repr__(i+1)
        else:
            return ' ' * i + 'Node %i: %s \n' % (i, str(self.value))

    def __init__(self, value):
        self.next_node = None
        self.value = value

    def _disconect(self):
        self.next_node = None


if __name__ == '__main__':
    sll = Single_Linked_List()

    for i in range(100):
        sll.append(i)

    print(sll.head)
    sll.reverse()
    print(sll.head)

