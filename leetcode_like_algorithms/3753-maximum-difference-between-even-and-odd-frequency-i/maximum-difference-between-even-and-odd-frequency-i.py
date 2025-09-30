from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)

        odd_freqs = [v for v in count.values() if v % 2 == 1]
        even_freqs = [v for v in count.values() if v % 2 == 0]

        if not odd_freqs or not even_freqs:
            return -1 
        return max(odd_freqs)-min(even_freqs)
        