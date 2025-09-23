from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        count = 0

        max_num = max(freq.values())
        print(freq, max_num)

        b = sum(y for x,y in freq.items() if y== max_num)

        return b
        

        