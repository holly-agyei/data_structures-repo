class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # Dictionary to store frequency counts of valid substrings
        substrings = {}
        
        # Dictionary to keep count of characters currently in the sliding window
        window = {}
        
        # Left pointer of the sliding window
        l = 0

        # Iterate through the string with right pointer 'r'
        for r in range(len(s)):
            # Add current character s[r] to the window frequency dictionary
            window[s[r]] = window.get(s[r], 0) + 1

            # If current window size exceeds the minimum size,
            # shrink the window from the left by removing s[l]
            if r - l + 1 > minSize:
                window[s[l]] -= 1  # Decrement count of leftmost char
                if window[s[l]] == 0:
                    del window[s[l]]  # Remove char if count becomes zero
                l += 1  # Move left pointer to the right, shrinking window
            
            # When the current window size is exactly minSize,
            # check if it satisfies the unique letter constraint
            if r - l + 1 == minSize and len(window) <= maxLetters:
                substring = s[l:r+1]  # Extract current substring
                # Update count of this substring in the frequency dictionary
                substrings[substring] = substrings.get(substring, 0) + 1

        # Return the maximum frequency of any valid substring,
        # or 0 if no valid substring was found
        return max(substrings.values(), default=0)


