#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 08:31:17 2019

 Let's represent an integer in a linked list format by having each node
 represent a digit in the number. The nodes make up the number in reversed
 order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5

is the number 54321.

Given two linked lists in this format, return their sum in the same linked
list format.

For example, given

9 -> 9

5 -> 2

return 124 (99 + 25) as:

4 -> 2 -> 1


@author: carlgval
"""


class Node:
    def __repr__(self):
        if self.next is not None:
            return str(self.value) + '->' + self.next.__repr__()
        else:
            return str(self.value)

    def __init__(self, value, next_node=None):
        self.next = next_node
        self.value = value

    def __add__(self, other):
        root = self.empty()
        self.sum_lists(self, other, root)
        return root

    @classmethod
    def empty(cls):
        e = cls(None)
        return e

    @classmethod
    def from_list(cls, l):
        if len(l) > 1:
            n = cls(l[0], cls.from_list(l[1:]))
        else:
            n = cls(l[0])
        return n

    @classmethod
    def sum_lists(cls, list_1, list_2, out, reminder=0):
        out.value = reminder
        if list_1 is not None:
            out.value += list_1.value
            list_1 = list_1.next
        if list_2 is not None:
            out.value += list_2.value
            list_2 = list_2.next

        reminder = 0
        if out.value >= 10:
            reminder = out.value // 10
            out.value = out.value % 10

        if list_1 or list_2 or reminder > 0:
            if out.next is None:
                out.next = cls(None)
            out = out.next
            cls.sum_lists(list_1, list_2, out, reminder)


if __name__ == '__main__':
    l1 = [5, 4, 3, 2, 1]
    n1 = Node.from_list(l1)
    l2 = [9, 9]
    n2 = Node.from_list(l2)
    print(n1, n2, n1 + n2)
