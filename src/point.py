#!/usr/bin/env python
"""
Class for a single 2D Point
Usage: polytri.polytri.py, src.poly.py, src.poly_math.py, src.poly_sort.py, main.py
"""

import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_from_point(self, p) -> float:
        """
        Gets the distance between this point and point p.
        :param p: the other point
        :return: the distance
        """
        return np.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)
