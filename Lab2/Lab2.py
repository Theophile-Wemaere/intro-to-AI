#!/bin/python
import argparse

graph = {
    'Start': ["A", "B", "D"],
    'A': ["Start", "C"],
    'B': ["Start", "D"],
    'C': ["A", "D", "Goal"],
    'D': ["Start", "B", "C", "Goal"],
    'Goal': ["C", "D"]
}

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

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description='run BFS and DFS algorithm')
        parser.add_argument('--dfs', action='store_true', help='Perform depth-first search (DFS).')
        parser.add_argument('--bfs', action='store_true', help='Perform breath-first search (BFS).')
        args = parser.parse_args()

        if args.bfs:
            print("\nRunning BFS algorithm : ")
            bfs(graph, "Start","Goal")
        if args.dfs:
            print("\nRunning DFS algorithm : ")
            dfs(graph, "Start","Goal")
        if not args.dfs and not args.bfs:
            parser.print_help()

    except KeyboardInterrupt:
        print("\nCtrl+C pressed, exiting...")
        exit(1)