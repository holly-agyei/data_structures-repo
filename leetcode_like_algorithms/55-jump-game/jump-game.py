class Solution:
    def canJump(self, nums: List[int]) -> bool:
                
        target = len(nums)-1

        for i in range(target, -1,-1):
            #if your position + your jum >= target: set target

            if i+nums[i]>=target:
                target = i
                
            
            
        return target ==0