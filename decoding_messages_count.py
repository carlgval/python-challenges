# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 08:12:28 2018



Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count
the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as
'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not
allowed.

@author: carlosgonzalez
"""
import re


msg='112102312'



def count_decoded(msg):
    count = [0] * len(msg)
    count[0] = 1
    count[1] = 1

    for i in range(2,len(count)):
        if msg[i-1] > '0':
            count[i] = count[i-1]
        if (msg[i-2] == '1' or (msg[i-2] == '2' and msg[i-1] < '7') ):
            count[i] += count[i-2]

    return count[-1]