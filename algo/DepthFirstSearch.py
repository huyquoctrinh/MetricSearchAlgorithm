from algo.graphAsset import *

def dfsPath(graph, visited, start, end, path = []):
    q = [start]
    track = [[(0,0)] * len(graph[i]) for i in range(len(graph))]
    visited[start[0]][start[1]] = True
    while len(q) != 0:
        x, y = q.pop()
        if x == end[0] and y == end[1]:
            return findPath(track, start, end)
        for t in range(4):
            dr = x + dx[t]
            dc = y + dy[t]
            
            if dr in range(len(graph)) and dc in range(len(graph[-1])) and not visited[dr][dc]:
                visited[dr][dc] = True
                q.append((dr, dc))
                track[dr][dc] = (x,y)
    return []
