from algo.graphAsset import *
import queue

def sortPointsByDistanceToCurrentPoint(start, pickUpPoint=[]):
    for i in range(len(pickUpPoint) - 1):
        for j in range(i+1, len(pickUpPoint)):
            if (abs(pickUpPoint[i][0] - start[0]) + abs(pickUpPoint[i][1] - start[1])) > (abs(pickUpPoint[j][0] - start[0]) + abs(pickUpPoint[j][1] - start[1])):
                tmp = pickUpPoint[i]
                pickUpPoint[i] = pickUpPoint[j]
                pickUpPoint[j] = tmp
          
def dijkstraPath(graph, v, start, end):
    marked = deepcopy(v)
    q = queue.Queue()
    q.put(start)
    track = [[(-1, -1)]* len(graph[i]) for i in range(len(graph))]
    marked[start[0]][start[1]] = True
    dist = [[0] * len(graph[i]) for i in range(len(graph))]
    while not q.empty():
        u = q.get()
        if u == end:
            return findPath(track, start, end), dist[u[0]][u[1]]
        for i in range(4):
            dr = u[0] + dx[i]
            dc = u[1] + dy[i]
            if dr in range(len(graph)) and dc in range(len(graph[0])) and graph[dr][dc] != 'x':
                if not marked[dr][dc]:
                    q.put((dr, dc))
                    dist[dr][dc] = dist[u[0]][u[1]] + 1
                    marked[dr][dc] = True
                    track[dr][dc] = u
    return [], 0
    
def algo1Path(graph, visited, start, end, r=[]):
    pickUpPoints = r.copy()
    visited[start[0]][start[1]] = True
    track = [[(-1, -1)] * len(graph[i]) for i in range(len(graph))]
    
    disjPath = []
    total_cost = 0
    while len(pickUpPoints) != 0:
        sortPointsByDistanceToCurrentPoint(start, pickUpPoints)
        path, cost = dijkstraPath(graph, visited, start, (pickUpPoints[0][0], pickUpPoints[0][1]))
        if len(path) == []:
            return [], 0
        total_cost += cost
        prev = start
        visited[start[0]][start[1]] = True
        for p in path:
            track[p[0]][p[1]] = prev
            prev = p
            disjPath.append(p)
        start = (pickUpPoints[0][0], pickUpPoints[0][1])
        if len(pickUpPoints) != 0:
            pickUpPoints.pop(0)
    path, cost = dijkstraPath(graph, visited, start, end)
    if len(path) == []:
        return [], 0
    total_cost += cost
    prev = start
    for p in path:
        track[p[0]][p[1]] = prev
        prev = p
        disjPath.append(p)
    return disjPath, total_cost
