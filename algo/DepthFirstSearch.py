# def dfsPath( graph, start, end, visited):
#     q = [start]
#     visited[start[0]][start[1]] = True
#     while not q.empty():
#         x, y = q.pop()
        
#         path.append((x, y))
#         for t in range(4):
#             dr = x + dx[t]
#             dc = y + dy[t]
#             if dr == end[0] and dc == end[1]:
#                 if len(path) == 0:
#                     return path
#                 else:
#                     return path[1:]
#             if dr in range(len(graph)) and dc in range(len(graph[-1])) and not visited[dr][dc]:
#                 visited[dr][dc] = False
#                 q.append((dr, dc))
#     return []
