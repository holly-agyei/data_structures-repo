class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        from collections import defaultdict

        freq_map = defaultdict(int)

        for size in range(minSize, maxSize + 1):
            char_count = defaultdict(int)
            l = 0

            # Pre-fill the window
            for r in range(size):
                if r < len(s):
                    char_count[s[r]] += 1

            if len(char_count) <= maxLetters:
                freq_map[s[0:size]] += 1

            for r in range(size, len(s)):
                # Remove leftmost
                char_count[s[l]] -= 1
                if char_count[s[l]] == 0:
                    del char_count[s[l]]
                l += 1

                # Add rightmost
                char_count[s[r]] += 1

                if len(char_count) <= maxLetters:
                    substr = s[l:r + 1]
                    freq_map[substr] += 1

        return max(freq_map.values(), default=0)

            
                

          
        
        












