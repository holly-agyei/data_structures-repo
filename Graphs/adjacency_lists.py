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


#determine if there's a path between a start and end point:
def path(edges, start, end):
    edges = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("C", "E")
    ]
    #first make and adjacency list of which nodes are connected to the other. this is undirected
    node_set, node_lst = set(), []
    for x, y in edges:
        if x not in node_set:
            node_set.add(x)
            node_lst.append(y)

        if y not in node_set:
            node_set.add(y)
            node_lst.append(y)
    graph = {node: [] for node in node_lst}
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = set()
    def dfs(start, visited):
        if start in visited:
            return
        if start == end:
            return True #im thinking if we were finding and story all possible paths? how would we add ans to the res and backtrack
        visited.add(start)
        for nei in graph[start]:
            dfs(nei, visited)
            
        return False
        


