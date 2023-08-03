#!/usr/bin/env python
"""
Because points from the polygon are generated at random, they need to
get sorted for the polygon to look good.

Usage: main.py
"""

from src.point import Point


def find_closest_point(points: list[Point], ref_point_index: int, exceptions_list: list[int]):
    """
    Finds the closest point to a point of reference, as long as it is not in the exceptions_list.
    :param points: The set of points in which we're searching, ref_point_index included.
    :param ref_point_index: The index of the point that interests us.
    :param exceptions_list: The index of the points from the set that we do not want to get as a result.
    :return: the index of the closest point and the min dist between this point and the reference.
    """
    ref_point = points[ref_point_index]
    other_points_index_list = list(range(len(points)))
    other_points_index_list.pop(ref_point_index)
    other_points_index_list = [index for index in other_points_index_list if index not in exceptions_list]
    closest_point_index = other_points_index_list[0]

    dist_min = ref_point.dist_from_point(points[other_points_index_list[0]])

    for point_index in other_points_index_list:
        dist = ref_point.dist_from_point(points[point_index])
        if dist < dist_min:
            dist_min = dist
            closest_point_index = point_index

    return closest_point_index, dist_min


def get_order(points: list[Point], first_point_index: int):
    """
    Gets the order in which the points should have been placed to form a nice
    polygon when they're connected one to one.
    :param points: The set of points.
    :param first_point_index: The index of the point to start the list from.
    :return: A list containing the index of the points points, but sorted.
    """
    remaining_index_list = list(range(len(points)))
    result_road_index_list = [first_point_index]
    remaining_index_list.remove(first_point_index)
    dist_list = []

    while len(remaining_index_list) > 0:
        closest_point_index, dist = find_closest_point(points, result_road_index_list[-1], result_road_index_list)
        dist_list.append(dist)
        result_road_index_list.append(closest_point_index)
        remaining_index_list.remove(closest_point_index)

    dist_first_last = points[result_road_index_list[0]].dist_from_point(points[result_road_index_list[
                                       len(result_road_index_list) - 1]])

    dist_list.append(dist_first_last)

    return result_road_index_list, dist_list


def get_order_again(result_road_index_list, dist_list) -> int:
    """
    Checks if it is necessary to sort the polygon again starting from another point.
    :param result_road_index_list: The list of sorted point id found by get_order
    :param dist_list: The list of distances found by get_order
    :return: The point to start again from
    """
    max_dist = 0
    point_index_to_start_again_from = result_road_index_list[0]
    for i in range(len(dist_list)):
        if dist_list[i] > max_dist:
            point_index_to_start_again_from = result_road_index_list[i]
            max_dist = dist_list[i]
    if point_index_to_start_again_from != result_road_index_list[0]:
        return point_index_to_start_again_from
    else:
        return 0


def sort_polygon(points: list[Point]) -> list[Point]:
    """
    Sorts the polygon.
    :param points: The points forming the polygon.
    :return: The points forming the polygon, but sorted.
    """
    order_list, dist_list = get_order(points, 0)
    redo = get_order_again(order_list, dist_list)
    point_index_tried = []
    while redo > 0 and redo not in point_index_tried:
        point_index_tried.append(redo)
        order_list, dist_list = get_order(points, redo)
        redo = get_order_again(order_list, dist_list)
    new_list = []
    for i in order_list:
        new_list.append(points[i])
    return new_list
