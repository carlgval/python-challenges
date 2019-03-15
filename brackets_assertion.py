# -*- coding: utf-8 -*-
"""
 Given a string of round, curly, and square open and closing brackets,
 return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.

@author: carlgval
"""


brackets_encoder = {'(': 1,
                    ')': -1,
                    '[': 2,
                    ']': -2,
                    '{': 3,
                    '}': -3}


def assert_brackets(sentence):
    brackets = []
    for char in sentence:
        if char not in brackets_encoder:
            continue
        value = brackets_encoder[char]

        if value > 0:
            brackets.append(value)
        elif not brackets:
            return False
        elif (value + brackets[-1]) == 0:
            brackets.pop(-1)
        else:
            return False

    if brackets:
        return False
    else:
        return True

sentences = ["([])[]({})", "([)]", "((()"]

for sentence in sentences:
    print(sentence, assert_brackets(sentence))
