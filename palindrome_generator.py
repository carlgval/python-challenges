# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 08:43:31 2018
 Given a string, find the palindrome that can be made by inserting the fewest
 number of characters as possible anywhere in the word. If there is more than
 one palindrome of minimum length that can be made, return the
 lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we
can add three letters to it (which is the smallest amount to make a
palindrome). There are seven other palindromes that can be made from "race"
by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
@author: carlgval
"""


def palindrome(s):
    # Find bending point
    idx = 0

    for i in range(len(s)):
        s_temp_1, s_temp_2 = s[:i], s[i:]
        if i < len(s) / 2:
            s_temp_1 = s_temp_1[::-1]
            if s_temp_2.startswith(s_temp_1):
                idx = i
        else:
            s_temp_2 = s_temp_2[::-1]
            if s_temp_1.endswith(s_temp_2):
                idx = i

    if idx > len(s) // 2:
        i = 2 * idx - len(s)
        out = s + s[:i][::-1]
    else:
        i = 2 * idx if idx != 0 else 1
        out = s[i:][::-1] + s

    return out

print(palindrome("google"))
print(palindrome("race"))
