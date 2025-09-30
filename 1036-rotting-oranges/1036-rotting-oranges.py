from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #using bfs cox it's the rotting of neibhoring oranges at each minute.
        queue = deque() #empty array
        #this is a multisource bfs question, find all the rotten ones.

        rows, cols = len(grid), len(grid[0])
        b = True
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh+=1
                    
        if fresh == 0:
            return 0
        

        directions = [(-1,0),(0,-1), (1,0), (0,1)]
        minutes = 0
        while queue:
            l = len(queue)
            
            for i in range(l):
                r,c = queue.popleft()
                
                for dr, dc in directions:
                    if 0 <=dr+r< rows and 0<=dc+c <cols:
                        if grid[dr+r][dc+c]==1:
                            queue.append((dr+r, dc+c))
                            grid[dr+r][dc+c] = 2 #spoil it
                            fresh-=1
            minutes+=1

       
        return -1 if fresh>0 else minutes-1
        

                        

