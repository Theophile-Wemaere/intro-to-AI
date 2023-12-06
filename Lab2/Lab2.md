<html>
	<center>Introduction to AI, M. MATEI</center>
	<center>ISEP - December 2023</center>
	<center style="font-style:italic">by Theophile Wemaere</center>
</html>

## Depth-first search and Breath-first search

Source code and markdown source file can be found [here](https://github.com/Theophile-Wemaere/intro-to-AI/tree/main/Lab2)
or at [github.com/Theophile-Wemaere/intro-to-ai](https://github.com/Theophile-Wemaere/intro-to-ai) 

### Part A

**Question 1**

The time complexity of DFS and BFS algorithms is **O(V + E)**, where V is the number of vertices (the nodes) and E (links between nodes) is the number of edges in the graph. This means that the time it takes for these algorithms to run is proportional to the size of the graph.

A* uses a heuristic function to guide its search. The heuristic function is an estimate of the distance between the current node and the goal node. This allows A* to focus on the most promising paths, which can make it more efficient than DFS and BFS.

The time complexity of A* is **O(V + E log V)** in the worst case, but it is often much better than this in practice. This is because A* is able to prune many of the nodes that would be explored by DFS and BFS.

**Question 2**

The memory requirements of DFS and BFS algorithms are **O(V)**, where V is the number of vertices in the graph. This is because these algorithms store the entire frontier of the search in memory.

The memory requirements of A* are also **O(V)**, but they can be higher in practice if the heuristic function is not very accurate. This is because A* may explore more nodes than DFS and BFS.

**Question 3: Comparison and Applications**

Here is a table summarizing the key differences between DFS, BFS, UCS, and A*:

|Algorithm|Time Complexity|Memory Requirements|Description|Applications|
|---|---|---|---|---|
|DFS|O(V + E)|O(V)|Explores all paths in a depth-first manner|Finding connected components, detecting cycles|
|BFS|O(V + E)|O(V)|Explores all paths in a breadth-first manner|Finding shortest paths, checking if a graph is bipartite|
|UCS|O(V + E log V)|O(V)|Uninformed search algorithm that prioritizes nodes with the lowest cost|Finding shortest paths in graphs with non-negative edge costs|
|A*|O(V + E log V)|O(V)|Informed search algorithm that prioritizes nodes with the lowest estimated cost to the goal|Finding shortest paths in graphs with non-negative edge costs, planning navigation in robotics|

In general, DFS is a good choice for finding connected components and detecting cycles. BFS is a good choice for finding shortest paths and checking if a graph is bipartite. UCS is a good choice for finding shortest paths in graphs with non-negative edge costs. A* is a good choice for finding shortest paths in graphs with non-negative edge costs, planning navigation in robotics, and other applications where a heuristic function is available.

Here are some additional points to consider:

- DFS is more likely to get stuck in deep, narrow parts of the graph.
- BFS is more likely to explore a larger number of nodes.
- UCS is guaranteed to find the shortest path if one exists, but it may not be the most efficient algorithm.
- A* is not guaranteed to find the shortest path, but it is often much more efficient than UCS.
### Part B



### Part C
