# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 08:12:28 2018

 The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext

The directory dir contains an empty sub-directory subdir1 and a sub-directory
subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\
    tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

The directory dir contains two sub-directories subdir1 and subdir2. subdir1
contains a file file1.ext and an empty second-level sub-directory subsubdir1.
subdir2 contains a second-level sub-directory subsubdir2 containing a file
file2.ext.

We are interested in finding the longest (number of characters) absolute path
to a file within our file system. For example, in the second example above,
the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its
length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the
length of the longest absolute path to a file in the abstracted file system.
If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

@author: carlosgonzalez
"""
import numpy as np
from timeit import timeit
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

class Tree(object):
    def __repr__(self, level=0):
        s = ''
        if self.children:
            for k, v in self.children.items():
                s += '  ' * level + k + '\n'
                s += v.__repr__(level + 1)
        return s

    def __init__(self, children={}, s=''):
        self.children = children
        self.name = s
        self.last_child = None

    @classmethod
    def new_child(cls):
        return cls({})

    def __getitem__(self, key):
        if key not in self.children.keys():
            self.children[key] = self.new_child()
        self.last_child = self.children[key]
        return self.children[key]

    def add_child(self, word):
        if word.startswith("\t"):
            self.last_child.add_child(word[1:])
        else:
            self.__getitem__(word)

    @classmethod
    def build_tree(cls, words):
        root = cls({})
        for word in words:
            root.add_child(word)
        return root

    def longest_path(self):
        longest_paths = []
        if self.children:
            for k, v in self.children.items():
                path = str(k)

                if '.' in str(path):
                    longest_paths.append(path)
                    continue

                path += '/' + str(v.longest_path())

                if '.' in str(path):
                    longest_paths.append(path)

            lengths = [(len(a), i) for i, a in enumerate(longest_paths)]
            lengths = sorted(lengths, reverse=True)

            return longest_paths[lengths[0][1]]
        else:
            return ''

t = ['dir',
     '\tsubdir1',
     '\t\tfile1.ext',
     '\t\tsubsubdir1',
     '\tsubdir2',
     '\t\tsubsubdir2',
     '\t\t\tfile2.ext']

tree = Tree.build_tree(t)
print(tree.longest_path())
