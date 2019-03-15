# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 08:30:28 2018

 Implement an LFU (Least Frequently Used) cache. It should be able to be
 initialized with a cache size n, and contain the following methods:

    set(key, value): sets key to value. If there are already n items in the
    cache and we are adding a new item, then it should also remove the least
    frequently used item. If there is a tie, then the least recently used key
    should be removed.

    get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.
@author: carlgval
"""


# Implementation of double linked list needed for object storage
class Double_Linked_List(object):
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next_node = self.tail
        self.tail.prev_node = self.head

    def _append(self, node):
        self.tail.prev_node.next_node = node
        node.prev_node = self.tail.prev_node
        self.tail.prev_node = node
        node.next_node = self.tail

    def append(self, value):
        node = Node(value)
        self.__append(node)

    def _pop(self, index=-1):
        i = 0
        if index >= 0:
            node = self.head.next_node
            while i < index:
                node = node.next_node
                i += 1
        else:
            i -= 1
            node = self.tail.prev_node
            while i > index:
                node = node.prev_node
                i -= 1
        node._disconect()
        return node


class Node(object):
    def __init__(self, value):
        self.prev_node = None
        self.next_node = None
        self.value = value
        self.frequency = 0

    def _disconect(self):
        self.prev_node.next_node = self.next_node
        self.next_node.prev_node = self.prev_node
        self.next_node = None
        self.prev_node = None


class LFU(object):
    def __init__(self, n):
        self.n = n
        self.values = {}
        self.frequencies = {}
        self.frequencies[1] = Double_Linked_List()

    def set(self, value, key):
        if key not in self.values:
            # Delete lfu item
            if len(self.values) >= self.n:
                self._evict()
            # Insert new item
            n = Node((key, value))
            self.values[key] = n
            self.frequencies[1]._append(n)
        else:
            # Update value and increase frequency
            n = self.values[key]
            n.value = (key, value)
            self._item_used(n)

    def get(self, key):
        if key in self.values:
            n = self.values[key]
            self._item_used(n)
            return n.value[1]
        else:
            return None

    def _evict(self):
        f = self.frequencies.values()[-1]
        n = f._pop()
        k, v = n.value
        self.values.pop(k)

    def _item_used(self, n):
        n.frequency += 1
        n._disconect()
        if n.frequency not in self.frequencies:
            self.frequencies[n.frequency] = Double_Linked_List()
        self.frequencies[n.frequency]._append(n)


if __name__ == '__main__':
    lfu = LFU(100000)
    for i in range(1000000):
        lfu.set(i * 10, i)

    print(lfu.get(i))
