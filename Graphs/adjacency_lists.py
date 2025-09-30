from collections import deque
#ADJACENCY LISTS
edges = [("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "David"), ("Charlie", "David")]
nodes = ["Alice","Bob","Charlie","David"]
graph = {node:[] for node in nodes}

for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)

print(graph)

#BFS ON GRAPHS
"""
You’re given the friendship graph (Alice, Bob, Charlie, David).
Use BFS starting from "Alice" to print the order in which people get the news.
"""
def bfs(graph, start):
    q = deque()
    q.append(start)
    lst, visited = [], set()
    while q:
        node = q.popleft()
        lst.append(node)
        for nei in graph[node]: 
            if nei not in visited:
                visited.add(nei)
                q.append(nei)
    return lst
print(bfs(graph, "Alice"))