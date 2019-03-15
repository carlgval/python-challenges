# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 08:49:58 2018

 Given a string s and an integer k, break up the string into multiple texts
 such that each text has a length of k or less. You must break it up so that
 words don't break across lines. If there's no way to break the text up,
 then return null.

You can assume that there are no spaces at the ends of the string and that
there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog"
and k = 10, you should return: ["the quick", "brown fox", "jumps over",
"the lazy", "dog"]. No string in the list has a length of more than 10.

@author: carlgval
"""


def break_string(s, k):
    s = s.split()
    lines = []
    line = ''
    for word in s:
        if len(word) > k:
            return None
        if ((not line) and (not lines)):
            line = word
        elif ((len(line) + len(word) + 1) > k):
            lines.append(line)
            line = word
        else:
            line = line + ' ' + word

    if line:
        lines.append(line)

    return lines


if __name__ == '__main__':
    print(break_string("the quick brown fox jumps over the lazy dog", 10))
