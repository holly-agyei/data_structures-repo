class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #first get rotten oranges
        
        fresh = 0
        rotten = 0
        q = deque()
        rows, cols = len(grid), len(grid[0])
        time =0
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
       
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] ==1:
                    fresh+=1
        if fresh==0:
            return 0
        
        #perform bfs
        while q:
            
            for _ in range(len(q)): # need to keep track of the levels
                r,c =q.popleft()
                for dr, dc in directions:
                    nr,nc = r+dr, c+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                        grid[nr][nc] =2
                        q.append((nr,nc))
                        rotten+=1
            if q:
                time+=1
        return time if rotten == fresh else -1 

                
        
                    







        

        
        