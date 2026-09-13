class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        """
        Problem:
        n = number of nodes from 0-n-1 
        nums = increasing order
        maxDiff is used to determine if there's an undirected edge
        
        """
        results = [] 
        parent = {}
        i,j=0,0
        def find(node):
            path = []
            if node not in parent:
                    parent[node] = node
            while parent[node] != node:
                
                path.append(node)
                node = parent[node]
            top_boss = node
            for x in path:
                parent[x]=top_boss
            return node
        def union(u,v):
            rootu, rootv = find(u), find(v)
            if rootu!= rootv:
                parent[rootv] = rootu

        # Just check if each person can hold hands with the person directly to their right!
        for i in range(n - 1):
            if abs(nums[i] - nums[i+1]) <= maxDiff:
                union(i, i+1)

        for u,v in queries:
            if find(u)!=find(v):
                results.append(False)
            else:
                results.append(True)
        return results


                



        

        