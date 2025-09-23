from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #this is a multisource bfs
        queue = deque()
        rows, cols = len(mat), len(mat[0])
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r,c))
                else:
                    mat[r][c] = -1

        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        pd = 0 
        while queue:
            l = len(queue)
            pd+=1
            for i in range(l):
                r,c = queue.popleft()

                for dr, dc in directions:
                    if 0<=dr+r<rows and 0<=dc+c<cols:
                        if mat[dr+r][dc+c] == -1:
                            mat[dr+r][dc+c] = pd
                            queue.append((dr+r, dc+c))
           

        return mat


        

