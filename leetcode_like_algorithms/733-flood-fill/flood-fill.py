class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def iterative_dfs(r,c):
            stack =[(r,c)]
            nonlocal color
            num = image[sr][sc]
            
            

            while stack:
                dr,dc = stack.pop()
                #change the color
                image[dr][dc] = color

                for fr,fc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = fr + dr, fc + dc
                    if 0<=nr<row and 0<=nc<col and image[nr][nc]==num:
                        stack.append((nr,nc))
                        image[nr][nc] = color

        if image[sr][sc] == color:
            return image
        row = len(image)
        col =len(image[0])
        iterative_dfs(sr,sc)
        return image


