from algo.graphAsset import *
import queue

def heuristic(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)
    
def heuristic2(p1, p2, rewards):
    nearest_reward = 10**9
    for u, v, w in rewards:
        dist = abs(p1[0]-u) + abs(p1[1]-v) + w
        if dist < nearest_reward:
            nearest_reward = dist
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) + nearest_reward

def sortRewardByDistanceToPoint(start, rewards=[]):
    # rewards = sorted(rewards, lambda x : (abs(rewards[x][0] - start[0]) + abs(rewards[x][1] - start[1])))
    for i in range(len(rewards) - 1):
        for j in range(i+1, len(rewards)):
            if (abs(rewards[i][0] - start[0]) + abs(rewards[i][1] - start[1])) > (abs(rewards[j][0] - start[0]) + abs(rewards[j][1] - start[1])):
                tmp = rewards[i]
                rewards[i] = rewards[j]
                rewards[j] = tmp
          
def gbfs(graph, v, start, end):
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
    
def gbfsPath(graph, visited, start, end, r=[]):
    rewards = r.copy()
    #visited = [[False] * len(graph[i]) for i in range(len(graph))]
    visited[start[0]][start[1]] = True
    track = [[(-1, -1)] * len(graph[i]) for i in range(len(graph))]
    
    greedyPath = []
    total_cost = 0
    while len(rewards) != 0:
        sortRewardByDistanceToPoint(start, rewards)
        path, cost = gbfs(graph, visited, start, (rewards[0][0], rewards[0][1]))
        if len(path) == []:
            return [], 0
        total_cost += cost + rewards[0][2]
        prev = start
        visited[start[0]][start[1]] = True
        for p in path:
            track[p[0]][p[1]] = prev
            prev = p
            greedyPath.append(p)
        start = (rewards[0][0], rewards[0][1])
        if len(rewards) != 0:
            rewards.pop(0)
    path, cost = gbfs(graph, visited, start, end)
    if len(path) == []:
        return [], 0
    total_cost += cost
    prev = start
    for p in path:
        track[p[0]][p[1]] = prev
        prev = p
        greedyPath.append(p)
    return greedyPath, total_cost
# def gbfsPath(graph, start, end, rewards=[]):
#     track = [[(-1, -1)] * len(graph[i])for i in range(len(graph))]
#     cost = [[1] * len(graph[i]) for i in range(len(graph))]
#     dist = [[10**9] * len(graph[i]) for i in range(len(graph))]
#     for u, v, w in rewards:
#         cost[u][v] = w
#     pq = queue.PriorityQueue()
#     pq.put((0, start))
#     visited = []
#     rows = len(graph)
#     cols = len(graph[-1])
#     visited.append(start)
#     while not pq.empty():
#         weight, point = pq.get()
#         if point == end:
#             return findPath(track, start, end)
#         if (point[0], point[1], cost[point[0]][point[1]]) in rewards:
#             rewards.pop(rewards.index((point[0], point[1], cost[point[0]][point[1]])))
#         if weight > dist[point[0]][point[1]]:
#             continue
#         for i in range(4):
#             dr = point[0] + dx[i]
#             dc = point[1] + dy[i]
#             new_point = (dr, dc)
#             if dr in range(rows) and dc in range(cols) and graph[dr][dc] != 'x':
#                 if (dr, dc) not in visited:
#                     visited.append((dr, dc))
#                     dist[dr][dc] = heuristic2(new_point, end, rewards) + weight
#                     pq.put((dist[dr][dc], (dr, dc)))
#                     track[dr][dc] = point
                    
#     return []



