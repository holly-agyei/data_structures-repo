pairs = [("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "David"), ("Charlie", "David")]
nodes = ["Alice","Bob","Charlie","David"]
graph = {node:[] for node in nodes}

for u,v in pairs:
    graph[u].append(v)
    graph[v].append(u)

print(graph)