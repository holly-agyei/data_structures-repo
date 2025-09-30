class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # a helper function to run through connected cities in an island and mark them as visited.

        def dfs_visit(r,c): #this doesnt return anything, but  to mark visits.
            #1 check if it's in bounds
            if (r<0 or r>= rows) or (c<0 or c>=cols):
                return #backtrack
            if grid[r][c] == "0":
                return
            grid[r][c] = "0" #mark visited
            directions = [(0,1),(0,-1), (-1,0), (1,0)]
            
            for dr,dc in directions:
                nr, nc = r+dr, c+dc 
                dfs_visit(nr, nc)
            
        #main fuction 
        rows, cols = len(grid), len(grid[0])
        island_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "0": #if not visited, remember it will always be in bounds, call dfs
                    dfs_visit(r,c)
                    island_count+=1
        return island_count

            




            
        