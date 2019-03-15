#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 08:18:51 2019

 Implement 3 stacks using a single list:

class Stack:
    def __init__(self):
        self.list = []

    def pop(self, stack_number):
        pass

    def push(self, item, stack_number):
        pass

@author: carlgval
"""

import random


class Stack:
    def __init__(self, k=3):
        self.list = []
        self.start = [0 for i in range(k)]
        self.size = [0 for i in range(k)]

    def pop(self, stack_number):
        if not self.size[stack_number]:
            return None

        idx = self.start[stack_number] + self.size[stack_number] - 1

        item = self.list.pop(idx)

        for i in range(stack_number + 1, len(self.start)):
            self.start[i] -= 1
        self.size[stack_number] -= 1

        return item

    def push(self, item, stack_number):
        idx = self.start[stack_number] + self.size[stack_number]
        self.list.insert(idx, item)

        for i in range(stack_number + 1, len(self.start)):
            self.start[i] += 1
        self.size[stack_number] += 1


if __name__ == '__main__':
    s = Stack(3)

    for i in range(100):
        j = random.randint(0, 2)
        s.push(i * 10**j, j)

    for j in range(1000):
        i = random.randint(0, 2)
        item = s.pop(i)
        if item is not None:
            print(i, item)
