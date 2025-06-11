class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #define dfs helper function with iteration.
        def checknode(r,c):
            stack = [(r,c)]
            visited[r][c] = True
            area = 0

            while stack:
                cur_r,cur_c = stack.pop()
                area+=1

                for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                    nr,nc = cur_r+dr , cur_c +dc
                    #check for bounds and check validity
                    if 0<=nr<rows and 0<=nc<cols:
                        if not visited[nr][nc] and grid[nr][nc] ==1:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
            return area
        
        #now come to the main function
        cols, rows = len(grid[0]), len(grid)
        visited = [[False]*cols for _ in range(rows)]
        max_area=0

        for r in range(rows):
            for c in range(cols):
                #check if not visited and valid for functional call
                if not visited[r][c] and grid[r][c]==1:
                    area = checknode(r,c)
                    max_area = max(area, max_area)
        return max_area




