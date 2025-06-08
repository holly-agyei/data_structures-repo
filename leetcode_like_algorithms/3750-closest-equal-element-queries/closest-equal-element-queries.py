import bisect
from collections import defaultdict
from typing import List

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        numMap = defaultdict(list)

        # Step 1: Store sorted positions of each number
        for idx, val in enumerate(nums):
            numMap[val].append(idx)

        result = []

        for q in queries:
            val = nums[q]
            positions = numMap[val]

            # If the number occurs only once, no neighbor to compare
            if len(positions) == 1:
                result.append(-1)
                continue

            i = bisect.bisect_left(positions, q)
            best = float('inf')

            # Left neighbor (wraps around if needed)
            left = positions[(i - 1) % len(positions)]
            if left != q:
                dist = abs(left - q)
                best = min(best, min(dist, n - dist))

            # Right neighbor (wraps around if needed)
            right = positions[(i + 1) % len(positions)]
            if right != q:
                dist = abs(right - q)
                best = min(best, min(dist, n - dist))

            result.append(best)

        return result
