# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 09:15:26 2018

 Given a dictionary of words and a string made up of those words (no spaces),
 return the original sentence in a list. If there is more than one possible
 reconstruction, return any of them. If there is no possible reconstruction,
 then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the
string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the
string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or
['bedbath', 'and', 'beyond'].

@author: carlgval
"""


def asdf(string, dictionary):
    if not string:
        return []

    for k in dictionary:
        if string.startswith(k):
            l = asdf(string[len(k):], dictionary)
            if l is not None:
                return [k] + l

    return None


if __name__ == "__main__":
    words = ['quick', 'brown', 'the', 'fox']
    string = "thequickbrownfox"

    print(asdf(string, words))

    words = ['bed', 'bath', 'bedbath', 'and', 'beyond']
    string = "bedbathandbeyond"

    print(asdf(string, words))

