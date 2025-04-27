class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Use a visited container--a set is ideal
        
        Approach:
        set left and right. right expands and left shrinks
        expand while:
            the element at right is not in the set--thus we have non-repeating elements
            calculate the 
        shrink while:
        the element at right is in the set.
        """

        visited = set()
        left, right = 0, 0
        max_len = 0

        while right < len(s):
            if s[right] not in visited: #meaning theres no duplicate so add the character and update the max
                visited.add(s[right]) # add the char to the visited
                max_len = max(max_len, right-left+1) #update the max
                right+=1 #expand
            else: #when there's a duplicate like abca, move the pointer from "a" at the left
                visited.remove(s[left])
                left+=1 #shrink
        
        return max_len


            
            


                


