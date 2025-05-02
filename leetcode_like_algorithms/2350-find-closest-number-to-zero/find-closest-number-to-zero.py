class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        value = nums[0]
        

        #loop through array to make every number positive and at the same time try to find the minimum.

        for i in range(len(nums)):
            if abs(nums[i]) < abs(closest):
                closest = nums[i]
                value = nums[i]
            if abs(nums[i]) == abs(closest) and closest != nums[i]:
                closest= max(nums[i], closest)
                value = closest
                
            
            
        
        return value
            

        
        