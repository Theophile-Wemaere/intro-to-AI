#!/bin/python

def dfs(graph,start,goal):
    visited = []
    queue = [[start]]

    while queue:
        path = queue.pop()
        current_node = path[-1]
        visited.append(current_node)
        print(f"Visiting {current_node} from {' -> '.join(path)}")

        if current_node == goal:
            print("\nOptimal path found : ",end ='') 
            print(' -> '.join(path))
            return 0

        for neighbor in list(graph[current_node])[::-1]:
            if neighbor not in visited:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

graph = {
    'Start': ["A", "B", "D"],
    'A': ["Start", "C"],
    'B': ["Start", "D"],
    'C': ["A", "D", "Goal"],
    'D': ["Start", "B", "C", "Goal"],
    'Goal': ["C", "D"]
}

dfs(graph, "Start","Goal")