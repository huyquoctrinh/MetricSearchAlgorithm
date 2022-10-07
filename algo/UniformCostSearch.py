from algo.graphAsset import *
import queue

class Point:
    def __init__(self, dis, u, v):
        self.dist = dis
        self.u = u
        self.v = v
    def __lt__(self, other):
        return self.dist < other.dist

def ucsPath(graph, start, end, rewards):
    dist = [[10**9] * len(graph[i]) for i in range(len(graph))]
    cost = [[1] * len(graph[i]) for i in range(len(graph))]
    track = [[(0,0)] * len(graph[i]) for i in range(len(graph))]
    for u, v, w in rewards:
        cost[u][v] = w
    u, v = start
    rows = len(graph)
    cols = len(graph[0])
    dist[u][v] = 0
    pq = queue.PriorityQueue()
    pq.put(Point(0, u, v))
    while not pq.empty():
        point = pq.get()
        w, u, v = point.dist, point.u, point.v
        if w > dist[u][v]:
            continue
        if u == end[0] and v == end[1]:
            return findPath(track, start, end)

        for i in range(4):
            dr = u + dx[i]
            dc = v + dy[i]
            if dr in range(rows) and dc in range(cols) and graph[dr][dc] != 'x':
                if w + cost[dr][dc] < dist[dr][dc]:
                    dist[dr][dc] = w + cost[dr][dc]
                    pq.put(Point(dist[dr][dc], dr, dc))
                    track[dr][dc] = (u, v)
                    cost[dr][dc] = 1 if cost[dr][dc] == 1 else (abs(cost[dr][dc]) + 1)
    return []
