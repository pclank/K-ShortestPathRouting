# Import Libraries

import numpy as np
import sys


# **********************************************************
# Function Definition Section
# **********************************************************

# Define Tester Function for Printing Results from Dijkstra

def testPrint(distance, path_list):
    for v in range(vertices):
        print("\nDistance from %d is: %d - Path: " % (v, distance[v]), path_list[v])


# Define Tester Function for Printing Results from Extended Dijkstra

def testPrintExtended(path_list, cost_list):
    cnt = 0

    for path in path_list:
        print("\nPath %d: " % cnt, path, " with Cost: %d" % cost_list[cnt])
        cnt += 1


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
    distance = [sys.maxsize] * vertices  # List of Size mat With Default INT_MAX Values
    distance[src] = 0  # Set src Distance to Zero
    parent = [*range(vertices)]  # List of Paths from Source to All Vertices

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

    path_list = []  # List of Shortest Paths
    final_cost = []  # List of Final Costs of Shortest Paths
    cnt = [0] * vertices  # Counter of Shortest Paths Found for Every Vertex
    temp_path_list = []  # List of Temporary Paths
    cost = [0]  # List of Costs According to Paths in temp_path_list

    temp_path_list.append([src])

    while temp_path_list and cnt[tgt] < k:
        # Get Path Based on Index of Path with Least Cost

        path_index = cost.index(min(cost))  # TODO: Check Proper Usage of min()
        path = temp_path_list[path_index]

        # Save cost Before Removing
        temp_cost = cost[path_index]

        # Remove path from temp_path_list
        temp_path_list.remove(path)

        # Remove temp_cost from cost
        cost.pop(path_index)

        # Increment Counter Variable of path Target Vertex
        cnt[path[-1]] += 1

        # If path Target is tgt Add path to path_list, and Add cost to final_cost

        if path[-1] == tgt:
            path_list.append(path)
            final_cost.append(temp_cost)

        # Check Adjacent Vertices

        if cnt[path[-1]] <= k:
            for v in range(vertices):
                if mat[path[-1], v] > 0 and v not in path:
                    # Add Edge (u, v) to path as new_path

                    new_path = []
                    new_path.extend(path)
                    new_path.append(v)

                    # Add new_path to temp_path_list
                    temp_path_list.append(new_path)

                    # Set cost to Added cost from New Edge
                    cost.append(temp_cost + mat[path[-1], v])

    return path_list, final_cost


# *****************************************
# Driver Code
# *****************************************

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

# User Choice over Which Function to Run
fun_choice = int(input('\n0: Dijkstra\n1: Extended Dijkstra\nSelect Function to Run: '))

if fun_choice == 0:
    # User Choice Over Source Vertex
    src = int(input('\nGive Source Vertex for Dijkstra: '))

    test_distance, test_path_list = dijkstra(network, vertices, src)
    testPrint(test_distance, test_path_list)

elif fun_choice == 1:
    # User Choice Over Source Vertex
    src = int(input('\nGive Source Vertex for Extended Dijkstra: '))

    # User Choice Over Target Vertex
    tgt = int(input('Give Target Vertex for Extended Dijkstra: '))

    # User Choice Over K Number of Paths
    k = int(input('Give Number of Shortest Paths to Calculate: '))

    # Run Extended Dijkstra Algorithm Function
    path_list, path_cost = dijkstraExtended(network, vertices, src, tgt, k)

    # Print Results
    testPrintExtended(path_list, path_cost)
