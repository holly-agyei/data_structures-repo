class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board[0] or not board: return 

        rows, cols = len(board), len(board[0])
        
        dummy = "boarder"
        parent = {dummy: dummy}

        #implement the union find
        def find(node): 
            path = []
            while parent[node] != node:
                path.append(node)
                node = parent[node]
            for a in path: #path compression is such that if we connect a boarder to a dummy, all it's generation is connected!!
                parent[a] = node
            return node 
        def union(u,v):
            rootu, rootv = find(u), find(v)
            if rootu!=rootv:
                parent[rootv]=rootu 
        
        #process the boards 2. union all edge cell to dummy
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    parent[(r,c)] = (r,c)
                    if r == 0 or r == rows-1 or c == 0 or c == cols-1:
                        parent[(r,c)] = find(dummy)
        #connect all inner cells as groups 
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    directions = [(0,1), (1,0)]
                    for dr, dc in directions:
                        nr,nc = dr+r, dc+c
                        if 0<=nr<rows and 0<=nc<cols and board[nr][nc] == "O":
                            union((r,c), (nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and find((r,c)) != find(dummy):
                    board[r][c]="X"
        
       
                            
        






        