#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 12:33:06 2018

What does the below code snippet print out? How can we fix the anonymous
functions to behave as we'd expect?

@author: carlgval
"""

functions = []
for i in range(10):
    functions.append(lambda i=i: i)

for f in functions:
    print(f())
