class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        #if you want to see the future start from the end 
        stack = [] #keep track of biggest so far
        medium = float("-inf")


        for i in range(len(nums)-1,-1,-1):
            if nums[i]<medium:
                return True 
            while stack and nums[i]>stack[-1]:
                medium = stack.pop()
            stack.append(nums[i])
        
        return False
