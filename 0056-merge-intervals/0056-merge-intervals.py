from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort them
        intervals.sort(key = lambda x: x[0])

        #handle none case:
        if not intervals:
            return []


        merged = []

        merged.append(intervals[0])

        #loop
        for interval in intervals[1:]:
            last = merged[-1]

            if interval[0]<=last[1]:
                merged[-1][-1] = max(interval[1], last[1])
            else:
                #just append
                merged.append(interval)
        return merged
