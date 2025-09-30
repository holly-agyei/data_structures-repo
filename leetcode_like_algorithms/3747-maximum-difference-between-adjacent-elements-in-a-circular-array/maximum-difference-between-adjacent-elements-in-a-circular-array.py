class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        #circular array uses modulo
        max_diff = 0
        n = len(nums)
    
        for i in range(len(nums)):
            diff = max(abs(nums[i]-nums[(i-1)]), abs(nums[i]-nums[(i+1)%n]))
            max_diff = max(diff, max_diff)
        return max_diff
