# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 08:34:21 2018

 Given a string of parentheses, write a function to compute the minimum number
 of parentheses to be removed to make the string valid (i.e. each open
 parenthesis is eventually closed).

For example, given the string "()())()", you should return 1. Given the
string ")(", you should return 2, since we must remove all of them.

@author: carlgval
"""


def check_parentheses(s):
    '''Method to count not closed parentheses

    Args:
        s (str): String to count parentheses.

    Returns:
        int: count of not-closed parentheses
    '''

    opened = 0
    count = 0
    for char in s:
        if char == '(':
            opened += 1
        elif char == ')':
            if opened > 0:
                opened -= 1
            else:
                count += 1

    return count + opened


if __name__ == '__main__':
    print(check_parentheses('()())()'))
    print(check_parentheses(')('))
    print(check_parentheses('))))'))
    print(check_parentheses('(((('))
    print(check_parentheses('()()()()()'))
    print(check_parentheses('(((())))'))
