# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 09:29:41 2018
 Implement regular expression matching with the following special characters:

    . (period) which matches any single character
    * (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular
expression and returns whether or not the string matches the regular
expression.

For example, given the regular expression "ra." and the string "ray", your
function should return true. The same regular expression on the string
"raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function
should return true. The same regular expression on the string "chats"
should return false.
@author: carlosgonzalez
"""


def re(text, expression):
    if len(text) == 0 and len(expression) == 0:
        return True
    elif len(text) == 0 or len(expression) == 0:
        return False

    expr, t = expression[0], text[0]
    if len(expression) > 1 and expression[1] == '*':
        results = []
        for i in range(len(text) - (len(expression)-2)):
            results.append(re(text[1:], ''.join([expr] * i) + expression[2:]))
        return any(results)
    elif expr == '.' or expr == t:
        return re(text[1:], expression[1:])
    else:
        return False





if __name__ == '__main__':
    print(re("ray", "ra."), 'True')
    print(re("raymond", "ra."), 'False')
    print(re("chat", ".*at"), 'True')
    print(re("chats", ".*at"), 'False')
