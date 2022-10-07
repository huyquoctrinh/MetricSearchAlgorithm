from algo.graphAsset import *
import queue

class Point:
    def __init__(self, dis, u, v):
        self.dist = dis
        self.u = u
        self.v = v
    def __lt__(self, other):
        return self.dist < other.dist
    
def printArray(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end = ' ')
        print()

def ucsPath(graph, start, end, rewards=[]):
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
    pq.put((0, start))
    visited = []
    while not pq.empty():
        w, point = pq.get()
        visited.append(point)
        if point == end:
            return findPath(track, start, end)
        u, v = point
        for i in range(4):
            dr = u + dx[i]
            dc = v + dy[i]
            if dr in range(rows) and dc in range(cols) and graph[dr][dc] != 'x':
                if (dr, dc) not in visited:
                    pq.put((w + cost[dr][dc], (dr, dc)))
                    track[dr][dc] = (u, v)
    return []

