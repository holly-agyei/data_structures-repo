from typing import List

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        
        """
        1. find the min of both nums1 and nums2 ---->  O(2N) Time
            2. If the are the same, like 3,3 return only one
            3. if they are not the same, like 5,1 return 15 (min, max), 
        
         """
        
        if min(nums1) == min(nums2):
            return min(nums1) 
        
        maxx = max(min(nums1), (min(nums2)))  #5 from testcase1
        minn = min(min(nums1), (min(nums2)))  #1 from testcase1
        
        # I Check if there's a common number in both lists so i return the smallest common
        common = set(nums1).intersection(nums2)   #O(1)
        if common:
            return min(common)  
        
        #if none of the conditions apply, return min,max
        return int(f"{minn}{maxx}")

        #or i can return (10*minn + max) in mathematical perspective
         l,r = 0, len(nums)-1
        
        while l<=r:
            mid = (l+r)//2
            """"""
               