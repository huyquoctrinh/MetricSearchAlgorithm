from copy import copy, deepcopy

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def findPath(track, start, end):
    path = []
    u, v = end[0], end[1]
    while True:
        path.append((u,v))
        if track[u][v] == (-1,-1):
            return path[::-1]
        u, v = track[u][v]
    return path