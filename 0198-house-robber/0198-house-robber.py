class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*(len(nums)+1)
        dp[0] = 0
        dp[1] = nums[0] #max money to rob from house one u can always rob from house one for the start. 

        for i in range(2, len(nums)+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1]) #be careful of indexing!!

        return dp[len(nums)]

        