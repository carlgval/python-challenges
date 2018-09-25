# -*- coding: utf-8 -*-
txt = """
Created on Tue Sep  4 08:12:28 2018
 Implement an autocomplete system. That is, given a query string s and a set
 of all possible query strings, return all strings in the set that have s as
 a prefix.

For example, given the query string de and the set of strings
[dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure
to speed up queries.


@author: carlosgonzalez
"""


class Tree(object):
    def __repr__(self, level=0):
        s = ''
        if self.children:
            for k, v in self.children.items():
                s += '  ' * level + k + ':' + str(v.suggested_words) + '\n'
                s += v.__repr__(level + 1)
        return s

    def __init__(self, children={}, words=[], count=[]):
        self.children = children
        self.suggested_words = words
        self.count = count

    @classmethod
    def new_child(cls):
        return cls({}, [], [])

    def __getitem__(self, key):
        if key not in self.children.keys():
            self.children[key] = self.new_child()
        return self.children[key]

    def add_words(self, words):
        for word in words:
            tree = self
            for letter in word:
                if word not in tree.suggested_words:
                    tree.suggested_words.append(word)
                    tree.count.append(1)
                else:
                    tree.count[tree.suggested_words.index(word)] += 1
                tree = tree[letter]

    def autocomplete(self, s):
        tree = self
        if s[0] in tree.children.keys():
            tree = tree.children[s[0]]
            s = s[1:]

            if len(s) > 0:
                return tree.autocomplete(s)
            else:
                return zip(*sorted(zip(tree.count,
                                       tree.suggested_words),
                                   reverse=True))[1]
        else:
            return []


for c in ['.', ',', ':', '@', '[', ']', '\n']:
    txt = txt.replace(c, ' ')
words = txt.split()

t = Tree()
t.add_words(words)
t
