# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 08:34:21 2018

 Implement a queue using two stacks. Recall that a queue is a FIFO (first-in,
 first-out) data structure with the following methods: enqueue, which inserts
 an element into the queue, and dequeue, which removes it.


@author: carlgval
"""


class Fifo(object):
    # Define two empty stacks
    stack_1 = []
    stack_2 = []

    # When enqueuing, push the element into the first stack
    def enqueue(self, el):
        self.stack_1.append(el)

    # When dequeuing, check if the second stack is empty, if it is, dump all
    # contents of the first stack, inverting the order. Finally, pop an elem.
    def dequeue(self):
        if not self.stack_2:
            for i in range(len(self.stack_1)):
                self.stack_2.append(self.stack_1.pop())
        return self.stack_2.pop()


if __name__ == '__main__':
    f = Fifo()
    f.enqueue(1)
    f.enqueue(2)
    f.enqueue(3)

    print(f.dequeue())
    print(f.dequeue())
    f.enqueue(4)
    f.enqueue(5)
    print(f.dequeue())
    print(f.dequeue())
    print(f.dequeue())
