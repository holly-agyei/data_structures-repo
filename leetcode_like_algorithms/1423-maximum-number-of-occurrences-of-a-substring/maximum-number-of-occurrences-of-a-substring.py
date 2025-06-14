class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        l, r = 0, 0
        substrings = {}  # To count valid substrings and how many times they appear
        window = {}      # To track character frequency in the current window

        while r < len(s):
            # Step 1: Expand window by adding character at index r
            window[s[r]] = window.get(s[r], 0) + 1

            # Step 2: Shrink window if it exceeds minSize
            while (r - l + 1) > minSize:
                # Reduce the count of the leftmost character
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]  # Clean up if count becomes zero
                l += 1  # Move the left side of the window to the right

            # Step 3: When window is exactly minSize, check and count substring
            if (r - l + 1) == minSize:
                if len(window) <= maxLetters:
                    substr = s[l:r + 1]  # Get the current substring
                    substrings[substr] = substrings.get(substr, 0) + 1

            # Step 4: Move right side of window
            r += 1

        # Step 5: Return the maximum frequency found (or 0 if no valid substrings)
        return max(substrings.values(), default=0)




            
                

          
        
        












