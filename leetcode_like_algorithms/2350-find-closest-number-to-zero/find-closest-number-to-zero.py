class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        
        

        #this is like finding the absolute minimum in the array. (but in the case we nums like 1, -1), return the positive!

        for i in range(len(nums)):
            if abs(nums[i]) < abs(closest):
                closest = nums[i]
                
            if abs(nums[i]) == abs(closest) and nums[i]> closest:
                closest = nums[i]
               
                
            
            
        
        return closest
            

        
        