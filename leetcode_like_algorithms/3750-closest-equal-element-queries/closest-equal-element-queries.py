import bisect
from collections import defaultdict
from typing import List

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        my_map = defaultdict(list)

        for index, value in enumerate(nums):
            my_map[value].append(index)
        
        results = [-1]*len(queries)
        for index, q in enumerate(queries):
            positions = my_map[nums[q]]
            if len(positions)==1:
                continue
            k = len(positions)
            indexx = bisect.bisect_left(positions,q) #find the index at q in positions
            left_index = (indexx-1)%k
            right_index = (indexx+1)%k

            left = positions[left_index]
            right = positions[right_index]    

            if left !=q:
                distance = abs(q-left)
                circ_l = min(distance, n-distance)
            distance = abs(q-right)
            circ_r = min(distance, n-distance)

            results[index] = (min(circ_r, circ_l))
        return results


