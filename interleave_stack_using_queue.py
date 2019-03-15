#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 09:08:29 2019
Given a stack of N elements, interleave the first half of the stack with the
second half reversed using only one other queue. This should be done in-place.

Recall that you can only push or pop from a stack, and enqueue or dequeue
from a queue.

For example, if the stack is [1, 2, 3, 4, 5], it should become
[1, 5, 2, 4, 3]. If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].

Hint: Try working backwards from the end state.
@author: carlgval
"""

from collections import deque


class Stack(deque):
    def __init__(self, *args):
        super(Stack, self).__init__(*args)
        self.push = self.append
        self.pop = self.pop


class Queue(deque):
    def __init__(self, *args):
        super(Queue, self).__init__(*args)
        self.enqueue = self.append
        self.dequeue = self.popleft


if __name__ == '__main__':
    N = 10
    n = list(range(N))
    s = Stack(n)
    q = Queue()
    print(s)
    for i in range(N - 1, 1, -1):
        for j in range(i):
            q.enqueue(s.pop())
        for j in range(i):
            s.append(q.dequeue())

    print(s)
