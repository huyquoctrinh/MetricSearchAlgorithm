import queue

def bfs(graph, node, visited, path = []):
    queue = [node]
    visited.append(node)
    while queue:
        v = queue.pop(0)
        
        path.append(v)

        for neighbour in graph[v]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return path
