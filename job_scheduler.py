# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 08:12:28 2018

 Implement a job scheduler which takes in a function f and an integer n,
 and calls f after n milliseconds.

@author: carlosgonzalez
"""
from __future__ import print_function
import threading
import time


class Scheduler(threading.Thread):
    def __init__(self, f, miliseconds):

        def run():
            time.sleep(float(miliseconds)/1000)
            f()

        self.run = run
        super(Scheduler, self).__init__()
        self.start()


s1 = Scheduler(lambda: print('second'), 1000)

s2 = Scheduler(lambda: print('third'), 2000)

s3 = Scheduler(lambda: print('first'), 500)
