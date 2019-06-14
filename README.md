# search-algorithms
Research about different search algorithms: B&B, B&B with heuristics, DFS and BFS.
It compares between two different algorithms, branch and hop, and branch and hop with underestimation.

The following classes have been added to the utils.py file:

"babg" Based on the structure of the FIFOQueue class modifying the extended method by adding the sort order of the list to the path_cost.

"babgsub" Based on the structure of the FIFOQueue class modifying the extended method by adding the sort order of the list by the sum of the path_cost together with the given heuristic in the problem class.

The graph_search class has been added to the search.py file:
branch_and_bound and branch_and_bound_sud that return the corresponding tree search.
