# Import Libraries

import numpy as np
import sys


# Define Tester Function for Printing Results

def testPrint(distance, path_list):
    for v in range(vertices):
        print("\nDistance from %d is: %d - Path: " % (v, distance[v]), path_list[v])


# Define Distance Helper Function for Finding Closest Vertex

def minDistanceCalc(vertices, distance, shortest_path_list):
    min_distance = sys.maxsize

    minimum_index = 0

    for v in range(vertices):
        if distance[v] < min_distance and shortest_path_list[v] == False:
            min_distance = distance[v]
            minimum_index = v

    return minimum_index


# Define Path Building Helper Function

def buildPath(src, parent, vertices):
    # Initialize List of Lists Containing Paths
    path_list = [[] for _ in range(vertices)]

    # For Every Target Vertex

    for v in range(vertices):
        # v Isn't Source
        if v != src:
            # u as First Parent
            u = parent[v]

            # While Parent Is Not the Source Vertex
            while u != src:
                # Add u in the Beginning of the List
                path_list[v].insert(0, u)

                # Update u
                u = parent[u]

    return path_list


# Define Dijkstra Function

def dijkstra(mat, vertices, src):
    # Array - List Definitions

    shortest_path_list = [False] * vertices  # List of Size mat With Default False Values
    distance = [sys.maxsize] * vertices      # List of Size mat With Default INT_MAX Values
    distance[src] = 0                        # Set src Distance to Zero
    parent = [*range(vertices)]              # List of Paths from Source to All Vertices

    for cnt in range(vertices):
        # Find Closest Vertex Not Processed
        u = minDistanceCalc(vertices, distance, shortest_path_list)

        # Vertex Processed
        shortest_path_list[u] = True

        # Update Distances

        for v in range(vertices):
            if mat[u, v] > 0 and shortest_path_list[v] == False and distance[v] > (distance[u] + mat[u, v]):
                distance[v] = distance[u] + mat[u, v]
                parent[v] = u

    path_list = buildPath(src, parent, vertices)

    return distance, path_list


# Define Extended Dijkstra Function

def dijkstraExtended(mat, vertices, src, tgt, k):
    # Array - List Initialization

    path_list = []          # List of Shortest Paths
    cnt = [0] * vertices    # Counter of Shortest Paths Found for Every Vertex
    temp_path_list = [[0]]  # List of Temporary Paths
    cost = [] * vertices    # List of Costs According to Paths in temp_path_list

    while temp_path_list and cnt[tgt] < k:
        # Get Path Based on Index of Path with Least Cost
        path = temp_path_list[cost.index(min(cost))]

        # Remove path from temp_path_list
        temp_path_list.remove(path)

        # Increment Counter Variable of path Target
        cnt[path[-1]] += 1


# Define Network Topology as Array - Matrix
network = np.array([[0, 0, 5, 0, 0],
                    [0, 0, 0, 3, 7],
                    [5, 0, 0, 1, 0],
                    [0, 3, 1, 0, 1],
                    [0, 7, 0, 1, 0]])

network2 = np.array([[0, 4, 0, 0, 0, 0, 0, 8, 0],
                     [4, 0, 8, 0, 0, 0, 0, 11, 0],
                     [0, 8, 0, 7, 0, 4, 0, 0, 2],
                     [0, 0, 7, 0, 9, 14, 0, 0, 0],
                     [0, 0, 0, 9, 0, 10, 0, 0, 0],
                     [0, 0, 4, 14, 10, 0, 2, 0, 0],
                     [0, 0, 0, 0, 0, 2, 0, 1, 6],
                     [8, 11, 0, 0, 0, 0, 1, 0, 7],
                     [0, 0, 2, 0, 0, 0, 6, 7, 0]
                     ])

# Number of Vertices
vertices = len(network)

# Testing Section

# User Choice Over Source Vertex
choice = int(input('\nGive Source Vertex for Dijkstra: '))

test_distance, test_path_list = dijkstra(network, vertices, choice)
testPrint(test_distance, test_path_list)

# User Choice Over K Number of Paths
choice = int(input('\nGive Number of Shortest Paths to Calculate: '))

# TODO: Extended Dijkstra Running Here
