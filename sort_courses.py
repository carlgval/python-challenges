#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Created on Fri Dec  7 12:39:36 2018

 We're given a hashmap with a key courseId and value a list of courseIds,
 which represents that the prerequsite of courseId is courseIds. Return a
 sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], '
CSC100': []}, should return ['CSC100', 'CSC200', 'CSCS300'].

@author: carlgval
"""


class Course(object):
    def __repr__(self, tab=0):
        out = '{} id={} \n'.format(self.__class__.__name__, self.id)
        for each in self.prerequisites:
            out += (tab + 1) * '  ' + \
                '{}'.format(each.__repr__(tab + 1))
        return out

    def __init__(self, name):
        self.id = name
        self.prerequisites = []

    def list_prerequisites(self):
        out = []
        self._list_prerequisites(out)
        return out

    def _list_prerequisites(self, stack):
        debug_id = self.id
        for each in self.prerequisites:
            each._list_prerequisites(stack)

        if self.id not in stack:
            idx = max([stack.index(each.id) for each in self.prerequisites] + [-1])
            stack.insert(idx + 1, self.id)


def check_prerequisites(hashmap):
    added_courses = {}

    def add_course(course_id):
        if course_id not in added_courses.keys():
            course = Course(course_id)
            for each in hashmap[course_id]:
                course.prerequisites.append(add_course(each))
            added_courses[course_id] = course
            return course
        else:
            return added_courses[course_id]

    for each_id, _ in hashmap.items():
        add_course(each_id)
    return added_courses


if __name__ == '__main__':
    courses = check_prerequisites({'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []})
    print(courses['CSC300'].list_prerequisites())
