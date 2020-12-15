# Import Libraries

import numpy as np
import sys


# Define Distance Helper Function for Finding Closest Vertex

def minDistanceCalc(mat, distance, shortest_path_list):
    min_distance = sys.maxint

    minimum_index = 0

    for v in range(mat):
        if distance[v] < min_distance and shortest_path_list[v] == False:
            min_distance = distance[v]
            minimum_index = v

    return minimum_index


# Define Dijkstra Function

def dijkstra(mat, src):
    # Array - List Definitions

    shortest_path_list = [False] * mat  # List of Size mat With Default False Values
    distance = [sys.maxint] * mat  # List of Size mat With Default INT_MAX Values
    distance[src] = 0  # Set src Distance to Zero

    for cnt in range(mat):
        # TODO Add MinDistance Helper Function
        print()


# Define Network Topology as Array - Matrix
network = np.array([[0, 0, 5, 0, 0],
                    [0, 0, 0, 3, 7],
                    [5, 0, 0, 1, 0],
                    [0, 3, 1, 0, 1],
                    [0, 7, 0, 1, 0]])

# User Choice Over K Number of Paths
choice = input('\nGive Number of Shortest Paths to Calculate: ')

# TODO: Extended Dijkstra Running Here
