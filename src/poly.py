#!/usr/bin/env python
"""
The main methods used to build a floor.
Usage: main.py
"""

import random
from src.point import Point
import src.poly_maths as pm
import src.poly_sort as pr


def generate_random_poly(corners: int) -> list[Point]:
    """
    Generates a polygon with a specified number of corners.
    :param corners: the number of corners
    :return: the polygon as a list of Points
    """
    poly = []
    for i in range(corners):
        a, b = random.randint(0, 100), random.randint(0, 100)
        new_point = Point(a, b)
        poly.append(new_point)
    return poly


def create_dot_inside(poly: list[Point]) -> Point:
    """
    Generates a Point inside the specified polygon.
    :param poly: The polygon inside which to generate a Point.
    :return: said Point
    """
    p = Point(random.randint(0, 100), random.randint(0, 100))
    while not pm.is_in_polygon(poly, p):
        p = Point(random.randint(0, 100), random.randint(0, 100))
    return p


def generate_x_dots(poly: list[Point], howmany: int, distmin: float) -> list[Point]:
    """
    Generates a specified number of points inside a specified polygon.
    :param poly: The polygon inside which to generate a set of points.
    :param howmany: How many points to generate.
    :param distmin: The minimum distance between two points.
    :return: A list with the generated Points.
    """
    result = [create_dot_inside(poly)]
    for i in range(howmany - 1):
        dot = create_dot_inside(poly)
        result.append(dot)
        while pr.find_closest_point(result, len(result) - 1, [])[1] < distmin:
            result.pop(-1)
            dot = create_dot_inside(poly)
            result.append(dot)
    return result
