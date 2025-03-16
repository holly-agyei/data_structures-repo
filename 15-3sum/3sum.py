from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the numbers first
        nums.sort()
        results = []

        # Iterate through nums, fixing one element at a time
        for fixed in range(len(nums) - 2):
            if fixed > 0 and nums[fixed] == nums[fixed - 1]:  # Skip duplicates for fixed
                continue
            
            left, right = fixed + 1, len(nums) - 1  # Two-pointer approach

            while left < right:
                total = nums[fixed] + nums[left] + nums[right]

                if total == 0:
                    results.append([nums[fixed], nums[left], nums[right]])
                    
                    # Move both pointers while skipping duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1  # Increase sum by moving left pointer
                else:
                    right -= 1  # Decrease sum by moving right pointer

        return results

            
