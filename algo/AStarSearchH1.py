from algo.graphAsset import *
import queue

def heuristic1(p1, p2, rewards):
    nearest_reward = 10**9
    for u, v, w in rewards:
        dist = abs(p1[0]-u) + abs(p1[1]-v)  + w + abs(u-p2[0]) + abs(v-p2[1])
        if dist < nearest_reward:
            nearest_reward = dist
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) + nearest_reward

def checkInReward(p, rewards):
    index = -1
    for i in range(len(rewards)):
        if rewards[i][0] == p[0] and rewards[i][1] == p[1]:
            index = i
    if index != -1:
        rewards.pop(index)

def aStarh1(graph, start, end, rewards=[]):
    open = []
    close = []
    f = [[10**10] * len(graph[i]) for i in range(len(graph))]
    g = [[10**10] * len(graph[i]) for i in range(len(graph))]
    track = [[(-1,-1)] * len(graph[i]) for i in range(len(graph))]
    open.append(start)
    g[start[0]][start[1]] = 0
    f[start[0]][start[1]] = 0
    cost = [[1] * len(graph[i]) for i in range(len(graph))]
    for u, v, w in rewards:
        cost[u][v] = w
    rows = len(graph)
    cols = len(graph[0])
    while len(open) != 0:
        min_index = 0
        for i in range(len(open)):
            u = open[min_index]
            v = open[i]
            if f[u[0]][u[1]] > f[v[0]][v[1]]:
                min_index = i
        u = open[min_index]
        checkInReward(u, rewards)
        close.append(u)
        if u == end:
            return findPath(track, start, end), g[u[0]][u[1]]
        for i in range(4):
            dr = u[0] + dx[i]
            dc = u[1] + dy[i]
            if dr in range (rows) and dc in range(cols) and graph[dr][dc] != 'x':
                if (dr, dc) not in open and (dr, dc) not in close:
                    g[dr][dc] = g[u[0]][u[1]] + cost[dr][dc]
                    f[dr][dc] = g[u[0]][u[1]] + heuristic1((dr, dc), end, rewards)
                    track[dr][dc] = u
                    open.append((dr, dc))
                elif (dr, dc) in open:
                    if g[dr][dc] > g[u[0]][u[1]] + cost[dr][dc]:
                        g[dr][dc] = g[u[0]][u[1]] + cost[dr][dc]
                        f[dr][dc] = g[dr][dc] + heuristic1((dr, dc), end, rewards)
                        track[dr][dc] = u
        open.pop(min_index)
    return [],0

