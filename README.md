# K-ShortestPathRouting
Python Implementation of Various Algorithms Conserning Optical Network Pathfinding, and Lightpath Use Reduction. The Implementation is Ready to Run, and is Based on Networks Discribed as Matrices, Where an Element A(i, j) > 0 Denotes that an Edge (Link) Exists Between i and j with cost A(i, j). If A(i, j) = 0, then There is No Edge Between i and j.
## Types of Algorithms Included
The Following Implementations are Included for Pathfinding:
* Extended Dijkstra Algorithm, Solving the K - Shortest Path Problem, where K is a Parameter and Cost for Each Path is Also Printed.
* Edge Use Reduction Algorithm, Removing Unnecessary Edges in Each Set of Paths, Printing All Reductions per Set.
* Various Algoriths Solving the Limited Lightpath Assignment Problem, where the Number of Lightpaths per Vertex (Node) is a Parameter. Algorithms included are:
  - Random Lightpath Assignment
  - First - Fit Lightpath Assignment
  - Least Used Lightpath Assignment
