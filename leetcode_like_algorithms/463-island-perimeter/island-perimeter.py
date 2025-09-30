class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        we are considering the outer parts only since we are taking the perimeter
        the outer parts are those that touches water (check the neighbours of each land cell)
        """
        # use bfs
        # any neighbour that is land is added. 
        # and one is subtracted.

        def bfs(r, c):
            queue = deque([(r, c)])
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            visited = set()
            visited.add((r, c))
            total_perimeter = 0

            while queue:
                r, c = queue.popleft()
                perimeter = 4
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols) and grid[nr][nc] == 1:
                        perimeter -= 1
                        if (nr, nc) not in visited:
                            queue.append((nr, nc))
                            visited.add((nr, nc))
                total_perimeter += perimeter
            return total_perimeter

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    ans = bfs(r, c)
                    return ans
