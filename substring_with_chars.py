#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 09:17:38 2018

 Given a string and a set of characters, return the shortest substring
 containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i},
you should return "aeci".

If there is no substring containing all the characters in the set, return null.

@author: carlgval
"""


def substring_with_chars(l, chars_set):
    '''Method to find a substring that contains a set of chars.

    Given a string and a set of chars, this method iterates over the string,
    to find a substring that contains all chars. If no subset is found,
    the method returns None, else, it returns the shortest substring.
    Args:
        l (str): string to search.
        chars_set (set): set of chars to find
    Returns:
        (str or None): substring of l, or None if no substring is found.
    '''
    start = 0
    end = 0
    smallest = ''
    chars_occurrence = {c: 0 for c in chars_set}

    while start != len(l):
        # print(start, end, l[start:end])

        # Try to minimize window
        if all([el > 0 for el in chars_occurrence.values()]):
            if l[start] not in chars_set:
                start += 1
            elif chars_occurrence[l[start]] > 1:
                chars_occurrence[l[start]] -= 1
                start += 1
            else:
                if smallest == '' or len(l[start:end]) < len(smallest):
                    smallest = l[start:end]
                chars_occurrence[l[start]] -= 1
                start += 1

        # Find a window that contains all chars
        elif end < len(l):
            if l[end] in chars_set:
                chars_occurrence[l[end]] += 1
            end += 1

        else:
            start += 1

    if smallest == '':
        return None
    else:
        return smallest


if __name__ == '__main__':
    l = "figehaeci"
    chars = {'a', 'e', 'i'}

    print(substring_with_chars(l, chars))
