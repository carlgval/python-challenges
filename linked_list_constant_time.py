# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 08:20:44 2018
 Implement a stack that has the following methods:

    push(val), which pushes an element onto the stack
    pop(), which pops off and returns the topmost element of the stack. If
    there are no elements in the stack, then it should throw an error or
    return null.
    max(), which returns the maximum value in the stack currently. If there
    are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.

Implementation: Double linked list where the relative max values are saved for
each element
@author: carlgval
"""


class Member(object):
    def __init__(self,
                 parent_stack,
                 next_member=None,
                 prev_member=None,
                 value=None,
                 rmax=None):
        self.parent = parent_stack
        self.next_member = next_member
        self.prev_member = prev_member
        self.value = value

        self.rmax = rmax


class Stack(object):
    def __init__(self):
        self.first = None
        self.last = None
        self.max = None

    def push(self, val):
        if self.first is not None:
            rmax = max(val, self.first.rmax)
            new_element = Member(self,
                                 prev_member=self.first,
                                 value=val,
                                 rmax=rmax)
            self.first.next_member = new_element
        else:
            rmax = val
            new_element = Member(self,
                                 prev_member=self.first,
                                 value=val,
                                 rmax=rmax)
        self.first = new_element

    def _max(self):
        if self.first is not None:
            return self.first.rmax
        else:
            raise Exception('Empty stack')

    def pop(self):
        if self.first is not None:
            v = self.first.value
            self.first = self.first.prev_member
            if self.first is not None:
                self.first.next_member = None
            return v
        else:
            raise Exception('Empty stack')

if __name__ == '__main__':
    s = Stack()

    s.push(4)
    s.push(3)
    s.push(2)
    s.push(1)
    print(s._max())
    s.push(5)
    print(s._max())
    while True:
        print(s.pop())
