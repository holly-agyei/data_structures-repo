class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #strictly increasing
        #start and end index, else -1 -1
        #logn runtime 
        #edge case, if array is empty, return -1 -1

        """
        [1,3,4,4,4,5,6] #Binary search target 4
            l    r      
        [3,5,6,7,7,7,7,7,8] 
        [0]
        """
        if len(nums)==0:
            return [-1,-1]
        left_index = -1
        right_index = -1
        def binarysearch_left(nums,l,r):
            nonlocal left_index
            
            while l<=r:
                mid = (l+r)//2

                if nums[mid] == target:
                    if left_index ==-1:
                        left_index= mid
                    
                    left_index = min(left_index, mid)
                    r = mid-1
                elif nums[mid] > target:
                    r = mid-1
                elif nums[mid]<target:
                    l = mid+1
            return left_index
        def binarysearch_right(nums,l,r):
            nonlocal right_index 
            while l<=r:
                mid = (l+r)//2

                if nums[mid] == target:
                    right_index = max(right_index, mid)
                    l = mid+1
                elif nums[mid] > target:
                    r = mid-1
                elif nums[mid]<target:
                    l = mid+1
            return right_index 
        #cal function on nums
        left = binarysearch_left(nums, 0, len(nums)-1)
        right = binarysearch_right(nums,0,len(nums)-1)

        return [left,right]
            

                



