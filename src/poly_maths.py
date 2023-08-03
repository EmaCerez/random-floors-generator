#!/usr/bin/env python
"""
The methods used to effectuate calculations like
    "Is this Point inside this triangle?"

Usage: src.poly.py
"""

from src.point import Point
import polytri.polytri as polytri


def area(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float):
    """
    Calculates the area of a triangle.
    :param x1: Point 1 x coordinate.
    :param y1: Point 1 Y coordinate.
    :param x2: Point 2 x coordinate.
    :param y2: Point 2 Y coordinate.
    :param x3: Point 3 x coordinate.
    :param y3: Point 3 Y coordinate.
    :return: The area
    """
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)


def is_in_triangle(t: list[list[float]], p: list[float]) -> bool:
    """
    Checks if point p is inside triangle t.
    :param t: The triangle.
    :param p: The point.
    :return: True if p is in t, else False.
    """
    p1, p2, p3 = t[0], t[1], t[2]
    A = area(p1[0], p1[1], p2[0], p2[1], p3[0], p3[1])
    A1 = area(p[0], p[1], p2[0], p2[1], p3[0], p3[1])
    A2 = area(p1[0], p1[1], p[0], p[1], p3[0], p3[1])
    A3 = area(p1[0], p1[1], p2[0], p2[1], p[0], p[1])
    if A == A1 + A2 + A3:
        return True
    else:
        return False


def is_in_polygon(poly: list[Point], p: Point) -> bool:
    """
    Checks if the point p is inside the polygon poly by triangulating the polygon
    poly and checking weither or not the point p is inside one of the triangles.
    :param poly: The polygon.
    :param p: The point.
    :return: True if p is in poly, else False.
    """
    triangles = polytri.earclip([(p.x, p.y) for p in poly])
    for triangle in triangles:
        if is_in_triangle(triangle, [p.x, p.y]):
            return True
    return False
