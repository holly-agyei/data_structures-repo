class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(-1,0),(0,-1),(1,0),(0,1)]
        count, max_count =0, 0

        def dfs(r,c):
            
            #whatever you take, you mark and call dfs on the neigbors.
            if grid[r][c] == 0:
                return
            grid[r][c] = 0
            nonlocal count
            count+=1
            for dr, dc in directions:
                if 0<=dr+r<rows and 0<=dc+c<cols:
                    dfs(dr+r, dc+c)

            return count 
        
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r,c)
                    max_count = max(count, max_count)
                    count=0

        return max_count
            
            