"""
Problem 2: Banana Collector (2-D Grid DP)

You have a rectangular grid of bananas 🍌 where grid[r][c] represents bananas on cell (r, c).
You start at the top-left corner (0,0) and want to reach the bottom-right corner (m-1,n-1).
You can only move right or down.
Your task is to collect the maximum number of bananas possible.

👉 Example 1

"""
def max_bananas(grid):
    row, col = len(grid), len(grid[0])
    dp = [[0]*col for _ in range(row)]

    dp[0][0] = grid[0][0]

    for r in range(row):
        for c in range(col):
            if r ==0 and c == 0:
                continue 
            elif r == 0:
                dp[r][c] = dp[r][c-1]+grid[r][c]
            elif c == 0:
                dp[r][c] = dp[r-1][c]+grid[r][c]
            else: 
                dp[r][c] = max(dp[r-1][c], dp[r][c-1]) + grid[r][c] #left or right
    return dp[row-1][col-1]

print(max_bananas([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]))  # 29 ✅

print(max_bananas([
  [0, 2, 0],
  [3, 1, 5],
  [4, 2, 1]
]))  # 11 ✅
