from algo.graphAsset import *
import queue

# def heuristic(p1, p2):
#     x1, y1 = p1
#     x2, y2 = p2
#     return abs(x1 - x2) + abs(y1 - y2)
    
def heuristic2(p1, p2, rewards):
    nearest_reward = 10**9
    for u, v, w in rewards:
        dist = abs(p1[0]-u) + abs(p1[1]-v) + w
        if dist < nearest_reward:
            nearest_reward = dist
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) + nearest_reward
    
def gbfsPath(graph, start, end, rewards=[]):
    track = [[(-1, -1)] * len(graph[i])for i in range(len(graph))]
    cost = [[1] * len(graph[i]) for i in range(len(graph))]
    dist = [[10**9] * len(graph[i]) for i in range(len(graph))]
    for u, v, w in rewards:
        cost[u][v] = w
    pq = queue.PriorityQueue()
    pq.put((0, start))
    visited = []
    rows = len(graph)
    cols = len(graph[-1])
    visited.append(start)
    while not pq.empty():
        weight, point = pq.get()
        if point == end:
            return findPath(track, start, end)
        if (point[0], point[1], cost[point[0]][point[1]]) in rewards:
            rewards.pop(rewards.index((point[0], point[1], cost[point[0]][point[1]])))
        if weight > dist[point[0]][point[1]]:
            continue
        for i in range(4):
            dr = point[0] + dx[i]
            dc = point[1] + dy[i]
            new_point = (dr, dc)
            if dr in range(rows) and dc in range(cols) and graph[dr][dc] != 'x':
                if (dr, dc) not in visited:
                    visited.append((dr, dc))
                    dist[dr][dc] = heuristic2(new_point, end, rewards) + weight
                    pq.put((dist[dr][dc], (dr, dc)))
                    track[dr][dc] = point
                    
    return []
                
