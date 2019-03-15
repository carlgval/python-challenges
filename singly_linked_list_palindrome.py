#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:06:28 2018

Determine whether a doubly linked list is a palindrome. What if it’s singly
 linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 returns true while 1 -> 4 returns false.

@author: carlgval
"""


class Node(object):
    def __repr__(self):
        if self.next is None:
            return "%s" % str(self.value)
        else:
            return "%s -> %s" % (str(self.value), self.next.__repr__())

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __len__(self):
        if self.next is None:
            return 1
        else:
            return len(self.next) + 1

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


def compare_lists(list_1, list_2):
    try:
        while list_1.next is not None or list_2.next is not None:
            assert list_1.value == list_2.value
            list_1 = list_1.next
            list_2 = list_2.next
        assert list_1.value == list_2.value
        assert list_1.next is None and list_2.next is None
    except AssertionError:
        return False
    return True


def split_list(l, n=None):
    if n is None:
        n = len(l)

    # Cut first half
    l1 = l
    i = 0
    temp_node = l
    while i < (n // 2 - 1):
        temp_node = temp_node.next
        i += 1
    l2 = temp_node.next.__copy__()

    if n % 2 == 0:
        temp_node.next = None
    else:
        temp_node.next.next = None

    return l1, l2


def reverse_list(l):
    l_next = l.next
    l_prev = None
    while l_next is not None:
        l_next = l.next

        l.next = l_prev

        l_prev = l
        l = l_next

    return l_prev


if __name__ == '__main__':
    l = Node(0)
    for i in range(1, 6):
        l.append(i)
    for i in range(4, -1, -1):
        l.append(i)
    print(l)
    print(len(l))
    l1, l2 = split_list(l)
    print(l1, l2)
    l2 = reverse_list(l2)
    print(l1, l2)
    print(compare_lists(l1, l2))
