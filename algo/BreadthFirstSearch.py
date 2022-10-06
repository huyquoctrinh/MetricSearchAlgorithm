import queue
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]


def findPath(track, start, end):
    path = []
    u, v = end[0], end[1]
    while True:
        if track[u][v] == (0,0):
            return path[::-1]
        u, v = track[u][v]
        path.append((u,v))
    return path

def bfsPath(graph, visited, start, end, path = []):
    q = queue.Queue()
    q.put(start)
    track = [[(0,0)] * len(graph[i]) for i in range(len(graph))]
    visited[start[0]][start[1]] = True
    while not q.empty():
        x, y = q.get()
        if x == end[0] and y == end[1]:
            return findPath(track, start, end)
        for t in range(4):
            dr = x + dx[t]
            dc = y + dy[t]
            
            if dr in range(len(graph)) and dc in range(len(graph[-1])) and not visited[dr][dc]:
                visited[dr][dc] = True
                q.put((dr, dc))
                track[dr][dc] = (x,y)
    return []
