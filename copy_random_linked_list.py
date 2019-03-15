#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 09:26:42 2019

 Given the head to a singly linked list, where each node also has a “random”
 pointer that points to anywhere in the linked list, deep clone the list.

@author: carlgval
"""

import random


class Node(object):
    def __repr__(self):
        if self.next is None:
            return "%s ^R(%s)" % (str(self.value), str(self.random.value))
        else:
            return "%s ^R(%s) -> %s" % (str(self.value),
                                        str(self.random.value),
                                        self.next.__repr__())

    def __init__(self, value, next_node=None, random_node=None):
        self.value = value
        self.next = next_node
        self.random = random_node

    def __len__(self):
        if self.next is None:
            return 1
        else:
            return len(self.next) + 1

    def __getitem__(self, index):
        if index < 0 or (self.next is None and index > 0):
            raise ValueError('Invalid index')
        elif index == 0:
            return self
        else:
            return self.next[index - 1]

    @classmethod
    def new_node(cls, value):
        return cls(value, None)

    def __copy__(self):
        return Node(self.value, self.next)

    def append(self, value):
        if self.next is None:
            self.next = self.new_node(value)
        else:
            self.next.append(value)


def copy_list(linked_list):
    l1 = linked_list
    curr = linked_list
    while curr is not None:
        curr.next = Node(curr.value, curr.next, curr.random)
        curr = curr.next.next

    curr = l1
    while curr is not None:
        curr.next.random = curr.random.next
        curr = curr.next.next

    curr = l1
    l2 = curr.next
    curr2 = l2
    while curr2.next is not None:
        curr.next, curr2.next = curr2.next, curr2.next.next

        curr = curr.next
        curr2 = curr2.next

    return l1, l2


if __name__ == '__main__':
    l = Node(0)
    for i in range(1, 10):
        l.append(i)

    for i in range(0, 10):
        l[i].random = l[random.randint(0, 9)]
    print(l)
    _, l2 = copy_list(l)
    print(l2)
