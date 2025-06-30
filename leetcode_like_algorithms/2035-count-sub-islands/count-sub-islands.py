class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        """
        -this is more like counting the number of islands with a twist 
        -for each island in grid 2, we want to check if it's a sub island in grid 1
        -how? 

        approach:
        run dfs on grid 2 to find the islands
        for each island in two, check if all the cells are also 1(lands) in grid 1.
        update the count
        """
        row, col = len(grid1), len(grid1[0])
        def dfs(r,c):
            stack = [(r, c)]
            is_sub = True

            while stack:
                x,y = stack.pop()

                if grid1[x][y] == 0:
                    is_sub = False
                grid2[x][y]=0
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = dx+x , dy+y

                    if 0<=nr<row and 0<=nc<col and grid2[nr][nc]==1:
                        stack.append((nr,nc))
            return is_sub
        
        row, col = len(grid1), len(grid1[0])
        count = 0
        for r in range(row):
            for c in range(col):
                if grid2[r][c] ==1: #theres a potential start
                    if dfs(r,c):
                        count+=1
        return count