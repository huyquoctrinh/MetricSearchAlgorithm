from algo.graphAsset import *
import queue

def heuristic2(p1, p2, rewards):
    nearest_reward = 10**9
    for u, v, w in rewards:
        dist = abs(p1[0]-u) + abs(p1[1]-v) 
        if dist < nearest_reward:
            nearest_reward = dist
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) + nearest_reward

def a_star_algorithm(graph, start_node, end, rewards=[]):
    # open_list is a list of nodes which have been visited, but who's neighbors
    # haven't all been inspected, starts off with the start node
    # closed_list is a list of nodes which have been visited
    # and who's neighbors have been inspected
    open_list = set([start_node])
    closed_list = set([])
    # g contains current distances from start_node to all other nodes
    # the default value (if it's not found in the map) is +infinity
    g = [[10**9] * len(graph[i]) for i in range(len(graph))]
    cost = [[1] * len(graph[i]) for i in range(len(graph))]
    for u, v, w in rewards:
        cost[u][v] = w
    g[start_node[0]][start_node[1]] = 0

    # parents contains an adjacency map of all nodes
    track = [[(-1, -1)] * len(graph[i]) for i in range(len(graph))]

    while len(open_list) > 0:
        n = None

        # find a node with the lowest value of f() - evaluation function
        for v in open_list:
            if n == None or g[v[0]][v[1]] + heuristic2(v, end, rewards) < g[n[0]][n[1]] + heuristic2(n, end, rewards):
                n = v

        if n == None:
            print('Path does not exist!')
            return []

        # if the current node is the end
        # then we begin reconstructin the path from it to the start_node
        if n == end:
            return findPath(track, start_node, end)

        # for all neighbors of the current node do
        for i in range(4):
            dr = n[0] + dx[i]
            dc = n[1] + dy[i]
            if dr in range(len(graph)) and dc in range(len(graph[0])) and graph[dr][dc] != 'x':
            # if the current node isn't in both open_list and closed_list
            # add it to open_list and note n as it's parent
                if (dr, dc) not in open_list and (dr, dc) not in closed_list:
                    open_list.add((dr, dc))
                    track[dr][dc] = n
                    g[dr][dc] = g[n[0]][n[1]] + cost[dr][dc]
                    cost[dr][dc] = 10**9

            # otherwise, check if it's quicker to first visit n, then m
            # and if it is, update parent data and g data
            # and if the node was in the closed_list, move it to open_list
                else:
                    if g[dr][dc] > g[n[0]][n[1]] + cost[dr][dc]:
                        g[dr][dc] = g[n[0]][n[1]] + cost[dr][dc]
                        cost[dr][dc] = 10**9
                        track[dr][dc] = n

                        if (dr, dc) in closed_list:
                            closed_list.remove((dr, dc))
                            open_list.add((dr, dc))

        # remove n from the open_list, and add it to closed_list
        # because all of his neighbors were inspected
        open_list.remove(n)
        closed_list.add(n)

    print('Path does not exist!')
    return None