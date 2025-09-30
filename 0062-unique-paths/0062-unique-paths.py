class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #imagine you are in the inner cell:
        #you only got there either from the top or from the left( 2 ways to get to each inner cell)
        #one way to get around all c=0, or r=0 cells.

        dp = [[0]*n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if c==0 or r==0:
                    dp[r][c] = 1
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1] #left or right

        return dp[m-1][n-1]