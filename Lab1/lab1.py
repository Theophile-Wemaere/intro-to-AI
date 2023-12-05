#!/bin/python
def h(x):
    H = {
    "A":2,
    "B":5,
    "C":2,
    "D":1
    }
    return H[x] if x not in ("Start","Goal") else 0

def build_path(current,previous,start):
    path = []
    while previous[current] != current:
        path.append(current)
        current = previous[current]
    path.append(start)
    path.reverse()
    return path

def a_star(start, stop, graph):
        # FRINGE are nodes spawned but not inspected and CLOSED are nodes inspected
        # we use set instead of list for easier access
        FRINGE = set([start])
        CLOSED = set([])

        # distances from start to each node    
        g = {}
        g[start] = 0

        # previous contains all nodes before each nodes (like a path)
        previous = {}
        previous[start] = start

        while len(FRINGE) > 0:
            # current is the node we are examining in this iteration
            current = None

            # find lowest value of f() for each node
            for candidat in FRINGE:
                if current == None or g[candidat] + h(candidat) < g[current] + h(current):
                    current = candidat;

            # is it the goal node ?
            if current == stop:
                path = build_path(current,previous,start)
                print("\nOptimal path found : ",end ='')
                print(' -> '.join(path)+'\n')
                return 0

            # get all neighbors of the current node 
            for node_name,weight in graph[current]: # return list of ["node_name",weight]
                # if this is a new node ?
                if node_name not in FRINGE and node_name not in CLOSED:
                    FRINGE.add(node_name)
                    previous[node_name] = current
                    g[node_name] = g[current] + weight
                    print("Examining : ",end='')
                    print(" -> ".join(build_path(node_name,previous,start)))


                else:
                    # check if it is worth it to visit the current neighbor (node_name)
                    if g[node_name] > g[current] + weight:
                        g[node_name] = g[current] + weight
                        previous[node_name] = current

                        if node_name in CLOSED:
                            CLOSED.remove(node_name)
                            FRINGE.add(node_name)
                    
            # all neighbors have been inspected, remove it
            FRINGE.remove(current)
            CLOSED.add(current)

        print('Error, no path found')
        return -1

if __name__ == "__main__":
    try:
        graph = {
            "Start":[("A",2),("B",3)],
            "A":[("Start",2),("C",4)],
            "B":[("Start",3),("D",4)],
            "C":[("A",4),("D",1),("Goal",2)],
            "D":[("Start",5),("B",4),("C",1),("Goal",5)],
            "Goal":[("C",2),("D",5)]
        }
        a_star('Start', 'Goal',graph)
    except KeyboardInterrupt:
        print("\nExiting...")
        exit(1)