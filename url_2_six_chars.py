# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 10:48:23 2018
 Implement a URL shortener with the following methods:

    shorten(url), which shortens the url into a six-character alphanumeric
    string, such as zLg6wl.
    restore(short), which expands the shortened string into the original url.
    If no such shortened string exists, return null.

Hint: What if we enter the same URL twice?
@author: carlgval
"""


class Url_Shortener(object):
    chars = 6
    char_map = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    id_map = {}

    def to_short(self, n):
        out = ''
        for i in reversed(range(self.chars)):
            out += self.char_map[n // (len(self.char_map) ** i)]
            n = n % (len(self.char_map) ** i)
        return out

    def to_id(self, n):
        out = 0
        for i, char in enumerate(n):
            out += self.char_map.index(char) * 62 ** (self.chars - i - 1)
        return out

    def shorten(self, url):
        if url not in self.id_map.keys():
            self.id_map[url] = len(self.id_map) + 1
        return self.to_short(self.id_map[url])

    def restore(self, url_s):
        id_s = self.to_id(url_s)
        return self.id_map.keys()[self.id_map.values().index(id_s)]


if __name__ == '__main__':
    u_s = Url_Shortener()
    print(u_s.to_short(321))
    print(u_s.to_id(u_s.to_short(321)))

    print(u_s.shorten('asdfsdfadsfasdf'))
    print(u_s.shorten('asdfsdfadsfasdf2'))
    print(u_s.shorten('asdfsdfadsfasdf'))
    print(u_s.restore(u_s.shorten('asdfsdfadsfasdf2')))
    print(u_s.restore(u_s.shorten('asdfsdfadsfasdf')))
