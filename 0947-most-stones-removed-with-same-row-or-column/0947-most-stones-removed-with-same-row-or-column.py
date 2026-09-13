class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        unique_bosses = set()

        def find(node):
            path = []
            if node not in parent:
                parent[node] = node
            while parent[node] != node:
                path.append(node)
                node = parent[node]
            top_boss = node
                #path compression
            for each in path:
                parent[each] = top_boss
            return top_boss 

        def union(u,v):
            rootu, rootv = find(u), find(v)
            if rootu!= rootv:
                parent[rootv] = rootu 

        for r,c in stones:
            union(r, c+10001)
        for r,c in stones:
            boss = find(r)
            unique_bosses.add(boss) 
        
        return len(stones)- len(unique_bosses)

