from algo.graphAsset import *
import queue

def bfsWithTeleportPath(graph, visited, start, end, teleports):
    q = queue.Queue()
    q.put(start)
    dist = [[-1] * len(graph[i]) for i in range(len(graph))]
    dist[start[0]][start[1]] = 0
    track = [[(-1,-1)] * len(graph[i]) for i in range(len(graph))]
    visited[start[0]][start[1]] = True
    while not q.empty():
        x, y = q.get()
        if x == end[0] and y == end[1]:
            return findPath(track, start, end), dist[x][y]
        for t in range(4):
            dr = x + dx[t]
            dc = y + dy[t]
            
            if dr in range(len(graph)) and dc in range(len(graph[-1])) and not visited[dr][dc]:
                visited[dr][dc] = True
                dist[dr][dc] = dist[x][y] + 1
                q.put((dr, dc))
                track[dr][dc] = (x,y)
        for u,v,uu,vv in teleports:
            if u==x and v==y:
                if graph[uu][vv] != 'x' and not visited[uu][vv]:
                    visited[uu][vv] = True
                    dist[uu][vv] = dist[x][y] 
                    q.put((uu, vv))
                    track[uu][vv] = (x,y)
    return [], 0

