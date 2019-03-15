# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 08:44:03 2018

 Given k sorted singly linked lists, write a function to merge all the lists
 into one sorted singly linked list.

@author: carlgval
"""


class Node:
    def __repr__(self):
        if self.next is not None:
            return str(self.value) + '\n' + self.next.__repr__()
        else:
            return str(self.value)

    def __init__(self, value, next_node=None):
        self.next = next_node
        self.value = value

    @classmethod
    def from_list(cls, l):
        if len(l) > 2:
            n = cls(l[0], cls.from_list(l[1:]))
        else:
            n = cls(l[0])
        return n


def merge_2_lists(list_1, list_2):
    if list_2 is None:
        return list_1
    elif list_1 is None:
        return list_2

    if list_1.value < list_2.value:
        n = list_1
        list_1.next = merge_2_lists(list_1.next, list_2)
    else:
        n = list_2
        list_2.next = merge_2_lists(list_1, list_2.next)

    return n


def merge_k_lists(lists):
    out = None
    for l in lists:
        out = merge_2_lists(l, out)

    return out


if __name__ == '__main__':
    import numpy as np

    k = np.random.randint(2, 10)
    lengths = np.random.randint(2, 10, k)
    starts = np.random.randint(0, 1000, k)
    ends = np.random.randint(10, 100, k)

    lists = [np.arange(starts[i],
                       ends[i]+starts[i],
                       ends[i]/lengths[i]) for i in range(k)]

    n = [Node.from_list(l) for l in lists]
    m = merge_k_lists(n)
    print(m)
