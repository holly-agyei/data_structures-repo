from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        result = [0] * n
        
        # copy elements less than pivot to the result array
        less_than_pivot_index = 0
        for i in range(n):
            if nums[i] < pivot:
                result[less_than_pivot_index] = nums[i]
                less_than_pivot_index += 1
        
        # copy elements equal to pivot to the result array
        equal_to_pivot_index = less_than_pivot_index
        for i in range(n):
            if nums[i] == pivot:
                result[equal_to_pivot_index] = nums[i]
                equal_to_pivot_index += 1
        
        # copy elements greater than pivot to the result array
        greater_than_pivot_index = equal_to_pivot_index
        for i in range(n):
            if nums[i] > pivot:
                result[greater_than_pivot_index] = nums[i]
                greater_than_pivot_index += 1
        
        return result

        