#!/bin/python

def bfs(graph, start,goal):
    visited = []
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        current_node = path[-1]
        print(f"Visiting {current_node} from {' -> '.join(path)}")

        visited.append(current_node)

        if current_node == goal:
            print("\nOptimal path found : ",end ='') 
            print(' -> '.join(path))
            return 0
    
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

graph = {
    'Start': ["A", "B","D"],
    'A': ["Start", "C"],
    'B': ["Start", "D"],
    'C': ["A", "D", "Goal"],
    'D': ["Start", "B", "C", "Goal"],
    'Goal': ["C", "D"]
}

bfs(graph, "Start", "Goal")
