class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        minimum = nums[0]
        value = nums[0]
        

        #loop through array to make every number positive and at the same time try to find the minimum.

        for i in range(len(nums)):
            if abs(nums[i]) < abs(minimum):
                minimum = nums[i]
                value = nums[i]
            if abs(nums[i]) == abs(minimum) and minimum != nums[i]:
                minimum = max(nums[i], minimum)
                value = minimum
                
            
            
        
        return value
            

        
        