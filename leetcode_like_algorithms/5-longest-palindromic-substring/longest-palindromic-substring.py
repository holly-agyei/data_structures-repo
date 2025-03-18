class Solution:
    def longestPalindrome(self, s: str) -> str:

            #expand around the center algorithm
        def expand(s, left, right):
            while left >= 0 and right< len(s) and s[right] == s[left]:
                left-=1
                right+=1

            return s[left+1:right]
        final = ""
        for i in range(len(s)):
            odd_pal = expand(s,i,i)
            even_pal = expand(s,i,i+1)

            longest = odd_pal if len(odd_pal) > len(even_pal) else even_pal

            if len(longest)>len(final):
                final = longest
        return final
          
