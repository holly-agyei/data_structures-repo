from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        Divide the array at the rotation pivot, then run binary search on each half.
        The pivot is detected where nums[i] < nums[i-1].
        """

        # nested binary search helper
        def bin_search(arr: List[int], tgt: int) -> bool:
            lo, hi = 0, len(arr) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if arr[mid] == tgt:
                    return True
                elif arr[mid] < tgt:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return False

        n = len(nums)
        # handle single-element case
        if n == 1:
            return nums[0] == target

        # find pivot index (last index of the first sorted segment)
        pivot = 0
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                pivot = i - 1
                break

        # split into two sorted subarrays
        left_half = nums[:pivot + 1]
        right_half = nums[pivot + 1:]

        # search in either half using the nested helper
        return bin_search(left_half, target) or bin_search(right_half, target)


            

        