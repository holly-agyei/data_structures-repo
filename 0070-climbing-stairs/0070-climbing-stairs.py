class Solution:
    def climbStairs(self, n: int) -> int:
        """
        -you must take one or two steps
        -steps to reach n can be steps to n-1 or steps to n-2
        -base case for buttom up
        dp[0] =1
        dp[1]=1
        """
        dp = [0]*(n+1) #n+1 for base case 0 
        dp[0],dp[1] = 1,1 

        for i in range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n] 

        