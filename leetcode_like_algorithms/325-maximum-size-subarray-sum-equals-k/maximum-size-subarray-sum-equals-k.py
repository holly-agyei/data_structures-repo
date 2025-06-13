class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix = {0: [0]}  # Now 0 is at index 0
        total = 0
        max_len = 0

        for i, num in enumerate(nums):
            total += num

            if (total - k) in prefix:
                start_idx = min(prefix[total - k])
                max_len = max(max_len, i - start_idx + 1)  # Add +1

            if total not in prefix:
                prefix[total] = []
            prefix[total].append(i + 1)  # because 0 is at index 0

        return max_len
