class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #use bfs in the manner that, it goes level by level, the one with the shortest path will get there
        #first
        #it costs 1 to start
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        q = deque([(0,0,1)])
        direction = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1), (-1,-1)]
        s = len(grid)
        grid[0][0] = 1  # mark start as visited

        #visited? use inplace

        while q:
            r,c,path = q.popleft()
            #check the conditio
            
            
            if r == s-1 and c==s-1: #if found
                return path
            
            for dr,dc in direction:
                if dr+r<0 or dr+r>=s or dc+c<0 or dc+c>=s or grid[dr+r][dc+c] == 1:
                    continue 
                else:
                    q.append((dr+r,dc+c, path+1))
                    grid[dr+r][dc+c] = 1

        return -1      
                    
        
        