from typing import List

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        
        """
        1. find the min of both nums1 and nums2 ---->  O(2N) Time
            2. If the are the same, like 3,3 return only one
            3. if they are not the same, like 5,1 return 15 (min, max), 
        
         """