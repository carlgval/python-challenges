# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 08:56:54 2018



Given a string, find the longest palindromic contiguous substring. If there
are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The
longest palindromic substring of "bananas" is "anana".

@author: carlgval
"""


def find_longest_palindrome(string):
    # Fill a triangular table[i,j] with 1 if pal. of length j is found in i
    table = [[None for i in range(len(string)-j)] for j in range(len(string))]
    for i in range(len(string)):
        for j in (range(len(string) - i)):
            if string[j] == string[j + i]:
                table[i][j] = 1
            else:
                table[i][j] = 0
    # Max length of pal. is found with the index of the rows != 0
    lengths = [r.count(1) for r in table]
    lengths.reverse()
    longest_length = len(lengths) - lengths.index(1)
    # Start point of the pal is found in first index with value != 0
    longest_index = table[longest_length - 1].index(1)

    return string[longest_index:(longest_index + longest_length)]

print(find_longest_palindrome("aabcdcb"))
print(find_longest_palindrome("bananas"))
