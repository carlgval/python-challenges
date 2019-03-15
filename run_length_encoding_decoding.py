# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 08:21:52 2018
 Run-length encoding is a fast and simple method of encoding strings. The
 basic idea is to represent repeated successive characters as a single count
 and character. For example, the string "AAAABBBCCDAA" would be encoded as
 "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be
encoded have no digits and consists solely of alphabetic characters. You can
assume the string to be decoded is valid.
@author: carlosgonzalez
"""


def run_length_encoding(string):
    count = 1
    out = ''
    for i, char in enumerate(string):
        if i < len(string)-1 and char == string[i+1]:
            count += 1

        else:
            out += str(count) + char
            count = 1
    return out


def run_length_decoding(string):
    out = ''
    for i, char in enumerate(string):
        if char.isdigit():
            for _ in range(int(char)):
                out += string[i+1]
    return out

s = "AAAABBBCCDAA"
print(s)
print(run_length_encoding(s))
assert s == run_length_decoding(run_length_encoding(s))
