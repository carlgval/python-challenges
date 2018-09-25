# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 12:03:46 2018
 The area of a circle is defined as πr^2. Estimate π to 3 decimal places
 using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
@author: carlosgonzalez
"""

import numpy as np

samples = 10**8

r = 1

points = np.random.random((2, samples)) * 2 - 1
area_square = (2 * r) * (2 * r) # area_circle = pi * r * r

# pi = area_circle * 4 / area_square

circle_points = np.sum(np.sqrt(np.sum(np.square(points), axis=0)) < r)

pi = float(circle_points) * 4 / samples
