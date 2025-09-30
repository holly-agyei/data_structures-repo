class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #in place-->red white blue -->0,1,2
        #whatever i do, the nums should sorted 
        #[0001111222]

        #do pointer approach in two runs 
        #swap zeros and others in the case that whenever you see a zero, swap with the swap point

        if len(nums)<2:
            return nums
        
        right, left = 0,0
        while left< len(nums):
            if nums[left]==0:#swap
                nums[left], nums[right]=nums[right],nums[left]
                right+=1
            
            left+=1

      

        #set the pointer at 2 starting.
        
        while right<len(nums) and nums[right] != 2:
            right+=1
            
        left =right
        while left< len(nums) and right < len(nums)-1:
            if nums[left]==1:#swap
                nums[left], nums[right]=nums[right],nums[left]
                right+=1
            
            left+=1
        






        