class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #we can define dp to be many stuff( that how i understand it)
        #here we take dp[i] cost to reach + be able to go over I. so dp[i] will include paying the cost[i]
        #In that case, dp[anwer] will be dp[n] or dp[last but one], cox from there u will be able to jump over.
        n = len(cost)

        dp = [0]*(n) #the lenght of the dp arr is not always n+1, here we started from cost[0] for base case, and we want to get to dp[n-1 or n] so the array lenght should just be as cost. | how or which strategy can i use to always see the array lenght?
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[n-1], dp[n-2])

