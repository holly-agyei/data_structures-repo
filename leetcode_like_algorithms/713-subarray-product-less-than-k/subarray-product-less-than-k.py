class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        im thinking of sliding window and being greeding but it will skip some 
        im like expand right while condition is valid and update result +1

       
        """
        count = 0
        product =1
        if k<=1:
            return 0

        l,r =0,0
        while r<len(nums):
            product*=nums[r]
            
            while product >= k and l<=r:
                product/=nums[l]
                l+=1
            count+=(r-l+1) #window size
            r+=1
        return count