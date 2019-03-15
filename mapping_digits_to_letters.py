# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 08:29:28 2018

 Given a mapping of digits to letters (as in a phone number), and a digit
 string, return all possible letters the number could represent. You can
 assume each valid number in the mapping is a single digit.

For example if {“2': [“a', “b', “c'], 3: [“d', “e', “f'], …} then “23' should
return [“ad', “ae', “af', “bd', “be', “bf', “cd', “ce', “cf"].

@author: carlgval
"""

mapping = {2: ['a', 'b', 'c'],
           3: ['d', 'e', 'f'],
           4: ['g', 'h', 'i'],
           5: ['j', 'j', 'l'],
           6: ['m', 'n', 'o'],
           7: ['p', 'q', 'r'],
           8: ['s', 't', 'u', 'w'],
           9: ['x', 'y', 'z'],}


def mapping_possibilities(digits):
    out = []
    for digit in digits:
        if not out:
            out = mapping[int(digit)]
            continue
        temp = out
        out = []
        for el in temp:
            out += [el + letter for letter in mapping[int(digit)]]

        return out


if __name__ == '__main__':
    print(mapping_possibilities('23'))
