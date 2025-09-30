class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        stack = []

        def dfs(r,c):
            stack.append((r,c,0, {(r,c)}))

            while stack:
                r,c,idx, visited = stack.pop()
                

                if idx ==len(word)-1:
                    return True

                directions = [(-1,0), (0,-1), (1,0), (0,1)]
                for dr, dc in directions:
                    if 0<=dr+r<rows and 0<=dc+c<cols and (dr+r, dc+c) not in visited:
                        if board[dr+r][dc+c] == word[idx+1]:
                            stack.append((dr+r, dc+c, idx+1, visited|{(dr+r, dc+c)}))
            return False

        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    x = dfs(r,c)
                    if not x:
                        continue
                    else:
                        return x
        return False
        


