# Import Libraries

import numpy as np
import sys


# Define Tester Function for Printing Results

def testPrint(distance):
    for v in range(vertices):
        print("\nDistance from %d is: %d" %(v, distance[v]))


# Define Distance Helper Function for Finding Closest Vertex

def minDistanceCalc(vertices, distance, shortest_path_list):
    min_distance = sys.maxint

    minimum_index = 0

    for v in range(vertices):
        if distance[v] < min_distance and shortest_path_list[v] == False:
            min_distance = distance[v]
            minimum_index = v

    return minimum_index


# Define Dijkstra Function

def dijkstra(mat, vertices, src):
    # Array - List Definitions

    shortest_path_list = [False] * vertices     # List of Size mat With Default False Values
    distance = [sys.maxint] * vertices          # List of Size mat With Default INT_MAX Values
    distance[src] = 0                           # Set src Distance to Zero

    for cnt in range(vertices):
        # Find Closest Vertex Not Processed
        u = minDistanceCalc(vertices, distance, shortest_path_list)

        # Vertex Processed
        shortest_path_list[u] = True

        # Update Distances

        for v in range(mat):
            if mat[u, v] > 0 and shortest_path_list[v] == False and distance[v] > (distance[u] + mat[u, v]):
                distance[v] = distance[u] + mat[u, v]

        return distance


# Define Network Topology as Array - Matrix
network = np.array([[0, 0, 5, 0, 0],
                    [0, 0, 0, 3, 7],
                    [5, 0, 0, 1, 0],
                    [0, 3, 1, 0, 1],
                    [0, 7, 0, 1, 0]])

# Number of Vertices
vertices = np.size(network) / 2

# User Choice Over K Number of Paths
choice = input('\nGive Number of Shortest Paths to Calculate: ')

# TODO: Extended Dijkstra Running Here
