from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #this screams number of islands but not lol
        #u need to make an adjacency list first. 

        
        row, col = len(isConnected), len(isConnected[0])
        graph = {i:[] for i in range(row)}

        for r in range(row):
            for c in range(col):
                if isConnected[r][c] == 1:
                    graph[r].append(c)
        print(graph)
        visited = set()
        count = 0 
        for start in graph:
            if start in visited:
                continue 
            stack = [(start)]
            while stack:
                node = stack.pop()
                if node in visited:
                    continue 
                visited.add(node)
                for nei in graph[node]:
                    if nei not in visited:
                        stack.append(nei)
            count+=1 

        return count 
                            
