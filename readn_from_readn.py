# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 08:25:14 2018

 Using a read7() method that returns 7 characters from a file, implement
 readN(n) which reads n characters.

For example, given a file with the content “Hello world”, three read7()
returns “Hello w”, “orld” and then “”.

@author: carlgval
"""


class read7(object):
    def __init__(self):
        self.i = 0
        self.msg = "Hello world"

    def __call__(self):
        i = self.i
        self.i += 7
        return self.msg[i:(i+7)]


class readN(object):
    def __init__(self):
        self.msg = ""
        self.r = read7()

    def __call__(self, n):
        if len(self.msg) < n:
            self.msg += self.r()
        out, self.msg = self.msg[:n], self.msg[n:]
        return out


if __name__ == '__main__':
    r = readN()
    print(r(2))
    print(r(4))
    print(r(7))
