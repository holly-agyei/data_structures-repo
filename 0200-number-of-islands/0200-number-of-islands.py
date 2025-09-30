class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        stack = []

        #the idea is that if u see a zero, reverse...if u see a one, continue
        def dfs(r,c):
            stack.append((r,c))
            visited.add((r,c))
            while stack:
                r,c = stack.pop()
    

                directions = [(1,0), (0,1), (-1,0), (0,-1)]
                for dr, dc in directions:
                    nr, nc = dr+r, dc+c
                    if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and grid[nr][nc]=="1": #if it's in bounds
                        stack.append((nr,nc))
                        visited.add((nr,nc))

        rows, cols, count= len(grid), len(grid[0]), 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    dfs(r,c)
                    count+=1
        return count


                




