class Solution:
    def rob(self, nums: List[int]) -> int:
        #this is like house  robber I but we can't rob first and last together
        #we can either implement a logic or make our life simpler by dividing it into 2
        # from index 0 to n-2 and 1 to n-1
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        def dynamic(arr):
            if len(arr) == 1:
                return arr[0]
            dp = [0]*(len(arr))
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                dp[i] = max(dp[i-1], dp[i-2]+arr[i])


            return dp[len(arr)-1]
        
        case1 = dynamic(nums[:-1])
        case2 = dynamic(nums[1:])

        return max(case1, case2)


