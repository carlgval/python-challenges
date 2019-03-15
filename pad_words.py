# -*- coding: utf-8 -*-
"""

 Write an algorithm to justify text. Given a sequence of words and an integer
 line length k, return a list of strings which represents each line, fully
 justified.

More specifically, you should have as many words as possible in each line.
 There should be at least one space between each word. Pad extra spaces when
 necessary so that each line has exactly length k. Spaces should be
 distributed as equally as possible, with the extra spaces, if any,
 distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand
side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps",
 "over", "the", "lazy", "dog"] and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly

@author: carlgval
"""


def pad_words(sentence, k):
    out = []
    line = []
    line_length = 0

    for word in sentence:
        if (line_length + len(word)) > k:
            word_index = 0
            while line_length <= k:
                line[word_index] = line[word_index] + ' '
                line_length += 1
                if word_index < (len(line) - 2):
                    word_index = word_index + 1
                else:
                    word_index = 0
            out.append(' '.join(line))
            line = []
            line_length = 0

        line.append(word)
        line_length += len(word) + 1

    word_index = 0
    while line_length <= k:
        line[word_index] = line[word_index] + ' '
        line_length += 1
        if word_index < (len(line) - 2):
            word_index = word_index + 1
        else:
            word_index = 0
    out.append(' '.join(line))

    return out

sentence = ["the",
            "quick",
            "brown",
            "fox",
            "jumps",
            "over",
            "the",
            "lazy",
            "dog"]

print(pad_words(sentence, 16))
