#!/usr/bin/env python
"""
Just a few methods used to plot more easily.
Usage: None anymore
"""

from typing import Tuple


def tri_coords_to_plt(triangle: list[list[float]]) -> Tuple[list[float], list[float]]:
    """
    Converts triangle coordinates into plotable coordinates.
    :param triangle: The triangle.
    :return: X coordinates as a list and Y coordinates as a list.
    """
    X = [x[0] for x in triangle]
    Y = [x[1] for x in triangle]
    return X, Y


def poly_coords_to_plt(poly: list[list[list[float]]]) -> Tuple[list[float], list[float]]:
    """
    Converts polygon (divided into triangles) coordinates into plotable coordinates.
    :param poly: The polygon.
    :return: X coordinates as a list and Y coordinates as a list.
    """
    X, Y = [], []
    for triangle in poly:
        xcoords, ycoords = tri_coords_to_plt(triangle)
        for i in range(len(xcoords)):
            X.append(xcoords[i])
            Y.append(ycoords[i])
    return X, Y
