from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def DFS(self,v,visited,res):
        visited.append(v)
        res.append(v)
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFS(neighbour,visited,res)
    def doDFS(self,v):
        visited = []
        res =[]
        self.DFS(v,visited,res)
        return res 
    def DFS_nondirected(self):
        visited = []
        res = []
        for v in self.graph:
            if (v not in visited):
                self.DFS(v,visited,res)
        return res

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
visited = []
res = []
print("Following is DFS from (starting from vertex 2)")
# Function call
res = g.doDFS(2)
print(res)
print(g.DFS_nondirected())