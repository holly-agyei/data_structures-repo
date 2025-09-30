class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        director = image[sr][sc]
        directions = [(-1,0),(0,-1), (1,0), (0,1)]
        rows, cols = len(image), len(image[0])

        def dfs(sr,sc):

            if image[sr][sc] != director or image[sr][sc] == color:
                return
    
            image[sr][sc] = color


            for dr, dc in directions:
                if 0<=dr+sr<rows and 0 <= dc+sc<cols:
                    dfs(dr+sr, dc+sc)
            
            
        
        dfs(sr,sc)
        return image
        
