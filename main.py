#!/usr/bin/env python

"""
The main file that runs the whole project.

__author__ = "EmaCerez"
__credits__ = ["EmaCerez", "ajaycc17"]
__version__ = "1.0.0"
__maintainer__ = "EmaCerez"
__email__ = "e.cerezo@proton.me"
"""

import matplotlib.pyplot as plt
import argparse

import polytri.polytri as polytri
import src.poly_sort as pr
import src.poly as poly
from src.point import Point


if __name__ == '__main__':
    # -------------------- Parser ------------------------------------

    DEFAULT_PATH = ''
    DEFAULT_FILENAME = "fig.png"
    DEFAULT_RANDOMIZE = False
    DEFAULT_CORNERS = 8
    DEFAULT_INSIDE_WALLS = 50
    DEFAULT_RD_INSIDE_WALLS = 14
    DEFAULT_POLY = [Point(0, 0), Point(0, 25), Point(0, 50), Point(0, 75),
                    Point(25, 75), Point(50, 75), Point(75, 75), Point(100, 75),
                    Point(100, 50), Point(100, 25), Point(100, 0), Point(75, 0),
                    Point(50, 0), Point(25, 0)]
    DEFAULT_SEPARATOR = 10
    DEFAULT_WALL_LENGTH = 1
    DEFAULT_COLOR = "black"
    DEFAULT_SHOW_DOTS = False

    parser = argparse.ArgumentParser(description='Generating random floors as plots.')

    parser.add_argument('-p', '--path', required=False, default=DEFAULT_PATH, type=str,
                        help="Path to save output.")
    parser.add_argument('-f', '--filename', required=False, default=DEFAULT_FILENAME, type=str,
                        help="Name of output file.")
    parser.add_argument('-rand', '--randomize', required=False, default=DEFAULT_RANDOMIZE, type=bool,
                        help="Weither or not the outside corners of the floors should be randomized.")
    parser.add_argument('-cn', '--corners', required=False, default=DEFAULT_CORNERS, type=int,
                        help="How many outside corners in the randomized output.")
    parser.add_argument('-miw', '--manual-inside-walls', required=False, default=DEFAULT_INSIDE_WALLS, type=int,
                        help="How many points to create inside walls (manual).")
    parser.add_argument('-iw', '--inside-walls', required=False, default=DEFAULT_RD_INSIDE_WALLS, type=int,
                        help="How many points to create inside walls (randomized).")
    parser.add_argument('-poly', '--polygon', required=False, default=DEFAULT_POLY, type=list[Point],
                        help="Specify a polygon structure: [Point(0,0), Point(25,0), ...].\nPoints coordinates must be between 0 and 100.")
    parser.add_argument('-sep', '--separator', required=False, default=DEFAULT_SEPARATOR, type=float,
                        help="Minimum distance between two inside points. Must not be too big, especially if inside-walls parameter is big.")
    parser.add_argument('-wl', '--wall-length', required=False, default=DEFAULT_WALL_LENGTH, type=int,
                        help="The xth closest point will be used to build walls.")
    parser.add_argument('-col', '--color', required=False, default="black", type=str,
                        help="The color of the output.")
    parser.add_argument('-sd', '--show-dots', required=False, default=DEFAULT_SHOW_DOTS, type=bool,
                        help="Show points used to create the output.")

    args = parser.parse_args()

    path = args.path
    filename = args.filename
    randomize = args.randomize
    nb_corners = args.corners
    man_inside_walls = args.manual_inside_walls
    inside_walls = args.inside_walls
    polygon = args.polygon
    separator = args.separator
    wall = args.wall_length
    color = args.color
    arg_show_dots = args.show_dots

    # -------------------------- Parameters ----------------------------------

    # Outside walls building parameters
    random_outside = randomize
    # If the outside walls are not randomised, this poly will be used:
    newpoly = polygon
    # Else, this number of corners will be used to build the outside walls:
    corners = nb_corners

    # Inside walls building parameters
    nb_inside_walls = man_inside_walls    # Number of dots used to build inside walls
    if random_outside:
        nb_inside_walls = inside_walls
    separate = separator       # Min dist between inside_walls dots
    wall_length = wall    # Xth closest dot will be used to build walls

    # Display parameters
    house_color = color
    wall_color = color
    show_dots = arg_show_dots

    # ------------------------------ Process ---------------------------------

    if random_outside:
        newpoly = poly.generate_random_poly(corners)

    sorted_poly = pr.sort_polygon(newpoly)
    sorted_poly = pr.sort_polygon(sorted_poly)
    sorted_poly = pr.sort_polygon(sorted_poly)

    newpolytri = polytri.polyToPolytri(sorted_poly)
    triangles = polytri.earclip(newpolytri)

    new_dots = poly.generate_x_dots(sorted_poly, inside_walls, separate)
    all_dots = [x for x in sorted_poly]

    additional_walls = []
    for dot in new_dots:
        all_dots.append(dot)
        exceptions = []
        closest = pr.find_closest_point(all_dots, -1, exceptions)[0]
        while len(exceptions) < wall_length - 1:
            exceptions.append(closest)
            closest = pr.find_closest_point(all_dots, -1, exceptions)[0]
        additional_walls.append([dot, all_dots[closest]])

    # ------------------------------- Display --------------------------------

    fig = plt.figure()

    X = [x.x for x in sorted_poly]
    X.append(sorted_poly[0].x)
    Y = [x.y for x in sorted_poly]
    Y.append(sorted_poly[0].y)

    add_walls_X = [[x[0].x, x[1].x] for x in additional_walls]
    add_walls_Y = [[x[0].y, x[1].y] for x in additional_walls]

    plt.plot(X, Y, color=house_color)

    for i in range(len(add_walls_X)):
        plt.plot(add_walls_X[i], add_walls_Y[i], "-", color=wall_color)

    if show_dots:
        plt.plot(X, Y, "p", color="red")
        plt.plot([x.x for x in new_dots], [x.y for x in new_dots],
                 "p", color="green")

    plt.axis('equal')
    plt.grid(False)
    plt.axis('off')
    plt.savefig(f'{path}{filename}')
    # plt.show()
