class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Use a visited container
        """
        l,r = 0,0
        visited = set()
        max_len = 0

        if len(s) ==1:
            return 1
        if not s:
            return 0  


        while r < len(s):
            if s[r] not in visited:
                visited.add(s[r])
                
                max_len = max(max_len, r-l+1)
                r+=1
            else:
                visited.remove(s[l])
                l+=1

        return max_len

"space and time complexity analysis"
time: O(N)
        