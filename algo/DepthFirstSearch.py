def dfs( graph, node, visited):
    
    if node not in visited:

        # print(node)
        visited.add(node)

    for neighbour in graph[node]:
        dfs(visited, graph, neighbour)
